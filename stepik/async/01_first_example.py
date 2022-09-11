import asyncio
import random


async def do(value: str):
    print("----")
    await asyncio.sleep(1)
    print(value)


async def main():
    await do(str(10))
    print("from main")


def check_while() -> None:
    step = 0
    while step < 10:
        x = random.randint(1, 100)
        print(x)
        step += 1
        if x < 10:
            break
    else:
        print("было 10 попыток")


if __name__ == "__main__":
    check_while()
