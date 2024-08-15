import os
from dotenv import load_dotenv

load_dotenv()

queue_name = os.getenv("QUEUE_NAME")
host = os.getenv("HOST")
user_name = os.getenv("USER_NAME")
password = os.getenv("PASSWORD")
connection_string = os.getenv("CONNECTION_STRING")