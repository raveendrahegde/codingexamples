# You are tasked with writing an asynchronous program to scrape the titles from multiple web pages to demonstrate async programming in Python. 
# You should use the aiohttp library for making asynchronous HTTP requests and asyncio to manage the concurrency. 
# The program should accept a list of URLs, fetch the pages concurrently, and extract the <title> tag content from each page.

import asyncio
import aiohttp
from bs4 import BeautifulSoup

async def fetchTitle(url):
  async with aiohttp.ClientSession() as session:
    response = await session.get(url)
    text = await response.text()
    soup = BeautifulSoup(text, 'html.parser')
    return soup.title.string

async def main():
  urls = [
  'https://docs.python.org/3/library/asyncio.html',
  'https://www.geeksforgeeks.org/how-to-check-if-an-object-is-iterable-in-python/'
  ]

  tasks = [asyncio.create_task(fetchTitle(url)) for url in urls]  # Explore asyncio.gather()

  for task in tasks:
    result = await task
    print(result)

if __name__ == "__main__":
  asyncio.run(main())
