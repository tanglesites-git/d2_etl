import asyncio
from time import perf_counter_ns

from Manifest.ManifestController import handle_reset
from WorldContent import build_world_content


async def main():
    start = perf_counter_ns()
    handle_reset()
    data_dict = await build_world_content()
    end = perf_counter_ns()

    print(f"Time: {(end - start) / 1_000_000_000} s")


if __name__ == '__main__':
    asyncio.run(main())
