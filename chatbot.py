#!/usr/bin/env python3
"""
Text Generation Chatbot using GPT-2

A simple chatbot that generates responses using a pre-trained GPT-2 model
from the Hugging Face transformers library.
"""

import sys
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch


class TextGenerationChatbot:
    """A chatbot powered by GPT-2 for text generation."""
    
    def __init__(self, model_name="gpt2"):
        """
        Initialize the chatbot with a pre-trained model.
        
        Args:
            model_name (str): Name of the pre-trained model to use.
                            Default is "gpt2" (smallest GPT-2 model).
        """
        print(f"Loading {model_name} model... This may take a moment.")
        self.tokenizer = GPT2Tokenizer.from_pretrained(model_name)
        self.model = GPT2LMHeadModel.from_pretrained(model_name)
        
        # Set pad token if not set
        if self.tokenizer.pad_token is None:
            self.tokenizer.pad_token = self.tokenizer.eos_token
        
        self.model.eval()
        print(f"{model_name} model loaded successfully!\n")
    
    def generate_response(self, prompt, max_length=100, temperature=0.7, 
                         num_return_sequences=1, top_k=50, top_p=0.95):
        """
        Generate a response based on the input prompt.
        
        Args:
            prompt (str): The input text to generate a response for.
            max_length (int): Maximum length of generated text.
            temperature (float): Sampling temperature (higher = more random).
            num_return_sequences (int): Number of responses to generate.
            top_k (int): Top-k sampling parameter.
            top_p (float): Top-p (nucleus) sampling parameter.
        
        Returns:
            str: The generated response.
        """
        # Encode the input prompt
        input_ids = self.tokenizer.encode(prompt, return_tensors="pt")
        
        # Generate response
        with torch.no_grad():
            output = self.model.generate(
                input_ids,
                max_length=max_length,
                temperature=temperature,
                num_return_sequences=num_return_sequences,
                top_k=top_k,
                top_p=top_p,
                pad_token_id=self.tokenizer.pad_token_id,
                do_sample=True,
                no_repeat_ngram_size=2,
            )
        
        # Decode and return the generated text
        generated_text = self.tokenizer.decode(output[0], skip_special_tokens=True)
        return generated_text
    
    def chat(self):
        """Run an interactive chat session."""
        print("=" * 60)
        print("Text Generation Chatbot (GPT-2)")
        print("=" * 60)
        print("Type your message and press Enter to get a response.")
        print("Commands:")
        print("  - 'quit' or 'exit' to end the conversation")
        print("  - 'clear' to clear the conversation history")
        print("=" * 60)
        print()
        
        conversation_history = ""
        
        while True:
            try:
                # Get user input
                user_input = input("You: ").strip()
                
                if not user_input:
                    continue
                
                # Check for exit commands
                if user_input.lower() in ['quit', 'exit', 'bye']:
                    print("\nChatbot: Goodbye! Have a great day!")
                    break
                
                # Check for clear command
                if user_input.lower() == 'clear':
                    conversation_history = ""
                    print("\nConversation history cleared.\n")
                    continue
                
                # Build prompt with conversation history
                if conversation_history:
                    prompt = f"{conversation_history}\nYou: {user_input}\nChatbot:"
                else:
                    prompt = f"You: {user_input}\nChatbot:"
                
                # Generate response
                print("Chatbot: ", end="", flush=True)
                response = self.generate_response(prompt, max_length=len(prompt.split()) + 50)
                
                # Extract just the chatbot's response
                if "Chatbot:" in response:
                    response_parts = response.split("Chatbot:")
                    if len(response_parts) > 1:
                        bot_response = response_parts[-1].split("You:")[0].strip()
                    else:
                        bot_response = response_parts[0].strip()
                else:
                    bot_response = response[len(prompt):].split("You:")[0].strip()
                
                print(bot_response)
                print()
                
                # Update conversation history (keep last few exchanges)
                conversation_history += f"\nYou: {user_input}\nChatbot: {bot_response}"
                # Keep only the last 200 words to avoid context length issues
                words = conversation_history.split()
                if len(words) > 200:
                    conversation_history = " ".join(words[-200:])
                
            except KeyboardInterrupt:
                print("\n\nChatbot: Goodbye! Have a great day!")
                break
            except Exception as e:
                print(f"\nError: {e}")
                print("Please try again.\n")


def main():
    """Main entry point for the chatbot."""
    # You can change the model here to use different GPT-2 variants:
    # "gpt2" (124M parameters - fastest)
    # "gpt2-medium" (355M parameters)
    # "gpt2-large" (774M parameters)
    # "gpt2-xl" (1.5B parameters - slowest)
    
    chatbot = TextGenerationChatbot(model_name="gpt2")
    chatbot.chat()


if __name__ == "__main__":
    main()
