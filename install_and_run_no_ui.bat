@echo off
setlocal

REM Check if venv_no_ui folder exists in the root directory and if requirements are installed
if not exist "%~dp0venv_no_ui\" (
    REM Print the step to the terminal
	echo Creating virtual environment...

    REM Create a virtual environment named "venv_no_ui" in the root directory
    python -m venv "%~dp0venv_no_ui"
	
    REM Print the step to the terminal
    echo Activating the virtual environment...

    REM Activate the virtual environment
    call "%~dp0venv_no_ui\Scripts\activate.bat"
	
    REM Print the step to the terminal
    echo Installing requirements...

    REM Install requirements inside the virtual environment
    pip install -r "%~dp0Scripts\requirements_no_ui.txt"
) else (
    echo Required packages are already installed and Virtual environment is already created.
	
	REM Print the step to the terminal
    echo Activating the virtual environment...

    REM Activate the virtual environment
    call "%~dp0venv_no_ui\Scripts\activate.bat"
)


REM Print the step to the terminal
echo Running Python script...

set /p your_prompt="Enter your prompt: "
set /p max_new_tokens="Enter the number of Max New Tokens (The maximum numbers of new tokens, controls how long is the output, int value from 256 to 512) : "
set /p repetition_penalty="Enter the Repition Penalty (Penalize repeated tokens, making the AI repeat less itself, float value from 0.1 to 2.0) : "
set /p temperature="Enter the model precision type (Higher values produce more diverse outputs, float value from 0.1 to 1.0): "
set /p top_p="Enter the Top P (Higher values sample more low-probability tokens, float value from 0.1 to 2.0): "
set /p top_k="Enter the Top K (Higher k means more diverse outputs by considering a range of tokens, int value from 1 to 100): "
set /p seed="Enter the seed (A starting point to initiate the generation process, put an integer or 0 for random): "

REM Run your Python file here
python %~dp0Scripts\install_and_run_no_ui.py "\"%your_prompt%\"" %max_new_tokens% %repetition_penalty% %temperature% %top_p% %top_k% %seed%

REM Print the step to the terminal
echo Deactivating the virtual environment...

REM Deactivate the virtual environment
call "%~dp0venv_no_ui\Scripts\deactivate.bat"

REM Print the step to the terminal
echo Script execution complete.

endlocal

pause /k