import argparse
import logging
import bgym

from agentlab.agents.generic_agent.generic_agent import GenericAgentArgs
from agentlab.agents.generic_agent.generic_agent_prompt import GenericPromptFlags
from agentlab.llm.chat_api import OpenAIModelArgs
from agentlab.agents import dynamic_prompting as dp
from agentlab.experiments.study import Study

logging.getLogger().setLevel(logging.INFO)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run experiments with specified parameters",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="Example: python run_exp.py --benchmark miniwob --n-jobs 4",
    )

    # Add command line arguments with more detailed help
    parser.add_argument(
        "--reproducibility-mode",
        action="store_true",
        help='Enable reproducibility mode. This will "ask" agents to be deterministic '
        "and prevent launching with local changes.",
    )

    parser.add_argument(
        "--benchmark",
        type=str,
        default="miniwob",
        choices=["miniwob_tiny_test", "miniwob", "workarena_l1", "webarena",  "workarena_l2_agent_curriculum_eva", "workarena_l3_agent_curriculum_eval", "webarena_tiny"],
        help="Benchmark to run on. Options include:\n"
        "- miniwob_tiny_test: Small test benchmark\n"
        "- miniwob: Standard miniwob benchmark\n"
        "- workarena_l1/l2/l3: Different levels of workarena\n"
        "- webarena_tiny: Tiny webarena benchmark\n"
        "(default: %(default)s)",
    )

    parser.add_argument(
        "--relaunch",
        action="store_true",
        help="Relaunch an existing study. This will continue incomplete "
        "experiments and relaunch errored experiments.",
    )

    parser.add_argument(
        "--n-jobs",
        type=int,
        default=1,
        help="Number of parallel jobs to run. Use 1 for debugging in VSCode. "
        "Set higher for parallel processing. (default: %(default)s)",
    )

    parser.add_argument(
        "--n-relaunch",
        type=int,
        default=1,
        help="Number of times to retry launching experiments. "
        "Useful for handling transient errors. (default: %(default)s)",
    )

    parser.add_argument(
        "--model-name",
        type=str,
        required=True,
    )

    return parser.parse_args()


def create_agent_args(model_name: str) -> GenericAgentArgs:
    model_args = OpenAIModelArgs(
        model_name=model_name, max_total_tokens=32_000, max_input_tokens=30_000, max_new_tokens=2_000, temperature=0.7
    )

    prompt_flags = GenericPromptFlags(
        obs=dp.ObsFlags(
            use_html=False,
            use_ax_tree=True,
            use_focused_element=False,
            use_error_logs=True,
            use_history=True,
            use_past_error_logs=False,
            use_action_history=True,
            use_think_history=False,
            use_diff=False,
            html_type="pruned_html",
            use_screenshot=False,
            use_som=False,
            extract_visible_tag=False,
            extract_clickable_tag=False,
            extract_coords="False",
            filter_visible_elements_only=False,
        ),
        action=dp.ActionFlags(
            action_set=bgym.HighLevelActionSetArgs(
                subsets=["bid"],
                multiaction=False,
            ),
            long_description=False,
            individual_examples=False,
        ),
        use_plan=False,
        use_criticise=False,
        use_thinking=True,  # Remember to change this
        use_memory=True,
        use_concrete_example=True,
        use_abstract_example=True,
        use_hints=False,
        enable_chat=False,
        max_prompt_tokens=25_000,
        be_cautious=True,
        extra_instructions=None,
    )

    return GenericAgentArgs(
        chat_model_args=model_args,
        flags=prompt_flags,
    )


def run_study(args: argparse.Namespace) -> None:
    agent_args = [create_agent_args(model_name=args.model_name)]
    if args.reproducibility_mode:
        [a.set_reproducibility_mode() for a in agent_args]

    if args.relaunch:
        #  relaunch an existing study
        study = Study.load_most_recent(contains=None)
        study.find_incomplete(include_errors=True)
    else:
        study = Study(agent_args, args.benchmark, logging_level_stdout=logging.WARNING)

    study.run(
        n_jobs=args.n_jobs,
        parallel_backend="ray",
        strict_reproducibility=args.reproducibility_mode,
        n_relaunch=args.n_relaunch,
    )

    if args.reproducibility_mode:
        study.append_to_journal(strict_reproducibility=True)


def main() -> None:
    args = parse_args()
    run_study(args)


if __name__ == "__main__":
    main()