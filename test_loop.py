#!/usr/bin/env python3
"""
Test script to loop through sample prompts and generate descriptions.
This demonstrates the product description generator with multiple examples.
"""

import requests
import time
import json

# Sample prompts to test
SAMPLE_PROMPTS = [
    {'product_name': 'EcoBottle', 'category': 'reusable water bottle'},
    {'product_name': 'SmartDesk', 'category': 'standing desk'},
    {'product_name': 'CloudRunner', 'category': 'running shoes'},
    {'product_name': 'FreshBrew', 'category': 'coffee maker'},
    {'product_name': 'ZenPad', 'category': 'meditation app'},
]

def test_generator(base_url='http://localhost:5000'):
    """Test the product description generator with sample prompts"""
    print("=" * 80)
    print("Product Description Generator Test")
    print("=" * 80)
    print()
    
    for i, sample in enumerate(SAMPLE_PROMPTS, 1):
        print(f"\n[{i}/{len(SAMPLE_PROMPTS)}] Testing: {sample['product_name']} ({sample['category']})")
        print("-" * 80)
        
        try:
            response = requests.post(
                f'{base_url}/generate',
                json=sample,
                headers={'Content-Type': 'application/json'},
                timeout=30
            )
            
            if response.status_code == 200:
                result = response.json()
                print(f"✅ Success!")
                print(f"Product: {result['product_name']}")
                print(f"Category: {result['category']}")
                print(f"Description: {result['description']}")
            else:
                print(f"❌ Error: {response.status_code}")
                print(f"Response: {response.text}")
        
        except requests.exceptions.ConnectionError:
            print("❌ Connection Error: Make sure the Flask server is running!")
            print("   Start it with: python app.py")
            break
        except Exception as e:
            print(f"❌ Exception: {str(e)}")
        
        # Small delay between requests
        if i < len(SAMPLE_PROMPTS):
            time.sleep(1)
    
    print("\n" + "=" * 80)
    print("Test completed!")
    print("=" * 80)

if __name__ == '__main__':
    print("Starting test loop for product description generator...")
    print("Make sure the Flask app is running (python app.py)\n")
    time.sleep(2)
    test_generator()