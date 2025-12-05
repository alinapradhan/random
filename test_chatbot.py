#!/usr/bin/env python3
"""
Test script to verify the chatbot implementation structure.
This tests the code without loading the actual models (which require large downloads).
"""

import sys
import ast

def test_chatbot_structure():
    """Test that chatbot.py has the correct structure."""
    print("Testing chatbot.py structure...")
    
    with open('chatbot.py', 'r') as f:
        code = f.read()
    
    # Parse the code
    tree = ast.parse(code)
    
    # Check for required elements
    classes = [node.name for node in ast.walk(tree) if isinstance(node, ast.ClassDef)]
    functions = [node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
    
    # Verify class exists
    assert 'TextGenerationChatbot' in classes, "TextGenerationChatbot class not found"
    print("✓ TextGenerationChatbot class found")
    
    # Verify required methods
    required_methods = ['__init__', 'generate_response', 'chat']
    for method in required_methods:
        assert method in functions, f"Method {method} not found"
        print(f"✓ Method {method} found")
    
    # Verify main function
    assert 'main' in functions, "main function not found"
    print("✓ main function found")
    
    # Check imports
    assert 'transformers' in code, "transformers import not found"
    assert 'torch' in code, "torch import not found"
    assert 'GPT2LMHeadModel' in code, "GPT2LMHeadModel not found"
    assert 'GPT2Tokenizer' in code, "GPT2Tokenizer not found"
    print("✓ All required imports found")
    
    # Check for key features
    assert 'temperature' in code, "Temperature parameter not found"
    assert 'max_length' in code, "max_length parameter not found"
    assert 'top_k' in code, "top_k parameter not found"
    assert 'top_p' in code, "top_p parameter not found"
    print("✓ All generation parameters found")
    
    # Check for user interaction
    assert 'input(' in code, "User input not found"
    assert 'quit' in code.lower() or 'exit' in code.lower(), "Exit commands not found"
    print("✓ User interaction features found")
    
    print("\nAll structure tests passed! ✓")
    return True

def test_requirements():
    """Test that requirements.txt is properly formatted."""
    print("\nTesting requirements.txt...")
    
    with open('requirements.txt', 'r') as f:
        lines = f.readlines()
    
    requirements = [line.strip() for line in lines if line.strip() and not line.startswith('#')]
    
    assert 'transformers' in ' '.join(requirements), "transformers not in requirements"
    assert 'torch' in ' '.join(requirements), "torch not in requirements"
    print("✓ All required packages in requirements.txt")
    
    return True

def test_readme():
    """Test that README has proper documentation."""
    print("\nTesting README.md...")
    
    with open('README.md', 'r') as f:
        content = f.read()
    
    # Check for key sections
    assert '# Text Generation Chatbot' in content, "Title not found"
    assert 'Installation' in content, "Installation section not found"
    assert 'Usage' in content, "Usage section not found"
    assert 'python chatbot.py' in content, "Usage command not found"
    assert 'GPT-2' in content or 'gpt2' in content.lower(), "GPT-2 reference not found"
    print("✓ README has all required sections")
    
    return True

if __name__ == "__main__":
    try:
        test_chatbot_structure()
        test_requirements()
        test_readme()
        print("\n" + "="*60)
        print("All tests passed successfully! ✓")
        print("="*60)
        sys.exit(0)
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        sys.exit(1)
