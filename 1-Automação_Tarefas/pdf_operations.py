import os
from PyPDF2 import PdfReader, PdfWriter, PdfMerger
from PIL import Image

def get_pdf_metadata(pdf_path):
    """Retorna os metadados de um arquivo PDF."""
    with open(pdf_path, "rb") as f:
        reader = PdfReader(f)
        return reader.metadata

def extract_text_from_pdf(pdf_path):
    """Extrai todo o texto de um arquivo PDF."""
    with open(pdf_path, 'rb') as f:
        reader = PdfReader(f)
        results = [reader.pages[i].extract_text() for i in range(len(reader.pages))]
    return ' '.join(results)

def split_pdf(pdf_path):
    """Divide um PDF em várias páginas individuais."""
    with open(pdf_path, 'rb') as f:
        reader = PdfReader(f)
        for page_num in range(len(reader.pages)):
            writer = PdfWriter()
            writer.add_page(reader.pages[page_num])
            filename = os.path.split(pdf_path)[1]
            new_filename = f'files/{filename}_{page_num + 1}.pdf'
            with open(new_filename, 'wb') as out:
                writer.write(out)

def fetch_all_pdf_files(parent_folder: str):
    """Busca e retorna todos os arquivos PDF em um diretório."""
    target_files = []
    for path, subdirs, files in os.walk(parent_folder):
        for name in files:
            if name.endswith(".pdf"):
                target_files.append(os.path.join(path, name))
    return target_files

def merge_pdf(list_pdfs, output_filename="files/final_pdf.pdf"):
    """Mescla uma lista de PDFs em um único arquivo PDF."""
    merger = PdfMerger()
    for file in list_pdfs:
        merger.append(file)
    with open(output_filename, "wb") as f:
        merger.write(f)

def rotate_pdf(pdf_path, page_num: int, rotation: int = 90):
    """Rotaciona uma página específica de um PDF."""
    with open(pdf_path, "rb") as f:
        reader = PdfReader(f)
        writer = PdfWriter()
        writer.add_page(reader.pages[page_num])
        writer.pages[page_num].rotate(rotation)
        filename = os.path.split(pdf_path)[1]
        output_filename = f"files/{filename}_{rotation}_rotated_page.pdf"
        with open(output_filename, "wb") as out:
            writer.write(out)

def extract_images_from_pdf(pdf_path):
    """Extrai todas as imagens de um arquivo PDF."""
    with open(pdf_path, "rb") as f:
        reader = PdfReader(f)
        for page_num in range(len(reader.pages)):
            selected_page = reader.pages[page_num]
            for img_file_obj in selected_page.images:
                with open(f"files/{img_file_obj.name}", "wb") as out:
                    out.write(img_file_obj.data)

def convert_img_pdf(image_file):
    """Converte uma imagem em um arquivo PDF."""
    my_image = Image.open(image_file)
    img = my_image.convert("RGB")
    filename = f"{os.path.splitext(image_file)[0]}.pdf"
    img.save(filename)

if __name__ == "__main__":
    # Exemplo de uso das funções
    rotate_pdf("files/arte_da_guerra.pdf", 0)
    extract_images_from_pdf("files/test_pdf_image.pdf")
    convert_img_pdf("files/Image96.jpg")
    # print(get_pdf_metadata('files/arte_da_guerra.pdf'))
    # print(extract_text_from_pdf('files/arte_da_guerra.pdf'))
    # pdf_list = fetch_all_pdf_files("files/")
    # merge_pdf(pdf_list)
    # split_pdf('files/arte_da_guerra.pdf')