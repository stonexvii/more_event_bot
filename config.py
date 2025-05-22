import os
import dotenv

dotenv.load_dotenv('.env')
BOT_TOKEN = os.getenv('BOT_TOKEN')
CHANNEL_TG_ID = int(os.getenv('CHANNEL_TG_ID'))
ADMIN_TG_ID = int(os.getenv('ADMIN_TG_ID'))
