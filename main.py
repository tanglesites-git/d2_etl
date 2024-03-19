import asyncio
from json import loads, dumps
from time import perf_counter_ns

from Manifest.ManifestController import handle_reset
from Settings import Dirs
from WorldContent import build_world_content


async def main():
    start = perf_counter_ns()
    handle_reset()
    data_dict = await build_world_content()
    end = perf_counter_ns()

    print(f"Time: {(end - start) / 1_000_000_000} s")


if __name__ == '__main__':
    asyncio.run(main())
    start1 = perf_counter_ns()
    end1 = perf_counter_ns()

    # with open('indexing.json', 'w', encoding="utf-8") as f:
    #     f.write(dumps(indexing_dict, indent=4, sort_keys=True))

    print(f"Time dict: {(end1 - start1) / 1_000_000_000} s")