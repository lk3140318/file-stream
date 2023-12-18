# (c) adarsh-goel (c) @biisal
import os
from os import getenv, environ
from dotenv import load_dotenv



load_dotenv()
bot_name = "Bɪɪsᴀʟ Fɪʟᴇ2Lɪɴᴋ Bᴏᴛ"
bisal_channel = "https://telegram.me/bisal_files"
bisal_grp = "https://t.me/+PA8OPL2Zglk3MDM1"

class Var(object):
    MULTI_CLIENT = False
    API_ID = int(getenv('API_ID', '24335028'))
    API_HASH = str(getenv('API_HASH', 'b204ec833fb451fb913fc8e683b232d0'))
    BOT_TOKEN = str(getenv('BOT_TOKEN' , '6699190464:AAG0Z8EGVxCnJ0hoMAO6mUvkYZnLZ7Wkl0U'))
    name = str(getenv('name', 'File_sharing_A_2_Z_Bot'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL', -1001586217765'))
    NEW_USER_LOG = int(getenv('NEW_USER_LOG', '-1002045377846'))
    PORT = int(getenv('PORT', '8080'))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "5213073489").split())  
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    OWNER_USERNAME = str(getenv('OWNER_USERNAME', '@A_z_Top_Rrr'))
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('File_sharing_A_2_Z')) #dont need to fill anything here
    
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', 'BIND_ADRESS:PORT')) if not ON_HEROKU or getenv('FQDN', '') else APP_NAME+'.herokuapp.com'
    HAS_SSL=bool(getenv('HAS_SSL',True))
    if HAS_SSL:
        URL = "https://{}/".format(FQDN)
    else:
        URL = "http://{}/".format(FQDN)
    DATABASE_URL = str(getenv('DATABASE_URL', 'mongodb+srv://lk3140318:yqduo05hHUIX15eU@cluster0.nygifov.mongodb.net/?retryWrites=true&w=majority'))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', '@FilmiChannelMix')) 
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "-1002122595775")).split()))   
    BAN_CHNL = list(set(int(x) for x in str(getenv("BAN_CHNL", "SAME AS BANNED CHANNELS")).split()))   
    
