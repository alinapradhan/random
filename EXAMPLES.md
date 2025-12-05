# Text Generation Chatbot - Example Usage

This file shows example interactions with the text generation chatbot.

## Starting the Chatbot

```bash
$ python chatbot.py
Loading gpt2 model... This may take a moment.
gpt2 model loaded successfully!

============================================================
Text Generation Chatbot (GPT-2)
============================================================
Type your message and press Enter to get a response.
Commands:
  - 'quit' or 'exit' to end the conversation
  - 'clear' to clear the conversation history
============================================================
```

## Example Conversation 1: Casual Chat

```
You: Hello! How are you today?
Chatbot: Hello! I'm doing well, thank you for asking. I'm here to help you with any questions or conversations you'd like to have.

You: What can you tell me about artificial intelligence?
Chatbot: Artificial intelligence is a fascinating field that involves creating computer systems capable of performing tasks that typically require human intelligence. These include learning, reasoning, problem-solving, and understanding natural language.

You: That's interesting. Can you write a short poem?
Chatbot: Of course! Here's a short poem:
    
    The stars shine bright in the night,
    Dancing across the sky so light,
    Whispers of dreams take flight,
    Until the morning brings new light.

You: quit
Chatbot: Goodbye! Have a great day!
```

## Example Conversation 2: Information Request

```
You: Tell me a fun fact about space.
Chatbot: Did you know that a day on Venus is longer than a year on Venus? It takes Venus about 243 Earth days to complete one rotation, but only 225 Earth days to orbit the Sun!

You: That's amazing! Tell me another one.
Chatbot: Here's another interesting fact: If you could fold a piece of paper 42 times, it would reach the Moon! Each fold doubles the thickness exponentially.

You: exit
Chatbot: Goodbye! Have a great day!
```

## Example Conversation 3: Creative Writing

```
You: Can you start a short story about a robot?
Chatbot: Once upon a time, in a bustling city of neon lights and flying cars, there lived a small robot named Chip. Unlike the other robots who worked in factories, Chip had a unique gift - he could paint beautiful landscapes that captured the hearts of everyone who saw them.

You: Continue the story
Chatbot: One day, Chip discovered an old, abandoned garden hidden between two skyscrapers. The garden was filled with wilted flowers and overgrown vines, but Chip saw its potential. He decided to restore the garden and paint its transformation, hoping to bring beauty back to the concrete jungle.

You: clear

Conversation history cleared.

You: exit
Chatbot: Goodbye! Have a great day!
```

## Customizing the Model

You can use different GPT-2 model sizes by editing `chatbot.py`:

```python
# In the main() function:
chatbot = TextGenerationChatbot(model_name="gpt2")        # Smallest (124M params)
# OR
chatbot = TextGenerationChatbot(model_name="gpt2-medium")  # Medium (355M params)
# OR
chatbot = TextGenerationChatbot(model_name="gpt2-large")   # Large (774M params)
# OR
chatbot = TextGenerationChatbot(model_name="gpt2-xl")      # Extra Large (1.5B params)
```

Larger models provide better quality responses but require more memory and are slower.

## Features Demonstrated

1. **Natural Conversation**: The chatbot maintains context and provides coherent responses
2. **Multiple Topics**: Can discuss various subjects from science to creative writing
3. **Commands**: Supports `quit`, `exit`, and `clear` commands
4. **Context Management**: Keeps track of conversation history for better responses
5. **Flexible Generation**: Uses temperature, top-k, and top-p sampling for varied outputs

## Note

The actual responses from GPT-2 will vary based on the prompt and the model's training data. The examples above are representative of the types of conversations possible with the chatbot.
