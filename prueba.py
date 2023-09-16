import keyboard
import asyncio

async def main():
    keyboard.on_press_key("a", lambda _: print("A key pressed"))
    keyboard.on_press_key("b", lambda _: print("B key pressed"))
    # Add more event handlers as needed
    while True:
        await print_i()
        await asyncio.Event().wait()
    # This will keep the program running and capturing keyboard events asynchronously
    

async def print_i():
    print("i")

if __name__ == "__main__":
    asyncio.run(main())

    
