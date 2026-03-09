import os
from dotenv import load_dotenv

load_dotenv()

AWS_SECRET_KEY = os.getenv('AWS_SECRET_KEY')

def connect():
    if AWS_SECRET_KEY:
        print(f"Connecting with: {AWS_SECRET_KEY}")
    else:
        print("AWS_SECRET_KEY not set")
