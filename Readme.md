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
src/pdf_processing/extracted_content/
├── module1/
│   ├── images/
│   │   ├── page_1.png
│   │   ├── page_2.png
│   │   └── ...
│   ├── module1_text.json
│   └── module1_summary.json
├── module2/
│   ├── images/
│   │   ├── page_1.png
│   │   ├── page_2.png
│   │   └── ...
│   ├── module2_text.json
│   └── module2_summary.json
└── ...
```

### 3. Convert to Training Format

```bash
# Convert your course materials to LLaVA training format
python src/convert_to_llava_format/convert_to_llava_format.py
```

This will create training data in:
```
src/convert_to_llava_format/llava_training_data/
├── images/
│   ├── module1_page_1.png
│   ├── module1_page_2.png
│   ├── module2_page_1.png
│   └── ...
├── module1_llava.json
├── module2_llava.json
└── ...
```

The conversion process:
1. Creates a central `images` directory containing all course images
2. Renames images to include module and page information
3. Generates LLaVA-format JSON files with proper image references
4. Maintains the relationship between text and images

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

### 5. Export to USB Key

After processing and training, you can export the data to a USB key for backup or transfer:

1. **Prepare the USB Key**
   - Ensure the USB key has sufficient space (recommended minimum 32GB)
   - Format the USB key as exFAT for cross-platform compatibility
   - Create a dedicated folder for the export (e.g., `llava_training_data_export`)

2. **Export the Data**
   ```bash
   # Create export directory on USB key
   mkdir /path/to/usb/llava_training_data_export
   
   # Copy the training data
   cp -r src/convert_to_llava_format/llava_training_data/* /path/to/usb/llava_training_data_export/
   ```

3. **Verify the Export**
   - Check that all files are copied successfully
   - Verify the directory structure matches the original
   - Ensure all image files are present and accessible
   - Test opening a few JSON files to verify integrity

4. **Important Considerations**
   - The export includes:
     - All processed images
     - LLaVA format JSON files
     - Training checkpoints (if any)
   - Excluded files:
     - Original PDFs (to save space)
     - Temporary processing files
     - Git repository data
   - Recommended minimum free space on USB key: 32GB
   - For large datasets, consider using compression:
     ```bash
     # Create a compressed archive
     tar -czf llava_training_data.tar.gz src/convert_to_llava_format/llava_training_data/
     ```

5. **Cross-Platform Compatibility**
   - Use exFAT file system for the USB key
   - Avoid special characters in filenames
   - Keep file paths under 260 characters
   - Use lowercase for all filenames

## Project Structure

### Core Components

- **LLaVA/**: Core framework code
  - Base model implementation
  - Training infrastructure
  - `train_llava.py`: Training configuration and execution

- **src/**: Project-specific code
  - `convert_to_llava_format/`: Data conversion utilities
    - `convert_to_llava_format.py`: Main conversion script
    - `llava_training_data/`: Formatted training data
  - `pdf_processing/`: PDF extraction and processing tools
    - `pdf_extractor.py`: PDF processing script
    - `extracted_content/`: Processed course materials

- **Class docs/**: Original course materials
  - PDF documents
  - Organized by modules

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

4. **Image Processing**
   - Verify all images are copied to the central images directory
   - Check image naming convention
   - Ensure JSON files reference correct image paths

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
