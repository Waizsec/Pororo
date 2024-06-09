# import torch
# from transformers import GPT2LMHeadModel, GPT2Tokenizer

# # Load pre-trained GPT-2 model and tokenizer
# model_name = "gpt2"
# tokenizer = GPT2Tokenizer.from_pretrained(model_name)
# model = GPT2LMHeadModel.from_pretrained(model_name)

# # Function to generate interpretation using GPT-2


# def generate_interpretation(input_features, prediction):
#     input_text = f"Input features: {input_features}\nPrediction: {prediction}\nInterpretation:"
#     input_ids = tokenizer.encode(input_text, return_tensors="pt")
#     output = model.generate(input_ids, max_length=100,
#                             num_return_sequences=1, temperature=0.7)
#     generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
#     return generated_text
