# Q: Give me a list of API URLs write two functions to make http calls to. One fucntion to should make a serial calls and other is for making parallel calls.

import requests
import threading 

def parallelApiCalls(urls):
  for url in urls:
    thread = threading.Thread(target=makeApiCall, args=(url, True))
    thread.start()

def serialApiCalls(urls):
  results = []
  with requests.Session() as session:
    for url in urls:
      results.append(makeApiCall(url))
  for result in results:
    print(result)

def makeApiCall(url, print_it=False):
  try:
    response = requests.get(url)
    if response.status_code == 200:
      if print_it:
        print(response.json())
      else:
        return response.json()
    else:
      if print_it:
        print(None)
      else:
        return None
  except Exception as e:
    print(f"There was an error getting the requests - {e}")
    return None

if __name__ == "__main__":
  urls = [
  'https://httpbin.org/delay/1',
  'https://httpbin.org/delay/2',
  'https://httpbin.org/delay/3'
  ]

  method = input('Which method you want to use:')
  if method == 'serial':
    serialApiCalls(urls=urls)
  elif method == 'parallel':
    parallelApiCalls(urls=urls)
  else:
    print("Not a valid input")