# Análise de Log

![pep8](https://img.shields.io/badge/pep8online-compliant-green.svg)

## Description of Project

create a reporting tool that prints reports (in plain text) based on the data in the database. 
This reporting tool is a Python program using the ``psycopg2`` module to connect to the database.

### Issues to which the reporting tool should respond:
1. **What are the three most popular articles of all time?** Which articles were the most accessed? 
  Present this information as an organized list with the most popular article at the top.
  
  **Example:**
  - "Princess Shellfish Marries Prince Handsome" — 1201 views
  - "Baltimore Ravens Defeat Rhode Island Shoggoths" — 915 views
  - "Political Scandal Ends In Political Scandal" — 553 views
  
 2. **Who are the authors of most popular articles of all time?** That is, when you organize all the articles that each author wrote, which authors get the most views? 
  Present this information as an organized list with the most popular author at the top.
  
  **Example:**
   - Ursula La Multa — 2304 views
   - Rudolf von Treppenwitz — 1985 views
   - Markoff Chaney — 1723 views
   - Contribuidor anônimo — 1023 views
 
3. **On what days more than 1% of requests resulted in errors?**
The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser (see this lesson again if you want to review the idea of ​​HTTP status codes).

  **Example**
  - July 29, 2016 — 2.5% errors
  
## How to Install
1. Download or clone from github [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm), instructions on how to install **Vagrant** and **Virtual Box**.
2. Install [Vagrant](https://www.vagrantup.com/) and [Virtual Box](https://www.virtualbox.org/)
3. Download database [newsdata](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
4. To run the virtual machine we will use the terminal [GitBash](https://git-scm.com/downloads)

## How to Run
1. Inside the Vagrant directory activate the virtual machine with the **vagrant up** command.
2. After your activation, enter the **vagrant ssh** command to activate your virtual machine.
3. Load the database with the command ``psql -d news -f newsdata.sql``
4. In GitBash run the ``python analise_logs.py`` command to perform the parsing.
  
### License
MIT © Beatriz Nonato
