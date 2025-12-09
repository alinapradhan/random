# Product Description Generator 🚀

A simple web application that generates compelling one-line marketing blurbs for products using AI/LLM technology.

## Features

- 📝 **Form Interface**: Easy-to-use web form for entering product name and category
- 🤖 **AI-Powered**: Uses Hugging Face transformers (DistilGPT2) for text generation
- 🎯 **Sample Prompts**: Pre-loaded sample products to test quickly
- 💫 **Beautiful UI**: Modern, responsive design with gradient styling
- ⚡ **Fast**: Lightweight model for quick response times

## Installation

1. Clone the repository:
```bash
git clone https://github.com/alinapradhan/random.git
cd random
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the Flask application:
```bash
python app.py
```

2. Open your browser and navigate to:
```
http://localhost:5000
```

3. Enter a product name and category, then click "Generate Description"

4. Or try one of the sample prompts by clicking on them

## Sample Prompts

- **EcoBottle** (reusable water bottle)
- **SmartDesk** (standing desk)
- **CloudRunner** (running shoes)
- **FreshBrew** (coffee maker)
- **ZenPad** (meditation app)

## Technology Stack

- **Backend**: Flask (Python web framework)
- **AI/ML**: Hugging Face Transformers with DistilGPT2 model
- **Frontend**: HTML5, CSS3, JavaScript (vanilla)
- **Styling**: Custom CSS with gradient design

## API Endpoints

### `GET /`
Returns the main web interface

### `POST /generate`
Generates a product description
- **Body**: `{"product_name": "string", "category": "string"}`
- **Response**: `{"product_name": "string", "category": "string", "description": "string"}`

### `GET /samples`
Returns sample product prompts for testing
- **Response**: Array of sample products

## License

MIT
  
