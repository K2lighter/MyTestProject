import os
from dotenv import load_dotenv

load_dotenv()


class Data:
    Login = os.getenv("Login")
    Password = os.getenv("Password")

