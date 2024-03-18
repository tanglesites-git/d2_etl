from enum import Enum

from Manifest.ManifestModel import ManifestModel
from Manifest.ManifestResponse import ManifestResponse

from Settings import Files, Dirs, settings, Environment
from Contexts import ManifestResponseRepository


def handle_reset():
    ENV = settings.Environment
    Dirs().create()
    Files().create()
    manifest_repo = ManifestResponseRepository()
    manifest_repo.create_manifest_data_tables()

    Manifest = ManifestModel()

    if ENV == Environment.DEVELOPMENT.name:
        Manifest.Read_Manifest()

    if ENV == Environment.PRODUCTION.name:
        Manifest.Download_Manifest()

    manifest_response = ManifestResponse.From(Manifest)

    result = manifest_repo.select_manifest_data()
    rows = result.fetchall()

    if rows[0][0] == manifest_response.version:
        print("No new manifest")
    else:
        print("Updating Manifest")
        manifest_repo.insert_into_manifest_data_tables(manifest_response)

    manifest_repo.conn.commit()
    manifest_repo.conn.close()
