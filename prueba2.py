import asyncio
import keyboard

async def print_something_periodically():
    keyboard.on_press_key("space", lambda _: print("A key pressed"))
    keyboard.on_press_key("b", lambda _: print("B key pressed"))
    while True:
        print("Printing something in an async loop...")
        await asyncio.sleep(1)  # Wait for 1 second before printing again

async def main():
    # Start the printing coroutine
    await print_something_periodically()

if __name__ == "__main__":
    asyncio.run(main())
