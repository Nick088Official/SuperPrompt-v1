# SuperPrompt-v1
Very small AI Model that Makes your prompts better for AI Art
Model Used: https://huggingface.co/roborovski/superprompt-v1

## Usage Locally UI & NO UI

As its a very small model (77M parameters) it can run easily even on old PCs CPU:

1. Click on Code and download as a zip.
2. extract it and the SuperPrompt-v1.zip inside of it.
3. Open the install_and_run_no_ui.bat if you want to use it without ui, or install_and_run_no_ui.bat to use the Gradio UI (if its your first time installing the package transformers on Windows, then you may wanna check this https://learn.microsoft.com/en-us/windows/win32/fileio/maximum-file-path-limitation?tabs=powershell#enable-long-paths-in-windows-10-version-1607-and-later).
4. (UI VERSION ONLY): Ctrl+Click the Local URL link that will appear after installing (DO NOT CLOSE THE CMD UNTIL YOU'RE DONE).
5. After it downloads everything it will ask you for the prompt you want to make better.
6. Put the Max New Tokens, controls how long is the output, reccomended to the max which is 512.
7. Put the Repetition Penalty, the higher the less the ai repeats itself (it goes from 1.0 to 2.0).
8. Put the Temperature, Higher values produce more diverse outputs, (from 0 to 1).
9. Put the Top P, Higher values sample more low-probability tokens, (from 0 to 2).
10. Put the Top K, Higher k means more diverse outputs by considering a range of tokens, (from 1 to 100).
11. After you will get the generated better prompt and it will start all again.
12. If you want to delete it, open delete.bat and then put to the trash bin the .zip and folders of the SuperPrompt-v1.

## Usage Google Colab Online
### NO UI
Run <a target="_blank" href="https://colab.research.google.com/github/Nick088Official/SuperPrompt-v1/blob/main/SuperPrompt_v1_Manual.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

### UI (WARNING: COULD RISK YOUR GOOGLE COLAB FREE TIER ACC)
Run <a target="_blank" href="https://colab.research.google.com/github/Nick088Official/SuperPrompt-v1/blob/main/SuperPrompt_v1_UI.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

## Usage Hugging Face Space Online
1. Go to https://huggingface.co/spaces/Nick088/SuperPrompt-v1.
2. Click the 3 dots in the up right corner and duplicate space (login if asked to, also you can just use cpu or use a paid gpu, it barely matters).
3. After the space loads, write the prompt you want to be better.
4. You can click additional inputs and change the repetition penalty, the higher the less the ai repeats itself, it goes from 1.0 to 2.0.
5. Click Submit
