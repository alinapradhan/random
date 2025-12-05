# Text Generation Chatbot

A simple chatbot that generates responses using a pre-trained GPT-2 language model from Hugging Face's transformers library.

## Features

- Uses GPT-2, a powerful pre-trained language model
- Interactive command-line interface
- Maintains conversation context
- No API keys required - runs locally
- Easy to use and extend

## Requirements

- Python 3.7 or higher
- PyTorch
- Transformers library

## Installation

1. Clone this repository:
```bash
git clone https://github.com/alinapradhan/random.git
cd random
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

Note: The first time you run the chatbot, it will download the GPT-2 model (~500MB). This is a one-time download.

## Usage

Run the chatbot:
```bash
python chatbot.py
```

### Commands

- Type your message and press Enter to get a response
- Type `quit`, `exit`, or `bye` to end the conversation
- Type `clear` to clear the conversation history
- Press `Ctrl+C` to exit at any time

### Example Conversation

```
You: Hello! How are you today?
Chatbot: I'm doing great! Thanks for asking. How can I help you?

You: Tell me a fun fact about space.
Chatbot: Did you know that a day on Venus is longer than a year on Venus?
```

## Customization

You can customize the chatbot by modifying the model in `chatbot.py`:

- `gpt2` (124M parameters) - Default, fastest
- `gpt2-medium` (355M parameters) - Better quality
- `gpt2-large` (774M parameters) - Higher quality
- `gpt2-xl` (1.5B parameters) - Best quality, slowest

Change the model in the `main()` function:
```python
chatbot = TextGenerationChatbot(model_name="gpt2-medium")
```

## How It Works

The chatbot uses the GPT-2 model, which is a transformer-based language model trained on a large corpus of text. It generates responses by:

1. Taking your input prompt
2. Using the model to predict the most likely next tokens
3. Generating a coherent response based on the conversation context

## License

See LICENSE file for details.

## Contributing

Feel free to open issues or submit pull requests for improvements!
