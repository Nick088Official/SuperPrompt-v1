import os
import time
from transformers import T5Tokenizer, T5ForConditionalGeneration
import torch
import gradio as gr
import random
import argparse


if torch.cuda.is_available():
    device = "cuda"
    print("Using GPU")
else:
    device = "cpu"
    print("Using CPU")

# Load the tokenizer and model
tokenizer = T5Tokenizer.from_pretrained("google/flan-t5-small")
model = T5ForConditionalGeneration.from_pretrained("roborovski/superprompt-v1", device_map="auto", torch_dtype="auto")

model.to(device)

print(f"Loaded model succesfully in auto precision type on {'GPU' if device == 'cuda' else 'CPU'}! Loading inference...")


# run ui
def generate(your_prompt, max_new_tokens, repetition_penalty, temperature, top_p, top_k, seed):
    
    input_text = f"Expand the following prompt to add more detail: {your_prompt}"
    input_ids = tokenizer(input_text, return_tensors="pt").input_ids.to(device)

    if seed == 0:
        seed = random.randint(1, 100000)
        torch.manual_seed(seed)
    else:
        torch.manual_seed(seed)
        
    outputs = model.generate(
        input_ids,
        max_new_tokens=max_new_tokens,
        repetition_penalty=repetition_penalty,
        do_sample=True,
        temperature=temperature,
        top_p=top_p,
        top_k=top_k,
    )

    better_prompt = tokenizer.decode(outputs[0])
    better_prompt = better_prompt.replace("<pad>", "").replace("</s>", "")
    return better_prompt


your_prompt = gr.Textbox(label="Your Prompt", interactive=True)

max_new_tokens = gr.Slider(value=512, minimum=250, maximum=512, step=1, interactive=True, label="Max New Tokens", info="The maximum numbers of new tokens, controls how long is the output")
    
repetition_penalty = gr.Slider(value=1.2, minimum=0, maximum=2, step=0.05, interactive=True, label="Repetition Penalty", info="Penalize repeated tokens, making the AI repeat less itself")
    
temperature = gr.Slider(value=0.5, minimum=0, maximum=1, step=0.05, interactive=True, label="Temperature", info="Higher values produce more diverse outputs")

top_p = gr.Slider(value=1, minimum=0, maximum=2, step=0.05, interactive=True, label="Top P", info="Higher values sample more low-probability tokens")

top_k = gr.Slider(value=1, minimum=1, maximum=100, step=1, interactive=True, label="Top K", info="Higher k means more diverse outputs by considering a range of tokens")

seed = gr.Number(value=42, interactive=True, label="Seed", info="A starting point to initiate the generation process, put 0 for a random one")

examples = [
    ["A storefront with 'Text to Image' written on it.", 512, 1.2, 0.5, 1, 50, 42]
]

gr.Interface(
    fn=generate,
    inputs=[your_prompt, max_new_tokens, repetition_penalty, temperature, top_p, top_k, seed],
    outputs=gr.Textbox(label="Better Prompt"),
    title="SuperPrompt-v1",
    description='Make your prompts more detailed! <br> <a href="https://huggingface.co/roborovski/superprompt-v1">Model used</a> <br> <a href="https://brianfitzgerald.xyz/prompt-augmentation/">Model Blog</a> <br> Task Prefix: "Expand the following prompt to add more detail:" is already setted! <br> Ports made by [Nick088](https://linktr.ee/Nick088)',
    examples=examples,
).launch(show_api=False, share=False)
