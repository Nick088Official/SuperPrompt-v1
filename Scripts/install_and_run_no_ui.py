import os
import subprocess
import random
import time
import transformers
from transformers import T5Tokenizer, T5ForConditionalGeneration
import torch
import random
import argparse

if torch.cuda.is_available():
    device = "cuda"
    print("Using GPU")
else:
    device = "cpu"
    print("Using CPU")


# Load the tokenizer and model to device
tokenizer = T5Tokenizer.from_pretrained("roborovski/superprompt-v1")
model = T5ForConditionalGeneration.from_pretrained("roborovski/superprompt-v1", device_map="auto", torch_dtype="auto")
model.to(device)

print(f"Loaded model succesfully in auto precision on {'GPU' if device == 'cuda' else 'CPU'}! Loading inference...")


def main(your_prompt, task_prefix, max_new_tokens, repetition_penalty, temperature, model_precision_type, top_p, top_k, seed):
    if seed == 0:
        seed = random.randint(1, 2**32-1)
    transformers.set_seed(seed)
    
    if model_precision_type == "fp16":
        dtype = torch.float16
    elif model_precision_type == "fp32":
        dtype = torch.float32

    model.to(dtype)

    repetition_penalty = float(repetition_penalty)
    
    input_text = f"{task_prefix}: {your_prompt}"
    input_ids = tokenizer(input_text, return_tensors="pt").input_ids.to(device)
        
    outputs = model.generate(
        input_ids,
        max_new_tokens=max_new_tokens,
        repetition_penalty=repetition_penalty,
        do_sample=True,
        temperature=temperature,
        top_p=top_p,
        top_k=top_k,
    )
        
    better_prompt = tokenizer.decode(outputs[0], skip_special_tokens=True)
    print(f"Generated Better Prompt: {better_prompt}")

if __name__ == "__main__":

    # Create an ArgumentParser object
    parser = argparse.ArgumentParser()

    # Add arguments for each input value
    parser.add_argument("your_prompt", type=str, help="Your Prompt that you wanna make better")
    parser.add_argument("task_prefix", type=str, help="The prompt prefix for how the AI should make yours better")
    parser.add_argument("max_new_tokens", type=float, help="Maximum number of the tokens to generate")
    parser.add_argument("repetition_penalty", type=float, help="The higher the less the AI repeats itself")
    parser.add_argument("temperature", type=float, help="Higher values produce more diverse outputs")
    parser.add_argument('model_precision_type', type=str, help='The precision type to load the model, like fp16 which is faster, or fp32 which gives better results')
    parser.add_argument("top_p", type=float, help="Higher values sample more low-probability tokens")
    parser.add_argument("top_k", type=int, help="Higher k means more diverse outputs by considering a range of tokens")
    parser.add_argument("seed", type=int, help="Seed for the generation process")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Get task prefix
    task_prefix = args.task_prefix

    # Get user prompt
    your_prompt = args.your_prompt

    # Get max new tokens
    max_new_tokens = args.max_new_tokens

    # Get repetition penalty
    repetition_penalty = args.repetition_penalty

    # Get Temperature
    temperature = args.temperature

    # Get top_p
    top_p = args.top_p

    # Get top_k
    top_k = args.top_k

    # Get precision model type
    model_precision_type = args.model_precision_type

    # Get seed
    seed = args.seed


    main(your_prompt, task_prefix, max_new_tokens, repetition_penalty, temperature, model_precision_type, top_p, top_k, seed)
