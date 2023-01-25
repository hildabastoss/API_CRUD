from time import sleep
import asyncio


async def func_1():
    print('inicio func_1')
    await asyncio.sleep(3)
    print('termino func_1')
    
    
async def func_2():
    print('inicio func_2')
    await asyncio.sleep(3)
    print('termino func_2')
    
async def main():
    await asyncio.gather(
        func_1(),
        func_2(),
    )
  
asyncio.run(main())