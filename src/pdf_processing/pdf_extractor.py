import os
import json
import fitz  # PyMuPDF
from pathlib import Path
from PyPDF2 import PdfReader
from PIL import Image

class PDFExtractor:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path
        self.pdf_name = Path(pdf_path).stem
        # Create output directories if they don't exist
        self.output_dir = Path('src/pdf_processing/extracted_content') / self.pdf_name
        self.images_dir = self.output_dir / 'images'
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.images_dir.mkdir(parents=True, exist_ok=True)

    def extract_text(self):
        """Extract text from PDF and save it page by page."""
        reader = PdfReader(self.pdf_path)
        text_content = []
        
        for page_num, page in enumerate(reader.pages, 1):
            text = page.extract_text()
            if text.strip():  # Only add non-empty pages
                text_content.append({
                    'page': page_num,
                    'text': text
                })
        
        # Save text content to JSON
        text_file = self.output_dir / f'{self.pdf_name}_text.json'
        with open(text_file, 'w', encoding='utf-8') as f:
            json.dump(text_content, f, ensure_ascii=False, indent=2)
        
        return text_content

    def extract_images(self):
        """Extract images from PDF using PyMuPDF."""
        try:
            doc = fitz.open(self.pdf_path)
            image_paths = []
            
            for page_num, page in enumerate(doc, 1):
                # Get the page as an image
                pix = page.get_pixmap()
                image_path = self.images_dir / f'page_{page_num}.png'
                pix.save(str(image_path))
                image_paths.append(str(image_path))
                
                # Extract embedded images
                image_list = page.get_images()
                for img_idx, img in enumerate(image_list, 1):
                    xref = img[0]
                    base_image = doc.extract_image(xref)
                    if base_image:
                        image_bytes = base_image["image"]
                        image_ext = base_image["ext"]
                        image_path = self.images_dir / f'page_{page_num}_img_{img_idx}.{image_ext}'
                        with open(image_path, 'wb') as img_file:
                            img_file.write(image_bytes)
                        image_paths.append(str(image_path))
            
            doc.close()
            return image_paths
        except Exception as e:
            print(f"Error extracting images: {e}")
            return []

    def process_pdf(self):
        """Process the PDF to extract both text and images."""
        print(f"Processing PDF: {self.pdf_path}")
        
        # Extract text
        print("Extracting text...")
        text_content = self.extract_text()
        print(f"Extracted text from {len(text_content)} pages")
        
        # Extract images
        print("Extracting images...")
        image_paths = self.extract_images()
        print(f"Extracted {len(image_paths)} images")
        
        # Create a summary of the extraction
        summary = {
            'pdf_name': self.pdf_name,
            'total_pages': len(text_content),
            'total_images': len(image_paths),
            'text_file': f'{self.pdf_name}_text.json',
            'image_directory': str(self.images_dir)
        }
        
        # Save summary
        summary_file = self.output_dir / f'{self.pdf_name}_summary.json'
        with open(summary_file, 'w', encoding='utf-8') as f:
            json.dump(summary, f, indent=2)
        
        return summary

def main():
    # Process all PDFs in the Class docs directory
    pdf_dir = Path('src/pdf_processing/Class docs')
    if not pdf_dir.exists():
        print(f"Error: Directory '{pdf_dir}' not found")
        return

    for pdf_file in pdf_dir.glob('*.pdf'):
        extractor = PDFExtractor(str(pdf_file))
        summary = extractor.process_pdf()
        print(f"\nProcessed {pdf_file.name}:")
        print(json.dumps(summary, indent=2))

if __name__ == '__main__':
    main() 