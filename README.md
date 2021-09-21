# Scrape Websites with Python & NoSQL
Learn how to scrape websites with Python, Selenium, Requests HTML, Celery, FastAPI, & NoSQL.


Here's what each tool is used for:

- **Python 3.9** [download](https://www.python.org/download/) - programming the logic.
- **AstraDB** [sign up](https://dtsx.io/3nQnjz1) - highly perfomant and scalable database service by DataStax. AstraDB is a Cassandra NoSQL Database. [Cassandra](https://cassandra.apache.org/_/index.html) is used by Netflix, Discord, Apple, and many others to handle astonding amounts of data.
- **Selenium** [docs](https://selenium-python.readthedocs.io/) - an automated web browsing experience that allows:
  - Run all web-browser actions through code
  - Loads JavaScript heavy websites
  - Can perform standard user interaction like clicks, form submits, logins, etc.
- **Requests HTML** [docs](https://docs.python-requests.org/) - we're going to use this to parse an HTML document extracted from Selenium
- **Celery** [docs](https://docs.celeryproject.org/) - Celery providers worker processes that will allow us to schedule when we need to scrape websites. We'll be using [redis](https://redis.io/) as our task queue.
- **FastAPI** [docs](https://fastapi.tiangolo.com/) - as a web application framework to Display and monitor web scraping results from anywhere



This series is broken up into 4 parts:

- **Scraping** How to scrape and parse data from nearly any website with Selenium & Requests HTML. 
- **Data models** how to store and validate data with `cassandra-driver`, `pydantic`, and **AstraDB**.
- **Worker & Scheduling** how to schedule periodic tasks (ie scraping) integrated with Redis & AstraDB
- **Presentation** How to combine the above steps in as robust web application service



## Setup your system.
Below is a preflight checklist to ensure you system is fully setup to work with this course. All guides and setup can be found in the [setup](./setup) directory of this repo.

### Preflight checklist
- [] Install Selenium & Chromedriver - [setup guide](./setup/Install%20Selenium%20%26%20Chromedriver%20on%20your%20System.md)
- [] Install Redis  - [setup guide](./setup/Setup%20Redis.md)
- [] Create a virtual environment & install dependencies
- [] Setup an account with DataStax
- [] Create your first AstraDB and get API credentials
- [] Use `cassandra-driver` to verify your connection to AstraDB
