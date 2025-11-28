import os

class Config:
    BOT_TOKEN = os.environ.get("BOT_TOKEN")       # name of env var
    API_ID = int(os.environ.get("API_ID"))        # name of env var
    API_HASH = os.environ.get("API_HASH")
    AUTH_USERS = os.environ.get("AUTH_USERS", "7540570087") # optional, comma-separated IDs
