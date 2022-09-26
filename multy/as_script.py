import requests
import time
import asyncio

url = 'https://en.wikipedia.org/wiki/Political_impact_of_the_COVID-19_pandemic'


async def req(url=url):
    print("starting")
    r = requests.get(url)
    print("ending")
    return r


def timer_fn(fn):
    def inner(*args, **kwargs):
        start = time.time()
        code = fn(*args, **kwargs)
        calculated_time = time.time() - start
        return (code, calculated_time)

    return inner


@timer_fn
def response_time(url):
    return requests.get(url).status_code


tasks = []


async def main():
    for i in range(10):
        # tasks.append(asyncio.create_task(req))
        tasks.append(asyncio.to_thread(response_time, url))
    list_of_responses = await asyncio.gather(*tasks)
    return list_of_responses


if __name__ == "__main__":
    start_time = time.time()
    print(asyncio.run(main()))

    print(time.time() - start_time)
