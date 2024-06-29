import subprocess
import time
import sys

def start_backend():
    print("Starting FastAPI backend server...")
    subprocess.Popen(["uvicorn", "main:app", "--reload"])

def start_frontend():
    print("Starting Streamlit frontend server...")
    subprocess.Popen(["streamlit", "run", "frontend.py"])

def main():
    start_backend()
    time.sleep(2)  # Adjust delay if necessary for backend to fully start before frontend
    start_frontend()

if __name__ == "__main__":
    main()