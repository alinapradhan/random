"""
Simplified Product Description Generator for Testing
Uses mock generation instead of downloading large models
"""

from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Mock descriptions for quick testing
TEMPLATES = [
    "Revolutionize your daily routine with {product}, the ultimate {category} that delivers unmatched quality and style.",
    "Experience the future of {category} with {product}, designed for those who demand excellence.",
    "Transform the way you think about {category} with {product}, where innovation meets perfection.",
    "{product} is not just a {category}, it's a lifestyle choice for the modern world.",
    "Discover {product}, the {category} that combines cutting-edge technology with timeless design.",
    "Elevate your experience with {product}, the premium {category} you've been waiting for.",
    "{product} redefines what a {category} can be, bringing you power, elegance, and efficiency.",
    "Meet {product}, the {category} that seamlessly blends functionality with sophistication.",
]

def generate_mock_description(product_name, category):
    """Generate a mock description using templates"""
    template = random.choice(TEMPLATES)
    description = template.format(product=product_name, category=category)
    return description

@app.route('/')
def index():
    """Render the main form page"""
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_description():
    """Generate product description based on product name and category"""
    try:
        data = request.get_json()
        product_name = data.get('product_name', '').strip()
        category = data.get('category', '').strip()
        
        if not product_name or not category:
            return jsonify({'error': 'Product name and category are required'}), 400
        
        # Generate the description using mock generator
        description = generate_mock_description(product_name, category)
        
        return jsonify({
            'product_name': product_name,
            'category': category,
            'description': description
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/samples', methods=['GET'])
def get_samples():
    """Return sample prompts for testing"""
    samples = [
        {'product_name': 'EcoBottle', 'category': 'reusable water bottle'},
        {'product_name': 'SmartDesk', 'category': 'standing desk'},
        {'product_name': 'CloudRunner', 'category': 'running shoes'},
        {'product_name': 'FreshBrew', 'category': 'coffee maker'},
        {'product_name': 'ZenPad', 'category': 'meditation app'}
    ]
    return jsonify(samples)

if __name__ == '__main__':
    # Debug mode should only be used in development
    # Set FLASK_DEBUG=0 or False in production
    import os
    debug_mode = os.environ.get('FLASK_DEBUG', 'True').lower() in ('true', '1', 't')
    app.run(debug=debug_mode, host='0.0.0.0', port=5000)