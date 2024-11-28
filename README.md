# Python Tasks Project

This project provides a Dockerized solution to perform three specific tasks: 
- Manage a dictionary
- Build a word from specific letters
- Calculate the total cost of items with tax

The project is implemented in Python and supports execution through Docker.

## Prerequisites

Ensure you have [Docker](https://www.docker.com/) installed on your machine.

## Usage Instructions

### Pulling the Docker Image
You can pull the pre-built image from Docker Hub using:
```bash
docker pull eyders/python-tasks:latest
````

## Running the Docker Image
The Docker container executes a `main.py` script that allows you to choose between three tasks: `dictionary`, `word_builder`, and `cost_calculator`. You can set the task and required parameters via environment variables.

### Task 1: Dictionary Operations
To add a word to the dictionary and retrieve its definition:
```bash
docker run --rm \
  -e TASK=dictionary \
  -e WORD=apple \
  -e DEFINITION="A fruit that grows on trees." \
  eyders/python-tasks:latest
```

To look up an existing word in the dictionary:
```bash
docker run --rm \
  -e TASK=dictionary \
  -e WORD=apple \
  eyders/python-tasks:latest
```


### Task 2: Cost Calculator
To calculate the total cost of specific items with a given tax:
```bash
docker run --rm \
  -e TASK=cost_calculator \
  -e ITEMS="socks,shoes" \
  -e TAX=0.1 \
  eyders/python-tasks:latest
```
In this example:

- ITEMS specifies the items to calculate, separated by commas.
- TAX specifies the tax rate as a decimal (e.g., 0.1 for 10%).

### Task 3: Word Builder
To build a word from specific letters of a list of words:
```bash
docker run --rm \
  -e TASK=word_builder \
  -e WORDS="hello,word,python" \
  eyders/python-tasks:latest
```