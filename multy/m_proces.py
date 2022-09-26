import requests
import time
from multiprocessing import Pool, Manager, Value, Process

url = 'https://en.wikipedia.org/wiki/Political_impact_of_the_COVID-19_pandemic'


def req(url=url):
    print("starting")
    r = requests.get(url)
    print("ending")
    return r


tasks = [url for x in range(10)]

if __name__ == "__main__":
    start_time = time.time()
    with Pool() as p:
        p.map(req, tasks)
    print(time.time() - start_time)
