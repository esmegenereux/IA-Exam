# LLaVA Course Material Training Project

This project enables training a LLaVA (Large Language and Vision Assistant) model on course materials, allowing it to understand and explain educational content that combines text and images.

## What You Can Do With This Project

1. **Process Course Materials**
   - Extract text and images from PDF course materials
   - Organize content by modules
   - Convert materials into a format suitable for AI training

2. **Train a Custom LLaVA Model**
   - Fine-tune LLaVA on your specific course content
   - Create a model that understands your course's unique terminology and structure
   - Generate explanations of course materials

3. **Manage Training Data**
   - Organize course materials by modules
   - Process and format images and text
   - Create structured training datasets

## Project Structure

### Core Components

- **LLaVA/**: Core framework code
  - Base model implementation
  - Training infrastructure
  - `train_llava.py`: Training configuration and execution

- **src/**: Project-specific code
  - `convert_to_llava_format.py`: Data conversion utilities
  - Custom processing scripts

- **extracted_content/**: Processed course materials
  - Organized by modules (e.g., `M1-strategie-recherche/`)
  - Contains images and text content
  - Includes module summaries

- **llava_training_data/**: Formatted training data
  - Structured conversation pairs
  - Image references
  - Ready for model training

- **pdf_processing/**: PDF extraction tools
  - Content extraction utilities
  - Image processing scripts

## Getting Started

### Prerequisites

- Python 3.10+
- CUDA-capable GPU (recommended)
- Sufficient disk space for course materials and model checkpoints

### Installation

1. Clone the repository and initialize submodules:
```bash
git clone https://github.com/esmegenereux/LLaVA.git
cd LLaVA
git submodule update --init --recursive
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up LLaVA environment:
```bash
conda create -n llava python=3.10
conda activate llava
python -m pip install --upgrade pip
pip install torch==2.2.0 torchvision==0.17.0 torchaudio==2.2.0 --index-url https://download.pytorch.org/whl/cu118
pip install -e .
pip uninstall bitsandbytes
```

## Usage Guide

### 1. Prepare Course Materials

1. Place your course materials in `Class docs/`
2. Run PDF processing scripts to extract content
3. Verify extracted content in `extracted_content/`

### 2. Convert to Training Format

Run the conversion script:
```bash
python src/convert_to_llava_format.py
```

This will:
- Process extracted content
- Create training-ready datasets
- Organize data in `llava_training_data/`

### 3. Train the Model

Start training:
```bash
python LLaVA/train_llava.py
```

The training process:
- Uses BF16 precision for efficiency
- Implements gradient accumulation
- Saves checkpoints periodically
- Handles modular course content

## Current Configuration

- Base model: LLaVA-v1.5-7b
- Vision encoder: CLIP ViT-L/14
- Training parameters:
  - Learning rate: 2e-5
  - Batch size: 1 (with gradient accumulation)
  - Training epochs: 1
  - Weight decay: 0
  - Warmup ratio: 0.03

## Model Export and Deployment

### Exporting the Model

1. **Prepare the Model for Export**
   ```bash
   # Navigate to the checkpoints directory
   cd checkpoints
   
   # The model checkpoints are saved in the format:
   # checkpoint-{step}/
   # Choose the latest or best checkpoint
   ```

2. **Export to USB Key**
   ```bash
   # Create a directory on your USB key
   mkdir /path/to/usb/llava_model
   
   # Copy the model files
   cp -r checkpoints/checkpoint-{step}/* /path/to/usb/llava_model/
   
   # Copy necessary configuration files
   cp LLaVA/config.json /path/to/usb/llava_model/
   cp LLaVA/tokenizer.json /path/to/usb/llava_model/
   ```

3. **Verify Export**
   - Check that all files are copied successfully
   - Ensure the USB key has sufficient space (model size ~7GB)
   - Verify file permissions are correct

### Using the Model from USB

1. **Setup on Target Machine**
   ```bash
   # Create a directory for the model
   mkdir -p ~/llava_model
   
   # Copy from USB to local storage
   cp -r /path/to/usb/llava_model/* ~/llava_model/
   
   # Install required dependencies
   pip install -r requirements.txt
   ```

2. **Load and Use the Model**
   ```python
   from llava.model.builder import load_pretrained_model
   import torch
   
   # Load the model with optimizations for lower RAM usage
   tokenizer, model, image_processor, context_len = load_pretrained_model(
       model_path="~/llava_model",
       model_base=None,
       vision_tower="openai/clip-vit-large-patch14-336",
       load_4bit=True,  # Enable 4-bit quantization
       device_map="auto"  # Automatically handle device placement
   )
   
   # Additional optimizations
   model = model.to(torch.float16)  # Use half precision
   torch.cuda.empty_cache()  # Clear GPU cache if using CUDA
   
   # Use the model for inference
   # (Add your inference code here)
   ```

3. **Performance Considerations**
   - Minimum RAM requirement: 8GB (with optimizations)
   - Recommended RAM: 16GB for better performance
   - Use CUDA if available for better performance
   - Monitor memory usage during inference
   - Consider using model quantization for lower memory usage

### Optimizing for Lower RAM Usage

1. **Quantization Techniques**
   ```python
   # 4-bit quantization (reduces memory usage by ~75%)
   model = model.quantize(bits=4)
   
   # 8-bit quantization (reduces memory usage by ~50%)
   model = model.quantize(bits=8)
   ```

2. **Memory-Efficient Loading**
   ```python
   # Load model in chunks
   model = load_pretrained_model(
       model_path="~/llava_model",
       load_in_8bit=True,  # 8-bit loading
       device_map="auto"   # Smart device placement
   )
   ```

3. **Additional Optimizations**
   - Use gradient checkpointing during training
   - Enable model pruning
   - Use dynamic batching
   - Implement memory-efficient attention

4. **RAM Usage Breakdown**
   - Base model: ~7GB
   - With 8-bit quantization: ~3.5GB
   - With 4-bit quantization: ~1.75GB
   - Additional overhead: ~1GB
   - Total minimum requirement: ~8GB

### Portable Usage Tips

1. **Model Optimization**
   - Consider using model quantization for smaller file size
   - Use half-precision (FP16) for reduced memory usage
   - Remove unnecessary model components if possible

2. **Storage Requirements**
   - Full model: ~7GB
   - Quantized model: ~3.5GB
   - Additional space for temporary files during inference

3. **Compatibility**
   - Ensure target machine has compatible Python version (3.10+)
   - Verify CUDA version compatibility if using GPU
   - Check for sufficient disk space and memory

## Next Steps

1. **Immediate Improvements**
   - Implement validation pipeline
   - Add support for additional document formats
   - Enhance image processing capabilities
   - Implement multi-GPU training support

2. **Model Enhancement**
   - Experiment with different model architectures
   - Fine-tune hyperparameters
   - Add support for more complex course structures

3. **Feature Development**
   - Add interactive model testing
   - Implement content generation capabilities
   - Develop evaluation metrics
   - Create visualization tools for training progress

4. **Documentation**
   - Add detailed API documentation
   - Create usage examples
   - Document best practices
   - Add troubleshooting guide

## License

[Specify your license here]
