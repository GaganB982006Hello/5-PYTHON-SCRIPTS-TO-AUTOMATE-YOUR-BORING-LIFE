import os
from PyPDF2 import PdfMerger # Note: 'PyPDF2' is the classic lib; 'pypdf' is the modern version

def merge_pdfs():
    merger = PdfMerger()
    
    # List of PDFs to merge (in order)
    pdf_files = ["Contract_P1.pdf", "Contract_P2.pdf", "Contract_P3.pdf"]
    
    for pdf in pdf_files:
        if os.path.exists(pdf):
            print(f"Adding {pdf}...")
            merger.append(pdf)
        else:
            print(f"File not found: {pdf}")

    # Write the merged file
    merger.write("Full_Contract_Merged.pdf")
    merger.close()
    print("PDFs merged successfully!")

if __name__ == "__main__":
    merge_pdfs()
