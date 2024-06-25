class InvoiceService:
    def __init__(self, invoice_manager):
        self.invoice_manager = invoice_manager

    def get_invoice_by_id(self, invoice_id):
        return self.invoice_manager.get_invoice_by_guid(invoice_id)