## Key Components

### Content Organization

- **extracted_content/**: Contains processed course materials organized by modules
  - Each module directory (e.g., `M1-strategie-recherche/`) contains:
    - `images/`: Extracted images from course materials
    - `*_text.json`: Extracted text content
    - `*_summary.json`: Module summaries and metadata

### Training Pipeline

- **LLaVA/**: Contains the core LLaVA model implementation and training scripts
- **llava_training_data/**: Houses the formatted training data ready for model consumption
  - Includes conversation pairs and image references structured for LLaVA training

### Processing Tools

- **pdf_processing/**: Tools for extracting and processing content from PDF documents
- **src/**: Custom implementation for data processing and format conversion

## Project Structure and Organization

The project follows a clear separation of concerns between framework code and project-specific code:

- **LLaVA/**: Contains the core LLaVA framework code
  - Base model implementation
  - Training infrastructure
  - Core vision-language model capabilities
  - `train_llava.py`: Configures and runs the LLaVA training process

- **src/**: Contains project-specific code
  - Custom data processing and conversion utilities
  - `convert_to_llava_format.py`: Converts course materials into LLaVA training format
  - Handles project-specific data structures and requirements

This separation allows for:
- Clear distinction between framework and project code
- Easier maintenance and updates of both components
- Better organization of project-specific adaptations
- Cleaner integration with the LLaVA framework

## Setup and Installation

1. Install required dependencies:
```bash
pip install -r requirements.txt
```

2. Set up the LLaVA environment:
```bash
# Create and activate conda environment
conda create -n llava python=3.10
conda activate llava

# Install PyTorch and other dependencies
pip install torch torchvision torchaudio
```

3. Prepare the training data:
   - Place course materials in `Class docs/`
   - Run PDF processing scripts to extract content
   - Verify extracted content in `extracted_content/`

## Training Process

1. Data Preparation:
   - Course materials are processed and organized by module
   - Images and text are extracted and structured
   - Content is converted to LLaVA training format

2. Model Training:
```bash
python train_llava.py
```

The training script is configured to:
- Use BF16 precision for efficient training
- Implement gradient accumulation for memory efficiency
- Save checkpoints periodically
- Handle modular course content structure

## Model Configuration

The training configuration includes:
- Base model: LLaVA-v1.5-7b
- Vision encoder: CLIP ViT-L/14
- Training parameters:
  - Learning rate: 2e-5
  - Batch size: 1 (with gradient accumulation)
  - Training epochs: 1
  - Weight decay: 0
  - Warmup ratio: 0.03

## Requirements

- Python 3.10+
- PyTorch
- Transformers library
- CUDA-capable GPU (recommended)
- See `requirements.txt` for complete list of dependencies

## Notes

- The project is structured to handle modular course content
- Training data is organized by course modules for better management
- Image processing maintains original module structure
- Checkpoints are saved regularly during training

## Future Improvements

- Implement validation pipeline
- Add support for additional document formats
- Enhance image processing capabilities
- Implement multi-GPU training support

## License

[Specify your license here]
