# app/routes.py
from flask import Blueprint, request, jsonify
from app.database import db, Inventory

inventory_bp = Blueprint('inventory_bp', __name__)

# Endpoint to get all inventory items
@inventory_bp.route('/inventory', methods=['GET'])
def get_inventory():
    items = Inventory.query.all()
    result = [
        {"id": item.id, "product": item.product_name, "stock": item.stock_level}
        for item in items
    ]
    return jsonify(result), 200

# Endpoint to update inventory for a particular product

