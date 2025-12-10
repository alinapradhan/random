"""
Product Description Generator
A simple web application that generates marketing blurbs for products using LLM.
"""

from typing import Tuple, Dict, Any
from flask import Flask, render_template, request, jsonify, Response
from transformers import pipeline
import html

app = Flask(__name__)

# Security: Add response headers for protection
@app.after_request
def add_security_headers(response: Response) -> Response:
    """Add security headers to all responses"""
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    response.headers['Content-Security-Policy'] = "default-src 'self' 'unsafe-inline'"
    return response

# Generation parameters
MAX_LENGTH = 50
TEMPERATURE = 0.7

# Initialize the text generation pipeline with a smaller model
generator = None

def get_generator() -> pipeline:
    """Lazy load the text generator"""
    global generator
    if generator is None:
        # Using a lightweight model for quick responses
        generator = pipeline('text-generation', model='distilgpt2')
    return generator

@app.route('/')
def index() -> str:
    """Render the main form page"""
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_description() -> Tuple[Response, int]:
    """Generate product description based on product name and category"""
    try:
        data = request.get_json()
        product_name = data.get('product_name', '').strip()
        category = data.get('category', '').strip()
        
        if not product_name or not category:
            return jsonify({'error': 'Product name and category are required'}), 400
        
        # Security: Validate input length to prevent abuse
        if len(product_name) > 100 or len(category) > 100:
            return jsonify({'error': 'Input too long. Maximum 100 characters allowed.'}), 400
        
        # Security: Sanitize inputs to prevent XSS
        product_name = html.escape(product_name)
        category = html.escape(category)
        
        # Create a prompt for generating marketing copy
        prompt = f"Write a compelling one-line marketing description for {product_name}, a {category} product: "
        
        # Generate the description
        gen = get_generator()
        result = gen(prompt, max_length=MAX_LENGTH, num_return_sequences=1, temperature=TEMPERATURE)
        
        # Extract the generated text and clean it up
        generated_text = result[0]['generated_text']
        # Remove the prompt from the response
        description = generated_text.replace(prompt, '').strip()
        
        # If the description is too long, truncate at first sentence
        if '.' in description:
            description = description.split('.')[0] + '.'
        
        return jsonify({
            'product_name': product_name,
            'category': category,
            'description': description
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/samples', methods=['GET'])
def get_samples() -> Response:
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
    debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() in ('true', '1', 't')
    app.run(debug=debug_mode, host='0.0.0.0', port=5000)
