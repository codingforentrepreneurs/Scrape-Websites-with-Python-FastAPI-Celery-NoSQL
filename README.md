# Scrape Websites with Python & NoSQL
Learn how to scrape websites with Python, Selenium, Requests HTML, Celery, FastAPI, & NoSQL.


Here's what each tool is used for:

- **Python** - programming the logic.
- **Selenium** - an automated web browsing experience that allows:
  - Run all web-browser actions through code
  - Loads JavaScript heavy websites
  - Can perform standard user interaction like clicks, form submits, logins, etc.
- **Requests HTML** - we're going to use this to parse an HTML document extracted from Selenium
- **Celery** - Celery providers worker processes that will allow us to schedule when we need to scrape websites
- **FastAPI** - as a web application framework to Display and monitor web scraping results from anywhere
- **AstraDB** - highly perfomant and scalable database service by DataStax. AstraDB is a Cassandra NoSQL Database. Cassandra is used by Netflix, Discord, Apple, and many others to handle astonding amounts of data.


This series is broken up into 4 parts:

- **Scraping** How to scrape and parse data from nearly any website with Selenium & Requests HTML. 
- **Data models** how to store and validate data with `cassandra-driver`, `pydantic`, and **AstraDB**.
- **Worker & Scheduling** how to schedule periodic tasks (ie scraping) integrated with Redis & AstraDB
- **Presentation** How to combine the above steps in as robust web application service
