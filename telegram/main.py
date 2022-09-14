import config
from telethon import TelegramClient
import asyncio


async def main():
    phone = "+79992125549"
    client = TelegramClient("SongBot", config.API_ID, config.API_HASH)
    await client.connect()
    if not client.is_user_authorized():
        await client.send_code_request(phone) #при первом запуске - раскомментить, после авторизации для избежания FloodWait советую закомментить
        await client.sign_in(phone, input('Enter code: '))
    msg = await client.send_file("SongBot", "/home/vadim/PycharmProjects/Tosong/audios/GunsNRoses-NovemberRain.mp3")
    print(msg)
    client.disconnect()



if __name__ == "__main__":
    asyncio.run(main())


