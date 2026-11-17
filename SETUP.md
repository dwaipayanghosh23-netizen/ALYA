SYSTEM REQUIREMENTS

Windows 10 or Windows 11

Python (compatible version specified by the developer)

Ollama

Internet connection for initial setup

Sufficient RAM and storage for your chosen AI model

NOTE:
AI model performance depends on your computer's hardware.
Larger models generally require more RAM and processing power.

INSTALL PYTHON

Visit:
https://www.python.org/downloads/

Download and install Python.

IMPORTANT:
During installation, enable:
"Add Python to PATH"

Open Command Prompt or PowerShell.

Verify installation:

python --version

If Python's version appears, installation was successful.

INSTALL OLLAMA

Visit:
https://ollama.com/download

Download Ollama for Windows.

Install Ollama.

Open Command Prompt or PowerShell.

Verify installation:

ollama --version

If the version appears, Ollama is installed successfully.

DOWNLOAD ALYA'S AI MODEL

ALYA uses Ollama to run its AI model locally.

Open Command Prompt or PowerShell.

Execute the following command:

ollama pull YOUR_MODEL_NAME

IMPORTANT:
Replace YOUR_MODEL_NAME with the exact model specified in the ALYA repository.

Wait for the download to finish.

The model only needs to be downloaded once.

DOWNLOAD ALYA

Option A: Download ZIP

Visit the ALYA GitHub repository.

Click the green CODE button.

Select Download ZIP.

Extract the downloaded ZIP file.

Open the extracted ALYA folder.

Option B: Clone using Git

git clone YOUR_REPOSITORY_URL

cd ALYA

INSTALL ALYA DEPENDENCIES

Open Command Prompt or PowerShell inside the ALYA folder.

Run:

pip install -r requirements.txt

Wait until all required Python packages are installed.

RUN ALYA

Make sure Ollama is installed and running.

Inside the ALYA folder, double-click:

run.bat

Alternatively, execute:

run.bat

from Command Prompt or PowerShell.

ALYA should now launch in your terminal.

Enjoy ALYA V1!

TROUBLESHOOTING

PROBLEM: Python is not recognized.

SOLUTION:
Reinstall Python and enable "Add Python to PATH".

PROBLEM: Ollama is not recognized.

SOLUTION:
Check whether Ollama is installed correctly.
Restart your terminal after installation.

PROBLEM: Model not found.

SOLUTION:
Run the correct ollama pull command again.

PROBLEM: ALYA cannot connect to Ollama.

SOLUTION:
Make sure Ollama is running on your computer.

PROBLEM: ALYA runs slowly.

SOLUTION:
Your computer might not have sufficient resources for the selected model.
Try a smaller compatible model if supported.

FEEDBACK & BUG REPORTS

ALYA V1 is an early version of the project.

Your feedback is important!

If you encounter bugs, errors, unexpected responses, or have suggestions:

Open an Issue on the GitHub repository.

Describe the problem.

Include relevant error messages.

THANK YOU FOR TESTING ALYA V1!

Suggest improvements.

Please avoid sharing personal information or private conversation logs.
