import asyncio


async def greet(name):
    print(f' Hello, {name}')
    await asyncio.sleep(1)
    print(f' Goodbye, {name}')
    return name.upper()


# coro = greet('Anton')
# print(type(coro))
#
#
# result= asyncio.run(greet('Anton'))
# print(result)





# async def main():
#     result= await asyncio.gather(
#         greet('Alex'),
#         greet('Bob'),
#         greet('Cathy')
#     )
#     print(result)
#
# asyncio.run(main())


# async def main():
#     task_1 = asyncio.create_task(greet('task_1'))
#     result_1 = await task_1
#     print(result_1)
#     task_2 = asyncio.create_task(greet('task_2'))
#     result_2 = await task_2
#     print(result_2)
#
# asyncio.run(main())



# async def main():
#     async with asyncio.TaskGroup() as task_group:
#         t1= task_group.create_task(greet("John"))
#         t2= task_group.create_task(greet("Jane"))
#         result_1= await t1
#         print(result_1)
#         result_2= await t2
#         print(result_2)
#
# asyncio.run(main())




async def main():
    async with asyncio.TaskGroup() as task_group:
        t1 = task_group.create_task(greet("A"))
        t2= task_group.create_task(greet("B"))
        result= await asyncio.gather(t1,t2)
        print(result)
    # asyncio.Lock
    # asyncio.Semaphore

asyncio.run(main())