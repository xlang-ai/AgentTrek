export OPENAI_API_KEY="YOUR_OPENAI_API_KEY"
export AGENTLAB_EXP_ROOT="./results"


export BASE_URL="YOUR_BASE_URL"
export WA_SHOPPING="${BASE_URL}:7770/"
export WA_SHOPPING_ADMIN="${BASE_URL}:7780/admin"
export WA_REDDIT="${BASE_URL}:9999"
export WA_GITLAB="${BASE_URL}:8023"
export WA_WIKIPEDIA="${BASE_URL}:8888/wikipedia_en_all_maxi_2022-05/A/User:The_other_Kiwix_guy/Landing"
export WA_MAP="${BASE_URL}:3000"
export WA_HOMEPAGE="${BASE_URL}:4399"

python run_exp.py --benchmark webarena \
    --model-name "agenttrek-instruct-32b" \
    --n-jobs 10