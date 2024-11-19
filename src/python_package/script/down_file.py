import requests
import asyncio
import aiohttp
import os
from ..decorators.time_logger import time_logger

# 下载指定软件脚本

# download single thread
def download_file(url, save_path):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)

        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

        print(f"Download completed: {save_path}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred during download: {e}")

# download 异步
@time_logger
async def superdownload(url,save_path:str):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                response.raise_for_status()
                with open(save_path,"wb") as file:
                    while True:
                        chunk = await response.content.read(8192)
                        if not chunk:
                            break
                        file.write(chunk)
        print(f"download completed:{save_path}")
    except Exception as e:
        print(f"An error occurred during download:{e}")

async def t1down_file():

    url = "https://www.listary.com/download-completion?version=stable"
        # installer_filename = "listary"
    save_path = '/Users/haveanicedayi/winapp/listary_installer.exe'

    # Ensure the directory exists
    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    # Download the file
    await superdownload(url, save_path)

if __name__ == "__main__":
    # url = "https://www.listary.com/download-completion?version=stable"
    # # installer_filename = "listary"
    # save_path = '/Users/haveanicedayi/winapp/listary_installer.exe'

    # # Ensure the directory exists
    # os.makedirs(os.path.dirname(save_path), exist_ok=True)

    # # Download the file
    # download_file(url, save_path)
    asyncio.run(t1down_file())

