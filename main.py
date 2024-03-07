import json
import time
import requests
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor


url = "https://dummyjson.com/products/"

def get_data(product_id, url):
    response = requests.get(url + str(product_id))
    data = response.json()
    return data

def run_threads(process_num):
    results = []
    with ThreadPoolExecutor() as executor:
        for i in range((process_num * 20) + 1, (process_num * 20) + 21):
            f = executor.submit(get_data, url=url, product_id=i)
            res = f.result()
            results.append(res)
        with open("out.json", "a") as outfile:
                json.dump(results, outfile, indent=2)

def main():
    with ProcessPoolExecutor() as executor:
        executor.map(run_threads, range(5)) 

if __name__ == '__main__':
    start = time.perf_counter()
    main()
    end = time.perf_counter()
    print(f"All the data is loaded in {end - start} time")