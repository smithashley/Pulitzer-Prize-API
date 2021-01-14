#Pulitzer Prize API

## Objective
Create an API that retrieves the year, author, and title for Pulitzer 
Prize winners of fiction, then deployed the application to Azure.

Application is live here: https://pulitzerprizeforfiction.azureappservice.com/api/data
## Tools
- Python - version 3.7

![](https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg)
- Flask - version 1.1.2

![](https://upload.wikimedia.org/wikipedia/commons/3/3c/Flask_logo.svg)
- Git  

![](https://upload.wikimedia.org/wikipedia/commons/e/e0/Git-logo.svg)
- Azure 

![](https://upload.wikimedia.org/wikipedia/commons/a/a8/Microsoft_Azure_Logo.svg)

## Steps
- Created NoSQL database
    - In Azure portal, create Cosmos DB account
    - In Cosmos DB account, create database
    - Create a  container that will contain the collection of items
        - Items composed of data from: https://en.wikipedia.org/wiki/Pulitzer_Prize_for_Fiction
- Set-up Key Vault
    - Azure secrets
- Create GET request
    - Configured connection to database using key management
    - Wrote GET request to query the data in database
    - Wrote test script to validate application locally
- Deployed to Azure App Service
    - Pushed the code to Github
    - Set up the repository in Azure Devops
    - Cloned repo
    
