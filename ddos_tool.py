import threading
import requests

target_url = "https://httpbin.org/get"

def send_requests():
    while True:
        try:
            response = requests.get(target_url)
            print(f"Request sent: {response.status_code}")
        except Exception as e:
            print(f"Error {e}")


num_threads = 10
threads = []
for i in range(num_threads):
    thread = threading.Thread(target=send_requests)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()