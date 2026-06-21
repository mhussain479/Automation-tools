import pdfplumber
import re
import os

folder = "invoices"
output_file = "all_invoices.csv"

with open(output_file, "w") as f:
    f.write("Invoice Number,Invoice Date,Due Date,Total Due,Order Number\n")
    

    for filename in os.listdir(folder):
        if filename.endswith(".pdf"):
            filepath = os.path.join(folder, filename)

            invoice_number = invoice_date = due_date = total_due = order_number = "Error"
            try:
                with pdfplumber.open(filepath) as pdf:
                    page = pdf.pages[0]
                    text = page.extract_text()
                    if not text:
                        raise ValueError("No text found — possibly scanned image")
                    for words in text.split("\n"):
                        match = re.search(r"[A-Z]{2,}-\d{3,}", words)
                        if match:
                            invoice_number = match.group(0)
                            print(f"Invoice Number: {invoice_number}")
                            
                        inv_date_match = re.search(r"Invoice Date.*?([A-Z][a-z]+ \d{1,2}, \d{4})", words)    
                        if inv_date_match:
                            invoice_date = inv_date_match.group(1)
                            print(f"Invoice Date: {invoice_date}")

                        due_match = re.search(r"Due Date.*?([A-Z][a-z]+ \d{1,2}, \d{4})", words)
                        if due_match:
                            due_date = due_match.group(1)
                            print(f"Due Date: {due_date}")
                        
                        total_match = re.search(r"(?:Total\s*Due|Total\s*Amount|Total\s*:)\s*\$?([\d,]+\.\d{2})", words)
                        if total_match:
                            total_due = total_match.group(1)
                            print(f"Total due: {total_due}")

                        order_match = re.search(r"(?:Order|PO)\s*(?:Number|#|No|:)?\s*:?\s*([A-Za-z0-9-]+)", words)
                        if order_match:
                            order_number = order_match.group(1)
                            print(f"Order Number: {order_number}")
            except FileNotFoundError:
                print("File not found.")
            except Exception as e:
                print(f"Error processing PDF: {e}")

            f.write(f'"{invoice_number}","{invoice_date}","{due_date}","{total_due}","{order_number}"\n')
        
