from os import environ

API_ID = int(environ.get("API_ID", "14091414"))
API_HASH = environ.get("API_HASH", "1e26ebacf23466ed6144d29496aa5d5b")
BOT_TOKEN = environ.get("BOT_TOKEN", "5752952621:AAGO61IiffzN23YuXyv71fbDztA_ubGM6qo")
ADMIN = [int(admin_id) for admin_id in environ.get("ADMIN", "5205602399, 5500572462").split(",")]
CAPTION = environ.get("CAPTION", "loda")

# for thumbnail (back end is MrMKN brain 😉)
DOWNLOAD_LOCATION = "./DOWNLOADS"
