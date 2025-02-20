export OPENAI_API_KEY="YOUR_OPENAI_API_KEY"
export AGENTLAB_EXP_ROOT="./results"
export MINIWOB_URL="YOUR_MINIWOB_PATH"

python run_exp.py --benchmark miniwob \
    --model-name "agenttrek-instruct-32b" \
    --n-jobs 10