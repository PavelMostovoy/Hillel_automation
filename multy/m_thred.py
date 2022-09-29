import concurrent.futures
from concurrent.futures.thread import ThreadPoolExecutor
from concurrent.futures.process import ProcessPoolExecutor

import requests
import time

url = 'https://en.wikipedia.org/wiki/Political_impact_of_the_COVID-19_pandemic'


def request_funct(url=url):
    # print("starting")
    response = requests.get(url)
    # print("ending")
    return response.elapsed.total_seconds()


def function_cpu():
    c = 0
    for i in range(100_000_000):
        c *= i


#
# start_time = time.time()
# pool_single = [url]*100
# for url in pool_single:
#     print(request_funct(url))
#
# print(f"Total time : {time.time() - start_time}")


if __name__ == "__main__":
    start_time = time.time()
    with ProcessPoolExecutor() as executor:
        pool = [executor.submit(function_cpu) for x in range(10)]
        for response_object in concurrent.futures.as_completed(pool):
            ...
            # print(f"Single responce time = {response_object.result()}")

    print(f"Total time : {time.time() - start_time}")
