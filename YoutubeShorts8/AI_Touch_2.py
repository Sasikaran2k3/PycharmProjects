from transformers import GPT2LMHeadModel, GPT2Tokenizer
import logging

# Configure logging to write to a file
logging.basicConfig(filename='output.log', level=logging.INFO)

# Your script code here

# Log messages
logging.info('Your message here')

# Load pre-trained model and tokenizer
model = GPT2LMHeadModel.from_pretrained("gpt2")
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

# Example input text
input_text = "what is ssh?"

# Tokenize input text
input_ids = tokenizer.encode(input_text, return_tensors="pt")

# Generate output
output = model.generate(input_ids, max_length=100, num_return_sequences=1, no_repeat_ngram_size=2)

# Decode and print the generated text
generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
print(generated_text)
