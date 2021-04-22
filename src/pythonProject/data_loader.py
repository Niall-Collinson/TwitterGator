#Importing packages
import json
from elasticsearch import Elasticsearch

def data_loader(size, query, time_request):
    """
    Getting data from elasticsearch with filtered queries, then loading it into a json file for the next operation
    :return:
    """

    #Converting user params to elasticsearch queries
    if time_request == "Last 15 minutes":
        time_request = "-15m"

    if time_request == "Last 30 minutes":
        time_request = "-30m"

    if time_request == "Last 6 hours":
        time_request = "-6h"

    if time_request == "Last day":
        time_request = "-1d"

    if time_request == "Last week":
        time_request = "-1w"

    if time_request == "Last month":
        time_request = "-1m"

    if time_request == "Last year":
        time_request = "-1y"

    print("The time request is:", time_request)

    #Establishing elasticsearch connection with server
    es_connection = Elasticsearch('http://twittergator-1791384971.eu-west-2.elb.amazonaws.com:9200')
    if es_connection.ping():
            print('Server connection successful')
    else:
        print('Failed to connect to server')

    if not query:

        #Query to pull relevant information from server
        query_body = {
            "query": {
                "filtered": {
                    "query": {"match_all": {}},
                    "filter": {
                        "range": {
                            "@timestamp": {
                                "gte": "now%s"%time_request,
                            }
                        }
                    }
                }
            },
            "sort": {
                "@timestamp": {
                    "order": "desc",
                    "ignore_unmapped": "true"
                }
            }
        }


    else:

        # Query to pull relevant information from server
        query_body = {
            "query": {
                "filtered": {
                    "query": {
                        "match": {
                            "text": {
                                "query": "%s" % query,
                                "operator": "or"
                            }
                        }
                    },
                    "filter": {
                        "range": {
                            "@timestamp": {
                                "gte": "now%s" % time_request,
                            }
                        }
                    }
                }
            },
            "sort": {
                "@timestamp": {
                    "order": "desc",
                    "ignore_unmapped": "true"
                }
            }
    }

    print("Size of query:", size)

    #Searching index with query and specified size
    result = es_connection.search(index="*", body=query_body, size=size)

    #Putting results in a array
    all_hits = result['hits']['hits']

    #Getting size of result
    print ("Size of ingested data:", len(result["hits"]["hits"]), "tweets")

    #Write data to json file
    with open('data.json', 'w') as json_file:
        json.dump(all_hits, json_file)