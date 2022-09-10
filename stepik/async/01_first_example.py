import asyncio


async def do(value: str):
    print("----")
    await asyncio.sleep(1)
    print(value)


async def main():
    await do(str(10))
    print("from main")


if __name__ == "__main__":
    asyncio.run(main())
