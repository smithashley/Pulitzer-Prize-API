import azure.cosmos.cosmos_client as cosmos_client
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from flask import Flask
import json

app = Flask(__name__)
Api=app
app.config['TESTING'] = True

#Set up Azure Key Vault
credential = DefaultAzureCredential()
secret_client = SecretClient(vault_url="https://accountkey.vault.azure.net/", credential=credential)
secret = secret_client.get_secret("acctkey")

# Set up connection to Cosmos DB
url = 'https://ppapidb.documents.azure.com:443/'
client = cosmos_client.CosmosClient(url, credential=secret.value)
database_name = 'ppapidb'
database = client.get_database_client(database_name)
container_name = 'ppdata'
container = database.get_container_client(container_name)

@app.route('/api/data')
def get_data():
    items=list(container.query_items(
    query='SELECT c.Year, c.Title, c.Author FROM c',
    enable_cross_partition_query=True))
    return json.dumps(items)

if __name__== '__main__':
    app.run(debug=True)

