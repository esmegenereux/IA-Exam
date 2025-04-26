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

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set up LLaVA environment:
```bash
conda create -n llava python=3.10
conda activate llava
pip install torch torchvision torchaudio
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
