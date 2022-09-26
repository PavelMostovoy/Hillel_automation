import requests
import time
import asyncio

url = 'https://en.wikipedia.org/wiki/Political_impact_of_the_COVID-19_pandemic'


# urls = ["http://google.com", "http://wikipedia.com", "https://google.com",
#         "http://microsoft.com"]


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


list_of_urls = []
for i in range(10):
    list_of_urls.append(url)

tasks = []
list_of_responses = []


async def main():
    """
    Main Asyncio runner
    run looper for asynchronous run
    """
    loop = asyncio.get_event_loop()

    for url in list_of_urls:
        tasks.append(loop.run_in_executor(None, response_time, url))
    # do something with tasks section
    for future in tasks:
        if await future:
            response = future.result()
            list_of_responses.append(response)


if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
    print(list_of_responses)
    print(time.time() - start)
