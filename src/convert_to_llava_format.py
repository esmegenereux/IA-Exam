import json
import os
import uuid
from pathlib import Path
import glob

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

def convert_to_llava_format(module_path, output_path):
    # Read the text content
    text_file = os.path.join(module_path, f"{os.path.basename(module_path)}_text.json")
    with open(text_file, 'r', encoding='utf-8') as f:
        text_content = json.load(f)
    
    # Get image directory
    image_dir = os.path.join(module_path, "images")
    
    # Create output directory if it doesn't exist
    os.makedirs(output_path, exist_ok=True)
    
    # Initialize the LLaVA dataset
    llava_dataset = []
    
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
            
        # Create conversation
        conversation = [
            {
                "from": "human",
                "value": f"<image>\nExplain the content of this page from the AI course material."
            },
            {
                "from": "gpt",
                "value": text
            }
        ]
        
        # Create sample
        sample = {
            "id": str(uuid.uuid4()),
            "image": image_path,
            "conversations": conversation
        }
        
        llava_dataset.append(sample)
    
    # Save the converted dataset
    output_file = os.path.join(output_path, f"{os.path.basename(module_path)}_llava.json")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(llava_dataset, f, ensure_ascii=False, indent=2)
    
    return output_file

def main():
    # Path to extracted content
    extracted_dir = "extracted_content"
    output_dir = "llava_training_data"
    
    # Process each module
    for module in os.listdir(extracted_dir):
        module_path = os.path.join(extracted_dir, module)
        if os.path.isdir(module_path):
            print(f"Processing {module}...")
            output_file = convert_to_llava_format(module_path, output_dir)
            print(f"Created {output_file}")

if __name__ == "__main__":
    main() 