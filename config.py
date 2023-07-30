from os import getenv
from sys import exit

TOKEN = getenv('BOT_TOKEN')
if not TOKEN:
    exit('Error: no token provided')
