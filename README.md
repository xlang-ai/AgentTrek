# AgentTrek: Agent Trajectory Synthesis via Guiding Replay with Web Tutorials

<p align="center">
        📑 <a  href="https://arxiv.org/abs/2412.09605" target="_blank">Paper</a> &nbsp&nbsp  </a> | &nbsp&nbsp 🌐 <a href="https://agenttrek.github.io/" target="_blank">Project Page</a> &nbsp&nbsp | &nbsp&nbsp 💾 <a href="https://huggingface.co/collections/ranpox/agenttrek-browser-use-agent-data-synthesis-6794a7cebb90c5ccdb9a3068" target="_blank"> AgentTrek Data Collection</a> &nbsp&nbsp
<br>

## intruduction
AgentTrek is a cost-efficient and scalable framework that synthesizes high-quality agent trajectories by guiding replay with web tutorials. These collected trajectories significantly enhance agent performance.
<p align="center">
    <img src="https://agenttrek.github.io/images/pipeline.png" type="image/jpg"/>
<p>

### Key Features & Contributions
- 🔄 **Scalable Data Synthesis Pipeline**: Cost-efficient and scalable pipeline to synthesize high-quality agent trajectories.
- 📊 **Comprehensive Dataset**: Largest-scale dataset of browseruse agent trajectories with multimodal grounding and reasoning.
- 🤖 **Capable Brouwseruse Agent**: Fully autonomous browseruse agent capable for performing general tasks.

### BrowserGym LeaderBoard </a> 🌐 <a href="https://huggingface.co/spaces/ServiceNow/browsergym-leaderboard" target="_blank">Browsergym LeaderBoard</a>
| Agent | WebArena | WorkArena-L1 | WorkArena-L2 | WorkArena-L3 | MiniWoB |
|-------|----------|--------------|--------------|--------------|---------|
| Claude-3.5-Sonnet | 36.20 | 56.40 | 39.10 | 0.40 | 69.80 |
| GPT-4o | 31.40 | 45.50 | 8.50 | 0.00 | 63.80 |
| GPT-o1-mini | 28.60 | 56.70 | 14.90 | 0.00 | 67.80 |
| Llama-3.1-405b | 24.00 | 43.30 | 7.20 | 0.00 | 64.60 |
| **AgentTrek-32b**💫 | **22.40** | **38.29** | **2.98** | **0.00** | **60.00** |
| Llama-3.1-70b | 18.40 | 27.90 | 2.10 | 0.00 | 57.60 |
| GPT-4o-mini | 17.40 | 27.00 | 1.30 | 0.00 | 56.60 |

Our Browseruse agent demonstrate exceptional performance in real-world online scenarios:

## Getting Started

### Installation

1. Clone the repository:
```bash
git clone ...
cd agenttrek
```

2. Create and activate a conda environment:
```bash
conda create -n agenttrek python=3.10
conda activate agenttrek
```

3. Install PyTorch and dependencies:
```bash
pip install -e .
```
### Data Preparation


### Training


### Model Checkpoints
- AgentTrek-7B: cooking🧑‍🍳
- AgentTrek-32B: [model](https://huggingface.co/xlangai/AgentTrek-1.0-32B)
- AgentTrek-72B: cooking🧑‍🍳

### Evaluation

**MiniWob++ Evaluation**
1. Configure your evaluation settings:
   - Open `scripts/run_webarena.sh`
   - Set the `OPENAI_API_KEY` variable to your own openai api key
   - Set the `AGENTLAB_EXP_ROOT` variable to specify the path for the results
   - Set the `MINIWOB_URL` variable to your Miniwob URL 
   - Set the `OPENAI_BASE_URL` variable to specify your model base url

2. Start inference:
```bash
bash scripts/run_miniwob.sh
```

**WebArena Evaluation**

1. Configure your evaluation settings:
   - Open `scripts/run_webarena.sh`
   - Set the `OPENAI_API_KEY` variable to your own OpenAI API key
   - Set the `AGENTLAB_EXP_ROOT` variable to specify the path for the results
   - Set the following URL variables for the relevant platforms:
     - `BASE_URL`: Specify the base URL for your WebArena instance
     - `WA_SHOPPING`: URL for the Shopping benchmark
     - `WA_SHOPPING_ADMIN`: URL for the Shopping Admin benchmark
     - `WA_REDDIT`: URL for the Reddit benchmark
     - `WA_GITLAB`: URL for the GitLab benchmark
     - `WA_WIKIPEDIA`: URL for the Wikipedia benchmark
     - `WA_MAP`: URL for the Map benchmark
     - `WA_HOMEPAGE`: URL for the Homepage benchmark
   - Set the `OPENAI_BASE_URL` variable to specify your model base URL

2. Start inference:
```bash
bash scripts/run_webarena.sh
```
