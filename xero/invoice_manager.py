import os

from xero_python.accounting import AccountingApi

class InvoiceManager:
    """Manages invoice operations using Xero API."""
    def __init__(self, xero_client):
        self.xero_client = xero_client
        self.xero_tenant = os.getenv('Tenant')
        

    def get_api_instance(self):
        api_client = self.xero_client.get_api_instance()
        return AccountingApi(api_client)

    def get_invoice_by_guid(self, invoice_guid):
        api_instance = self.get_api_instance()
        try:
            invoice = api_instance.get_invoice(self.xero_tenant, invoice_guid)
            return invoice
        except Exception as e:
            print(f"Error retrieving invoice: {str(e)}")
            return None

    def get_invoices(self):
        api_instance = self.get_api_instance()
        try:
            invoices = api_instance.get_invoices()
            return invoices
        except Exception as e:
            print(f"Error retrieving invoices: {str(e)}")
            return None