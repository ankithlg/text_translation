#!/bin/bash

echo "🔄 Starting local deployment..."

# Kill any running Flask process on default port 5000
pkill -f "flask run" 2>/dev/null

# Optional: Create a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the app in the background
nohup flask run --host=0.0.0.0 --port=5000 &

echo "✅ Flask app is running on http://localhost:5000"
