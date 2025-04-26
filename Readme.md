# LLaVA Course Material Training Project

This project enables training a LLaVA (Large Language and Vision Assistant) model on course materials, allowing it to understand and explain educational content that combines text and images.

## Quick Start Guide

### 1. Prepare Your Environment

```bash
# Create and activate conda environment
conda create -n llava python=3.10
conda activate llava

# Install PyTorch (choose appropriate version for your system)
pip3 install torch torchvision torchaudio

# Install LLaVA and other dependencies
pip install -r requirements.txt
```

### 2. Organize Your Course Materials

1. Place your PDF course materials in the `Class docs` directory:
```
Class docs/
├── module1.pdf
├── module2.pdf
└── ...
```

2. Run the PDF processing script:
```bash
python src/pdf_processing/pdf_extractor.py
```

This will create processed content in:
```
extracted_content/
├── module1/
│   ├── images/
│   ├── module1_text.json
│   └── module1_summary.json
├── module2/
│   ├── images/
│   ├── module2_text.json
│   └── module2_summary.json
└── ...
```

### 3. Convert to Training Format

```bash
# Convert your course materials to LLaVA training format
python src/convert_to_llava_format.py
```

This will create training data in:
```
src/llava_training_data/
├── module1_llava.json
├── module2_llava.json
└── ...
```

### 4. Train the Model

```bash
# Start the training process
python LLaVA/train_llava.py
```

The training will:
- Use your course materials as training data
- Save checkpoints periodically
- Log training progress
- Handle modular course content structure

## Project Structure

### Core Components

- **LLaVA/**: Core framework code
  - Base model implementation
  - Training infrastructure
  - `train_llava.py`: Training configuration and execution

- **src/**: Project-specific code
  - `convert_to_llava_format.py`: Data conversion utilities
  - `pdf_processing/`: PDF extraction and processing tools
  - `llava_training_data/`: Formatted training data

- **Class docs/**: Original course materials
  - PDF documents
  - Organized by modules

- **extracted_content/**: Processed course materials
  - Organized by modules
  - Contains images and text content
  - Includes module summaries

## Training Configuration

The training process uses the following settings:
- Base model: LLaVA-v1.5-7b
- Vision encoder: CLIP ViT-L/14
- Training parameters:
  - Learning rate: 2e-5
  - Batch size: 1 (with gradient accumulation)
  - Training epochs: 1
  - Weight decay: 0
  - Warmup ratio: 0.03

## System Requirements

- Python 3.10+
- CUDA-capable GPU (recommended)
- Minimum RAM: 8GB (with optimizations)
- Recommended RAM: 16GB for better performance
- Sufficient disk space for:
  - Course materials
  - Model checkpoints
  - Training data

## Troubleshooting

### Common Issues

1. **PyTorch Installation**
   - If CUDA version issues occur, try:
     ```bash
     pip3 install torch torchvision torchaudio
     ```

2. **Memory Issues**
   - Enable model quantization
   - Use gradient checkpointing
   - Reduce batch size

3. **Training Data Format**
   - Verify JSON structure
   - Check image paths
   - Ensure proper module organization

## Next Steps

1. **Model Enhancement**
   - Experiment with different architectures
   - Fine-tune hyperparameters
   - Add support for more complex structures

2. **Feature Development**
   - Add interactive testing
   - Implement content generation
   - Develop evaluation metrics

3. **Documentation**
   - Add API documentation
   - Create usage examples
   - Document best practices

## License

[Specify your license here]
