# SuperPrompt-v1

[![Discord](https://img.shields.io/discord/1198701940511617164?color=%23738ADB&label=Discord&style=for-the-badge)](https://discord.gg/dnrgs5GHfG)

Very small AI Model that Makes your prompts better for AI

Model Used: https://huggingface.co/roborovski/superprompt-v1

Check the model blog here: https://brianfitzgerald.xyz/prompt-augmentation/

## Usage Locally UI & NO UI

### Python Code

```py
pip install transformers
```
if its your first time installing the package transformers on Windows, then you may wanna check this https://learn.microsoft.com/en-us/windows/win32/fileio/maximum-file-path-limitation?tabs=powershell#enable-long-paths-in-windows-10-version-1607-and-later.
```py
from transformers import T5Tokenizer, T5ForConditionalGeneration

tokenizer = T5Tokenizer.from_pretrained("google/flan-t5-small")
model = T5ForConditionalGeneration.from_pretrained("roborovski/superprompt-v1", device_map="auto")

input_text = "Expand the following prompt to add more detail: A storefront with 'Text to Image' written on it."
input_ids = tokenizer(input_text, return_tensors="pt").input_ids.to("cuda")

outputs = model.generate(input_ids, max_new_tokens=77)
print(tokenizer.decode(outputs[0]))

# The neon sign above the storefront reads "NeurIPS" in bold, white letters. The storefront is surrounded by a bustling cityscape, with skyscrapers and neon signs lining the walls. The sign is surrounded by a variety of colorful goods, including a variety of fruits, vegetables, and fruits, all arranged in a neat and organized manner. The storefront is surrounded by a bustling crowd of people, all chatting and laughing as they go about their daily routines.
```

### Precompiled
As its a very small model (77M parameters) it can run easily even on old PCs CPU:

1. [Install Python](https://www.python.org/downloads/), if you haven't already.
2. Click on Code and download as a zip.
3. extract it and the SuperPrompt-v1.zip inside of it.
4. Open the install_and_run_no_ui.bat if you want to use it without ui, or install_and_run_gradio_ui.bat to use the Gradio UI (if its your first time installing the package transformers on Windows, then you may wanna check this https://learn.microsoft.com/en-us/windows/win32/fileio/maximum-file-path-limitation?tabs=powershell#enable-long-paths-in-windows-10-version-1607-and-later).
5. It will ask you which model precision type to use: fp16 which is faster and less resources consuming or fp32 which is more precised but slower and more resources consuming.
6. (UI VERSION ONLY): Ctrl+Click the Local URL link that will appear after installing (DO NOT CLOSE THE CMD UNTIL YOU'RE DONE).
7. After it downloads everything it will ask you for the prompt you want to make better.
8. Put the Max New Tokens, controls how long is the output, reccomended to the max which is 512.
9. Put the Repetition Penalty, the higher the less the ai repeats itself (it goes from 1.0 to 2.0).
10. Put the Temperature, Higher values produce more diverse outputs, (from 0 to 1).
11. Put the Top P, Higher values sample more low-probability tokens, (from 0 to 2).
12. Put the Top K, Higher k means more diverse outputs by considering a range of tokens, (from 1 to 100).
13. Put the Seed, A starting point to initiate the generation process, any integers, put 0 if you want it to be random.
14. After you will get the generated better prompt and it will start all again.
15. If you want to delete it, open delete.bat and then put to the trash bin the .zip and folders of the SuperPrompt-v1.

## Usage Google Colab Online
### NO UI
Run <a target="_blank" href="https://colab.research.google.com/github/Nick088Official/SuperPrompt-v1/blob/main/SuperPrompt_v1_Manual.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

### UI 
#### Ipywidgets
Run <a target="_blank" href="https://colab.research.google.com/github/Nick088Official/SuperPrompt-v1/blob/main/SuperPrompt_v1_Ipywidgets_UI.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

#### Gradio **(WARNING: COULD RISK YOUR GOOGLE COLAB FREE TIER ACC)**
Run <a target="_blank" href="https://colab.research.google.com/github/Nick088Official/SuperPrompt-v1/blob/main/SuperPrompt_v1_Gradio_UI.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>


## Usage Hugging Face Space Online
1. Go to https://huggingface.co/spaces/Nick088/SuperPrompt-v1.
2. Click the 3 dots in the up right corner and duplicate space (login if asked to, also you can just use cpu or use a paid gpu, it barely matters).
3. After the space loads, write the prompt you want to be better.
4. You can click additional inputs and change the repetition penalty, the higher the less the ai repeats itself, it goes from 1.0 to 2.0.
5. Click Submit
