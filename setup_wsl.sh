#!/bin/bash

git lfs install
git clone https://huggingface.co/Qwen/Qwen-VL-Chat path/to/qwen-vl-chat

# Create and activate virtual environment
python3 -m venv qwen_env
source qwen_env/bin/activate

# Update Ubuntu
sudo apt update && sudo apt upgrade -y

# Install Python and CUDA-friendly PyTorch
sudo apt install -y python3-pip git

# Install CUDA 11.4
wget https://developer.download.nvidia.com/compute/cuda/11.4.0/local_installers/cuda_11.4.0_470.42.01_linux.run
sudo sh cuda_11.4.0_470.42.01_linux.run --silent --toolkit
rm cuda_11.4.0_470.42.01_linux.run

# Add CUDA to PATH
echo 'export PATH=/usr/local/cuda-11.4/bin${PATH:+:${PATH}}' >> ~/.bashrc
echo 'export LD_LIBRARY_PATH=/usr/local/cuda-11.4/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}' >> ~/.bashrc
source ~/.bashrc

# Upgrade pip
pip install --upgrade pip

# Install deep learning libraries with CUDA 11.4
pip install torch==2.6.0 torchvision==0.21.0 torchaudio==2.6.0 --index-url https://download.pytorch.org/whl/cu118
pip install transformers datasets peft bitsandbytes accelerate deepspeed

# (Optional) Install xformers for faster training
pip install xformers

echo "Setup complete! Please activate the virtual environment with:"
echo "source qwen_env/bin/activate" 