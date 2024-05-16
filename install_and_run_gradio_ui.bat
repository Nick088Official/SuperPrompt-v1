@echo off
setlocal

REM Check if venv_ui folder exists in the root directory and if requirements are installed
if not exist "%~dp0venv_ui\" (
    REM Print the step to the terminal
	echo Creating virtual environment...

    REM Create a virtual environment named "venv_ui" in the root directory
    python -m venv "%~dp0venv_ui"

) else (
    echo Required packages are already installed and Virtual environment is already created.
	
	REM Print the step to the terminal
    echo Activating the virtual environment...

    REM Activate the virtual environment
    call "%~dp0venv_ui\Scripts\activate.bat"
)

REM Print the step to the terminal
echo Running Python script...

REM Run your Python file here
python "%~dp0Scripts\install_and_run_gradio_ui.py"

REM Print the step to the terminal
echo Deactivating the virtual environment...

REM Deactivate the virtual environment
call "%~dp0venv_ui\Scripts\deactivate.bat"

REM Print the step to the terminal
echo Script execution complete.

endlocal

pause /k