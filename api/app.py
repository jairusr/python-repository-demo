from flask import Flask, request, jsonify, Blueprint, session
from flask_session import Session
from flasgger import Swagger, swag_from
from service import InvoiceService
from xero import XeroClient, InvoiceManager
from .routes.invoice_controller import create_invoice_controller
from dotenv import load_dotenv

load_dotenv()  # Ensure environment variables are loaded

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Replace with a strong secret key

# Initialize the Xero client
xero_client = XeroClient(app)
invoice_manager = InvoiceManager(xero_client)

# Initialize services with the Xero client
invoice_service = InvoiceService(invoice_manager)

# Register the invoice controller
invoice_blueprint = create_invoice_controller(invoice_service)
app.register_blueprint(invoice_blueprint)

swagger = Swagger(app)