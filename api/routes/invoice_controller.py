from flask import Blueprint, request, jsonify
from service import InvoiceService
from flasgger import swag_from
from xero import jsonify, serialize_model

# Assuming invoice_service is passed as a dependency for simplicity
def create_invoice_controller(invoice_service):
    invoice_blueprint = Blueprint('invoice', __name__)

    @invoice_blueprint.route('/invoices/<invoice_id>', methods=['GET'])
    @swag_from('invoice_get.yml')
    def get_invoice(invoice_id):
        invoice = invoice_service.get_invoice_by_id(invoice_id)
        if invoice:
            return serialize_model(invoice), 200
        else:
            return jsonify({'error': 'Invoice not found'}), 404

    return invoice_blueprint
