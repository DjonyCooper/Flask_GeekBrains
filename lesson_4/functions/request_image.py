import threading
import time
from multiprocessing import Process
import asyncio
import aiohttp
import requests

files = []


def download(url):
    start_time = time.time()
    img_file = requests.get(url)
    with open(f'downloads/{url.split('/')[-1:][0]}', 'wb') as save_file:
        save_file.write(img_file.content)
    files.append(f'{url.split('/')[-1:][0]} - время скачивания: {time.time()-start_time:.2f} сек.')
    return files

async def async_download(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            img_file = await response.content.read()
            with open(f'downloads/{url.split('/')[-1:][0]}', 'wb') as save_file:
                save_file.write(img_file)


def threads_download_img(url_dict):
    """
    url_dict: словарь содержащий URL адреса изображений
    """
    threads = []
    start_time = time.time()

    for url in url_dict:
        thread = threading.Thread(target=download, args=[url])
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    text = f'Запрос выполнен. Файлы:\n'
    for file_name in files:
        text += f'• {file_name}\n'
    text += f'- успешно загружены.\nВремя выполнения запроса: {time.time() - start_time:.2f} сек.'
    files.clear()
    return text


def processes_download_img(url_dict):
    """
    url_dict: словарь содержащий URL адреса изображений
    """
    processes = []
    start_time = time.time()

    for url in url_dict:
        process = Process(target=download, args=(url, ))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    text = f'Запрос выполнен. Файлы:\n'
    if len(files)>0:
        for file_name in files:
            text += f'• {file_name}\n'
    else:
        text += f'• Error: возникла проблема с отображением названий файлов'
    text += f'- успешно загружены.\nВремя выполнения запроса: {time.time() - start_time:.2f} сек.'
    files.clear()
    return text


async def async_download_img(url_dict):
    tasks = []
    for url in url_dict:
        task = asyncio.ensure_future(async_download(url))
        tasks.append(task)
    await asyncio.gather(*tasks)

