import fitz  # PyMuPDF

# Open the PDF file
pdf_document = 'sample-1.pdf'
pdf = fitz.open(pdf_document)

for page_num in range(len(pdf)):
    page = pdf.load_page(page_num)
    
    # Extract text
    text = page.get_text("text")
    print(f"Text on page {page_num + 1}:")
    print(text)
    
    # Extract images
    images = page.get_images(full=True)
    print(f"Images on page {page_num + 1}:")
    for img in images:
        print(img)
