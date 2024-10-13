## Part 1: Asynchronous HTTP Requests with aiohttp

### Task 1. Basic Async HTTP Request Task

__Task:__  Write a Python script that makes multiple asynchronous HTTP requests to fetch data from a public API (e.g., fetching details about GitHub repositories).


__Details:__

- Use aiohttp to make requests concurrently.
- Ensure error handling for failed requests or timeouts.
- Display the time taken to complete all requests.


### Task 2. Parsing JSON Data Task

__Task:__  Extend the previous task to parse the JSON response from the API and extract specific fields (e.g., repository name, stars, description).

__Details:__

- Use asyncio.gather to handle multiple requests at once.
- Parse and format the results neatly.

### Task 3. Writing to a File Task

__Task:__  Write the parsed API response data to a local file asynchronously.

__Details:__

- Save the extracted fields into a CSV or JSON file.
- Handle file operations asynchronously using aiofiles library.

<br>

# Solution for Task 1 and Task 2

[See solution for task1 and task2](/asyncio/task1/main.py)

[See solution for task3](/asyncio/task3/main.py)


