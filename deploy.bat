@echo off
echo ===============================
echo Deploying Flask Translation App
echo ===============================

REM (Optional) Activate virtual environment if you're using one:
REM call venv\Scripts\activate.bat

echo Installing required Python packages...
pip install flask googletrans==4.0.0-rc1

echo Starting Flask app...
python app.py

echo ==================================
echo Flask app deployed and running...
echo ==================================
