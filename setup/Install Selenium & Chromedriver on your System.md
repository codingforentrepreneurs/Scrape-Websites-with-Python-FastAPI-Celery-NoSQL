# Setup Selenium & Chromedriver on your System

There are many ways to use chromedriver & selenium. Here are the ways we do it in this guide:

- Google Colab
- Deepnote
- macOS
- Linux (debian systems)
- Windows (coming soon)
- Docker

## Google Colab
Go to [this link](https://colab.research.google.com/github/codingforentrepreneurs/Scrape-Websites-with-Python-FastAPI-Celery-NoSQL/blob/main/setup/chromedriver-selenium-notebook.ipynb). It uses the notebook saved [here](./chromedriver-selenium-notebook.ipynb).

## Deepnote
Much like Google Colab, you can use Deepnote.com to run this setup. Click [this link](https://deepnote.com/launch?name=Scrape-Websites-with-Python-FastAPI-Celery-NoSQL&url=https://github.com/codingforentrepreneurs/Scrape-Websites-with-Python-FastAPI-Celery-NoSQL/blob/main/setup/chromedriver-selenium-notebook.ipynb) to launch it. It uses the notebook saved [here](./chromedriver-selenium-notebook.ipynb).


## macOS
### 1. Install __chromedriver__ via [homebrew](https://brew.sh) [formulae](https://formulae.brew.sh/cask/chromedriver)
```
brew install --cask chromedriver
```

### 2. Create and activate a virtual environment
```
cd path/to/your/project
```

```
python3 -m venv .
```

```
source bin/activate
```

### 3. Install Selenium
```
pip install selenium
```
> You can use `path/to/your/project/bin/pip install selenium` as well


## Linux (debian)

### 1. Install __chromedriver__ via apt
```
sudo apt-get update
sudo apt-get install -y \
    build-essential \
    python3-dev \
    python3-setuptools \
    chromium-driver
```

### 2. Create and activate a virtual environment
```
cd path/to/your/project
```

```
python3 -m venv .
```

```
source bin/activate
```

### 3. Install Selenium
```
pip install selenium
```
> You can use `path/to/your/project/bin/pip install selenium` as well


## Windows (coming soon)



## Using Docker 

__pre-built__
```dockerfile
FROM codingforentrepreneurs/python:3.9-webapp-selenium
```

__manually__
```dockerfile
FROM python:3.9-slim

RUN apt-get update && \
    apt-get install -y \
    build-essential \
    python3-dev \
    python3-setuptools \
    git \
    git-crypt \
    unzip \
    chromium-driver \
    gcc \
    make

RUN python -m pip install selenium

# Create a virtual environment in /opt
RUN python3 -m venv /opt/venv && /opt/venv/bin/python -m pip install selenium

RUN apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*
```
