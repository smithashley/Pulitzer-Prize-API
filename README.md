# Pulitzer Prize API

## Objective
Create an API that retrieves the year, author, and title for Pulitzer 
Prize winners of fiction, then deployed the application to Azure.

Application is live here: https://pulitzerprizeforfiction.azurewebsites.net/api/data
## Tools
- Python
- Flask
- Git  
- Azure 
## Steps
- Created NoSQL database
    - In Azure portal, created Cosmos DB account
    - In Cosmos DB account, created database
    - Created a container that holds the collection of items
        - Items composed of data from: https://en.wikipedia.org/wiki/Pulitzer_Prize_for_Fiction
- Set-up key management
    - Configured the Key Vault
    - Created a new secret that contains the read-only key to the database
- Create GET request
    - Configured connection to database using key management
    - Wrote GET request to query the data in database
    - Wrote test script to validate application locally
- Deployed to Azure App Service
    - Created requirements.txt file to import modules needed for the application
    - Pushed the code to Github
    - Configured the CI/CD pipeline with Github Actions
    - After the deployment was successful the application went live
