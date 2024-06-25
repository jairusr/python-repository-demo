import tkinter as tk
from tkinter import messagebox
import requests

class InvoiceGUI:
    def __init__(self, master):
        self.master = master
        master.title("Invoice Retrieval")

        self.label = tk.Label(master, text="Enter Invoice ID:")
        self.label.pack()

        self.invoice_id_entry = tk.Entry(master)
        self.invoice_id_entry.pack()

        self.get_invoice_button = tk.Button(master, text="Get Invoice", command=self.get_invoice)
        self.get_invoice_button.pack()

        self.result_text = tk.Text(master, height=10, width=50)
        self.result_text.pack()

    def get_invoice(self):
        invoice_id = self.invoice_id_entry.get()
        if invoice_id:
            try:
                response = requests.get(f'https://127.0.0.1:5000/invoices/{invoice_id}', verify=False)
                if response.status_code == 200:
                    self.result_text.delete(1.0, tk.END)
                    self.result_text.insert(tk.END, response.text)
                else:
                    messagebox.showerror("Error", f"Failed to retrieve invoice: {response.json()['error']}")
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showinfo("Info", "Please enter an invoice ID")

def main():
    root = tk.Tk()
    gui = InvoiceGUI(root)
    root.mainloop()

if __name__ == '__main__':
    main()
