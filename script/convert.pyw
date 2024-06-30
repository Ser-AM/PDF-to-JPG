import os
import fitz  # PyMuPDF
from PIL import Image

def pdf_to_image(pdf_path, output_path, target_width=200, target_height=283):
    try:
        pdf_document = fitz.open(pdf_path)
        first_page = pdf_document.load_page(0)
        pix = first_page.get_pixmap()
        image = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

        image_ratio = image.width / image.height
        target_ratio = target_width / target_height

        if image_ratio > target_ratio:
            new_width = target_width
            new_height = int(target_width / image_ratio)
        else:
            new_height = target_height
            new_width = int(target_height * image_ratio)

        resized_image = image.resize((new_width, new_height), Image.LANCZOS)  # Cambiado a LANCZOS
        final_image = Image.new("RGB", (target_width, target_height), (255, 255, 255))
        position = ((target_width - new_width) // 2, (target_height - new_height) // 2)
        final_image.paste(resized_image, position)
        final_image.save(output_path, "JPEG")
    except Exception as e:
        print(f"Error processing {pdf_path}: {e}")

def process_folder(input_folder, output_folder):
    if not os.path.exists(input_folder):
        print(f"Input folder '{input_folder}' does not exist.")
        return

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for file_name in os.listdir(input_folder):
        if file_name.lower().endswith('.pdf'):
            pdf_path = os.path.join(input_folder, file_name)
            output_path = os.path.join(output_folder, file_name.replace('.pdf', '.jpg'))
            print(f"Processing {pdf_path} -> {output_path}")
            pdf_to_image(pdf_path, output_path)
            print(f"Processed {pdf_path} -> {output_path}")

if __name__ == "__main__":
    input_folder = os.path.join(os.path.dirname(__file__), "..", "entrada")
    output_folder = os.path.join(os.path.dirname(__file__), "..", "salida")

    print(f"Input folder: {input_folder}")
    print(f"Output folder: {output_folder}")

    process_folder(input_folder, output_folder)
    print("Conversion complete!")
