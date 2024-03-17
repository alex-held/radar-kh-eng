import logging
from telethon.sync import TelegramClient
from telethon.types import PeerChannel 
import timer
import typing
from dotenv import load_dotenv
import os
from telethon.sessions import StringSession
import translation

load_dotenv()

API_ID = os.getenv("API_ID")
API_HASH  = os.getenv("API_HASH")
TOKEN = os.getenv("TOKEN")
STAGE = os.getenv("STAGE")
SESSION = os.getenv("SESSION")
LOCAL_SESSION = os.getenv("LOCAL_SESSION")

def get_session() -> str:
    if LOCAL_SESSION != None:
        return LOCAL_SESSION
    return SESSION

class Bot:
    channel_Radar_KH = PeerChannel(1850203289)
    channel_Radar_KH_ENG = PeerChannel(2020532266)

    client =  TelegramClient(StringSession(get_session()), api_id=API_ID, api_hash=API_HASH)
    id_offset = 0

    botClient = TelegramClient(session="bot", api_id=API_ID, api_hash=API_HASH)

    def __init__(self):
        logging.info(msg="initalizing!")
        self.client.flood_sleep_threshold = 0 
        self.client.start()
        logging.log(level=logging.INFO, msg="client started!")

        self.botClient.start(bot_token=TOKEN)
        logging.log(level=logging.INFO, msg="bot-client started!")

        self.getLatestMessageID()
        logging.info(f"initalization complete! id={self.id_offset}")

    def getLatestMessageID(self):
        for message in self.client.iter_messages(self.channel_Radar_KH,limit=1):
            logging.info(f"got latest message id {message.id}")
            self.id_offset = message.id
 
    def get_radar_kh_channel(self):
        channel = self.client.get_entity('https://t.me/radar_kharkov')
        return channel
    
    def send_messages(self,messages: typing.List[str]):
     for message in messages:
        if STAGE == "dev":
            print(f"{message}")
        else:
            self.botClient.send_message(self.channel_Radar_KH_ENG, message)

    def fetch_messages(self) -> typing.List[str]:
        messages = []
        logging.info(f"polling request from offset: {self.id_offset}")
        for message in self.client.iter_messages(self.channel_Radar_KH, reverse=True, offset_id=self.id_offset-3):
            messages.append(message)
            print(message)
            self.id_offset = message.id
        return messages

    def translate_messages(self,messages: typing.List[str]):
        for message in messages:
            yield translation.translate(message=message.message)

    def executeOnce(self):
        messages = self.fetch_messages()
        translated = self.translate_messages(messages=messages)
        self.send_messages(messages=translated)
    
    def run(self):
        t = timer.Timer()
        t.do_every(2, self.executeOnce)

def main():
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )
    
    bot = Bot()
    bot.run()


main()