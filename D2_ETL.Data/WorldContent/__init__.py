import asyncio
import sqlite3

from json import loads

import aiofiles

from Contexts import ManifestResponseRepository
from aiohttp import ClientSession

from Settings import Environment, settings, Dirs

manifest_repo = ManifestResponseRepository()
tables = manifest_repo.select_table_paths()


def get_table_name(path):
    name = path.split('/')[-1]
    name = name.split('-')[0]
    return name


async def request_table(session: ClientSession, path: str, name: str, data_dict: dict):
    if Environment.DEVELOPMENT.name == settings.Environment:
        print("Reading from local file...", name)
        async with aiofiles.open(Dirs.JSON / f'{name}.json', 'r', encoding="utf-8") as file:
            data = loads(await file.read())
            data_dict[name] = data
        print("Done Processing...", name)
    else:
        print("Requesting from Bungie...", name)
        async with session.get(f'https://www.bungie.net{path}') as response:
            manifest = await response.json()
            data_dict[name] = manifest
        print("Done Processing...", name)


async def get_all_tables():
    tasks = []
    data_dict = {}
    async with ClientSession() as session:
        for path in tables:
            name = get_table_name(path)
            print("Processing...", name)
            tasks.append(request_table(session, path, name, data_dict))
        await asyncio.gather(*tasks)
    return data_dict


async def build_world_content():
    return await get_all_tables()
