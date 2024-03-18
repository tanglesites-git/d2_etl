from json import dumps, loads

import requests

from Settings import Files


class ManifestModel:

    def __init__(self):
        self.manifest = None
        self.version = None

    def Read_Manifest(self):
        with open(Files.MANIFEST, "r", encoding="utf-8") as file:
            manifest_dict = loads(file.read())
            self.manifest = manifest_dict
            self.version = manifest_dict["Response"]["version"]

    def Download_Manifest(self):
        with requests.get('https://www.bungie.net/Platform/Destiny2/Manifest', stream=True,
                          allow_redirects=True) as response:
            self.manifest = response.json()
            self.version = self.manifest["Response"]["version"]
