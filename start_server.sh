#!/bin/bash

# Activate the virtual environment
source qwen_env/bin/activate

# Start the model server
python -m vllm.entrypoints.openai.api_server \
    --model Qwen/Qwen-VL-Chat \
    --trust-remote-code \
    --host 0.0.0.0 \
    --port 8000 