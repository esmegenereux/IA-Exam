from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers.generation import GenerationConfig
import torch

# Initialize the model and tokenizer
model_path = "qwen-vl-chat"
tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    model_path,
    device_map="auto",
    trust_remote_code=True
).eval()

# Set generation config
model.generation_config = GenerationConfig.from_pretrained(model_path, trust_remote_code=True)

def chat():
    print("Welcome to Qwen-VL-Chat! Type 'quit' to exit.")
    while True:
        # Get user input
        query = input("\nYou: ")
        if query.lower() == 'quit':
            break
            
        # Generate response
        response, history = model.chat(tokenizer, query=query, history=None)
        print(f"\nAssistant: {response}")

if __name__ == "__main__":
    chat()
