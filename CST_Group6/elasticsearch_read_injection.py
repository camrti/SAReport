from elasticsearch import Elasticsearch
import urllib3
from person import Person

# Suppress only the single InsecureRequestWarning from urllib3 needed to handle self-signed certificates
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Connect to the local Elasticsearch instance
# , api_key="SXBOa2pKQUJDbFcxV0l4VzFBLW06SmZGeG1Uc05RMUthRkh6VzA3ekpBQQ=="
es = Elasticsearch("https://elastic:Elastic2024@localhost:9200", verify_certs=False)   # default port for elasticsearch

if es.ping():
    print("Connected to Elasticsearch.")
else:
    print("Failed to connect to Elasticsearch.")

# Define a query to match all documents
query = {
    "query": {
        "match_all": {}
    }
}

try:
    response = es.search(index="users_context_attributes", body=query)

    # Saving the response in a dictionary
    data = {}
    for hit in response['hits']['hits']:
        # print(hit['_source'], type(hit['_source']))
        data[hit['_source']['user']] = hit['_source']
        # print(data[hit['_source']['user']])
    
    # Iterating over dictionary keys to get the user engagement level
    for user in data.keys():
        # calling the cst function
        # print(type(data[user]['user']))
        person = Person(data[user]['user'], data[user]['session_lenght'], 
                      data[user]['forum_question'], data[user]['not_answered'], 
                      data[user]['material'])
        
        engagement_level = person.get_dashboard_mapped_engagement_level()
        # print(engagement_level)

        # injecting the result of the cst function into elasticsearch
        es.index(
            index='users_engagement_level',
            document={
                'user': user,
                'engagement_level': engagement_level
            }
        )

    es.indices.refresh(index='')

except Exception as e:
    print(f"An error occurred: {e}")
