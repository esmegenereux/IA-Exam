git clone https://github.com/haotian-liu/LLaVA.git
cd LLaVA

# Create and activate environment
conda create -n llava python=3.10 -y
conda activate llava

# python packages
python -m pip install --upgrade pip
pip install -e .
pip install bitsandbytes accelerate peft
pip install wandb scipy
pip install datasets
pip install opencv-python
pip install pillow
pip install timm
pip install einops
pip install einops-exts
pip install markdown2[all]
pip install gradio
pip install gradio_client
pip install fastapi
pip install uvicorn
pip install httpx
pip install requests
pip install scikit-learn
pip install sentencepiece
pip install tokenizers
pip install transformers

# Given your specific use case (training on class notes and running on a USB key with school computers), I'll recommend the most practical approach:
#
# For the base model, I recommend downloading the LLaVA-1.5-7B model because:
# - It's the smallest model that still maintains good performance
# - It will fit better on your 64GB USB key (the model weights are about 14GB)
# - It will be more manageable to run on school computers
# - It will be faster to train on your class notes
# 
# You'll need to download:
# 1. The base model weights
# 2. The vision encoder weights
# 3. The projection weights
# 
# Here's how we can download them:

python -c "from huggingface_hub import snapshot_download; snapshot_download(repo_id='liuhaotian/llava-v1.5-7b', local_dir='./model')"
python -c "from huggingface_hub import snapshot_download; snapshot_download(repo_id='openai/clip-vit-large-patch14-336', local_dir='./model/clip-vit-large-patch14-336')"

# Next steps would be:
# - Prepare your class notes for training (you'll need to convert them into a format that LLaVA can understand)
# - Fine-tune the model on your notes
# - Test the model to ensure it works correctly
# - Package everything for the USB key

# Preparing your class notes for training
# You'll need to:
# - Gather all your notes in digital format
# - Convert them into a format that LLaVA can understand (we'll need to create a dataset with questions and answers)
# - Prepare the training configuration
# We can use both your class notes and open-source AI educational materials to train the model. 

# For converting your notes and preparing the training data, we'll need to create a dataset in a specific format. LLaVA uses a JSON format where each training example contains:
# An image (optional, but useful for diagrams or visual concepts)
# A conversation with questions and answers
# Metadata about the conversation

# Here's how we can structure this:
# 1. First, let's create a directory for your training data:
mkdir -p data/train

# 2. Now, let's create a template for your training data. I'll create a Python script that will help you convert your notes into the required format:
# added data/prepare_training_data.py

# 3. Now, to use this script:
# Create a text file named your_notes.txt in the same directory as the script
# Format your notes in one of these ways:
    What is AI?: AI is the simulation of human intelligence in machines...
    What are neural networks?: Neural networks are computing systems...
OR
    AI is the simulation of human intelligence in machines...
    Neural networks are computing systems...


# To use these PDFs for training LLaVA, we'll need to:
# 1. Extract text and images from the PDFs
# 2. Convert the content into the LLaVA training format (JSON with text-image pairs)
# 3. Organize the extracted images in the correct directory structure