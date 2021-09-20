# Setup Selenium & Chromedriver on your System

## Using Google Colab
Go to [this link](https://colab.research.google.com/github/codingforentrepreneurs/Scrape-Websites-with-Python-FastAPI-Celery-NoSQL/blob/main/setup/chromedriver-selenium-notebook.ipynb). It uses the notebook saved [here](./chromedriver-selenium-notebook.ipynb).

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
