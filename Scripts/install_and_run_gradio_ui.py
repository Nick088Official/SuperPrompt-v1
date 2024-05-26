import os
import transformers
from transformers import T5Tokenizer, T5ForConditionalGeneration
import torch
import gradio as gr
import random

if torch.cuda.is_available():
    device = "cuda"
    print("Using GPU")
else:
    device = "cpu"
    print("Using CPU")

# load model & tokenizer to device
tokenizer = T5Tokenizer.from_pretrained("roborovski/superprompt-v1")
model = T5ForConditionalGeneration.from_pretrained("roborovski/superprompt-v1", torch_dtype=torch.float16)
model.to(device)

# run ui
def generate(your_prompt, task_prefix, max_new_tokens, repetition_penalty, temperature, model_precision_type, top_p, top_k, seed):
    if seed == 0:
        seed = random.randint(1, 2**32-1)
    transformers.set_seed(seed)
    
    if model_precision_type == "fp16":
        dtype = torch.float16
    elif model_precision_type == "fp32":
        dtype = torch.float32
    model.to(dtype)
    
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
    return better_prompt


your_prompt = gr.Textbox(label="Your Prompt", info="Your Prompt that you wanna make better")

task_prefix = gr.Textbox(label="Task Prefix", info="The prompt prefix for how the AI should make yours better",value="Expand the following prompt to add more detail")

max_new_tokens = gr.Slider(value=512, minimum=250, maximum=512, step=1, label="Max New Tokens", info="The maximum numbers of new tokens, controls how long is the output")
    
repetition_penalty = gr.Slider(value=1.2, minimum=0, maximum=2, step=0.05, label="Repetition Penalty", info="Penalize repeated tokens, making the AI repeat less itself")
    
temperature = gr.Slider(value=0.5, minimum=0, maximum=1, step=0.05, label="Temperature", info="Higher values produce more diverse outputs")

model_precision_type = gr.Dropdown(["fp16", "fp32"], value="fp16", label="Model Precision Type", info="The precision type to load the model, like fp16 which is faster, or fp32 which is more precise but more resource consuming")

top_p = gr.Slider(value=1, minimum=0, maximum=2, step=0.05, label="Top P", info="Higher values sample more low-probability tokens")

top_k = gr.Slider(value=50, minimum=1, maximum=100, step=1, label="Top K", info="Higher k means more diverse outputs by considering a range of tokens")

seed = gr.Slider(value=42, minimum=0, maximum=2**32-1, step=1, label="Seed", info="A starting point to initiate the generation process, put 0 for a random one")

examples = [
    ["A storefront with 'Text to Image' written on it.", "Expand the following prompt to add more detail", 512, 1.2, 0.5, "fp16", 1, 50, 42]
]

gr.Interface(
    fn=generate,
    inputs=[your_prompt, task_prefix, max_new_tokens, repetition_penalty, temperature, model_precision_type, top_p, top_k, seed],
    outputs=gr.Textbox(label="Better Prompt"),
    title="SuperPrompt-v1",
    description='Make your prompts more detailed! <br> <a href="https://github.com/Nick088Official/SuperPrompt-v1">Github Repository & Model used</a> <br> <a href="https://brianfitzgerald.xyz/prompt-augmentation/">Model Blog</a> <br> Ports made by [Nick088](https://linktr.ee/Nick088)',
    examples=examples,
).launch(share=False)
