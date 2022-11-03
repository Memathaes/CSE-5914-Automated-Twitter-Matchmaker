from elasticsearch import Elasticsearch
import config

ELASTIC_PASSWORD = config.elastic_pass

es = Elasticsearch('https://localhost:9200')

