import json
import os
import uuid
from pathlib import Path
import glob
import shutil

def find_page_image(image_dir, page_num):
    # Look for any image file that starts with page_X where X is the page number
    pattern = os.path.join(image_dir, f"page_{page_num}*.png")
    matches = glob.glob(pattern)
    
    # If there are multiple matches, prefer the one without _img_ suffix
    # as that's likely the main page image
    if matches:
        main_page_images = [m for m in matches if "_img_" not in m]
        return main_page_images[0] if main_page_images else matches[0]
    return None

def convert_to_qwen_format(module_path, output_path, central_images_dir):
    # Read the text content
    text_file = os.path.join(module_path, f"{os.path.basename(module_path)}_text.json")
    with open(text_file, 'r', encoding='utf-8') as f:
        text_content = json.load(f)
    
    # Get image directory
    image_dir = os.path.join(module_path, "images")
    
    # Create output directory if it doesn't exist
    os.makedirs(output_path, exist_ok=True)
    
    # Initialize the Qwen dataset
    qwen_dataset = []
    
    # Process each page
    for page in text_content:
        page_num = page["page"]
        text = page["text"].strip()
        
        # Skip empty pages
        if not text:
            continue
            
        # Find corresponding image
        image_path = find_page_image(image_dir, page_num)
        if not image_path:
            print(f"Warning: No image found for page {page_num}")
            continue
            
        # Copy image to central images directory with unique name
        image_filename = f"{os.path.basename(module_path)}_page_{page_num}.png"
        output_image_path = os.path.join(central_images_dir, image_filename)
        shutil.copy2(image_path, output_image_path)
        
        # Create conversation in Qwen format
        conversation = [
            {
                "role": "user",
                "content": [
                    {
                        "image": output_image_path
                    },
                    {
                        "text": "Explain the content of this page from the AI course material."
                    }
                ]
            },
            {
                "role": "assistant",
                "content": text
            }
        ]
        
        # Create sample
        sample = {
            "id": str(uuid.uuid4()),
            "conversations": conversation
        }
        
        qwen_dataset.append(sample)
    
    # Save the converted dataset
    output_file = os.path.join(output_path, f"{os.path.basename(module_path)}_qwen.json")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(qwen_dataset, f, ensure_ascii=False, indent=2)
    
    return output_file

def main():
    # Path to extracted content
    extracted_dir = os.path.join("src", "pdf_processing", "extracted_content")
    output_dir = os.path.join("src", "convert_to_llava_format", "qwen_training_data")
    
    # Create central images directory
    central_images_dir = os.path.join(output_dir, "images")
    os.makedirs(central_images_dir, exist_ok=True)
    
    # Process each module
    for module in os.listdir(extracted_dir):
        module_path = os.path.join(extracted_dir, module)
        if os.path.isdir(module_path):
            print(f"Processing {module}...")
            output_file = convert_to_qwen_format(module_path, output_dir, central_images_dir)
            print(f"Created {output_file}")

if __name__ == "__main__":
    main() 