# Pulitzer Prize API

## Objective
Create an API that retrieves the year, author, and title for Pulitzer 
Prize winners of fiction from the database, then deploy the application to Azure.

Application is live here: https://pulitzerprizeforfiction.azurewebsites.net/api/data
## Tools
- Python

![](https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg)
- Flask

![](https://upload.wikimedia.org/wikipedia/commons/3/3c/Flask_logo.svg){width=50%}
- Azure

![](https://upload.wikimedia.org/wikipedia/commons/a/a8/Microsoft_Azure_Logo.svg)
## Steps
- Created NoSQL database
    - In Azure portal, created Cosmos DB account
    - In Cosmos DB account, created database
    - In database, created a container that holds the collection of items (partitioned by year)
        - Items composed of data from: https://en.wikipedia.org/wiki/Pulitzer_Prize_for_Fiction
- Configured Azure App Service plan
- Set-up key management
    - Configured the Key Vault
    - Created a new secret that contains the read-only key to the database
    - Added access policy for application
- Created GET request
    - Configured connection to database using key management
    - Wrote GET request to query the data in database
    - Wrote test script to validate application locally
- Deployed to Azure App Service
    - Created requirements.txt file to import modules needed for the application
    - In the terminal:
        - cd [insert application file path here]
        - az login
        - python3 -m venv .venv
        - source .venv/bin/activate
        - pip install -r requirements.txt
        - flask run
        - az webapp up --sku B1 --name [insert application name here]
    - After the deployment was successful the application went live
