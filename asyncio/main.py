import asyncio

async def fetch_data(number):
    print(f"Starting task {number}")
    await asyncio.sleep(2)
    print(f"Ending task {number}")

    return f"Result from task {number}"


async def main():
    task = [fetch_data(i) for i in range(1, 4)]
    results = await asyncio.gather(*task)
    print(results)


asyncio.run(main())


# OUTPUT:

# Starting task 1
# Starting task 2
# Starting task 3
# Ending task 1
# Ending task 2
# Ending task 3
# ['Result from task 1', 'Result from task 2', 'Result from task 3']