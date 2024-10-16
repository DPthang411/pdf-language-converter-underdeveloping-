import tkinter as tk
import fitz
pdf_document = ""
root = tk.Tk()
root.geometry("800x500")
root.resizable(False, False)
def handle_everything():
    global pdf_document
    inputValue=textBox.get("1.0","end-1c")
    pdf_document = inputValue
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
lable = tk.Label(root, text="Path to your file",font=("Calibri", 40))
textBox=tk.Text(root, height=3, width=60)
convert_button=tk.Button(root, height=1, width=10, text="convert", 
                    command=lambda: handle_everything())
convert_button.place(y = 200, x=380)
textBox.place(y = 100, x=170)
lable.pack()
root.mainloop()