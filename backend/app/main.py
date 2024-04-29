from pickle import STRING
from typing import Union
from pydantic import BaseModel
from neo4j import GraphDatabase
import os
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
data_loaded = False

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

class db:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()
        
    def insert_data(self, data):
        with self.driver.session() as session:
            for item in data:
                session.write_transaction(self._create_node, item)
                
    def insert_relationships(self, data):
        with self.driver.session() as session:
            for item in data:
                session.write_transaction(self._create_relationship, item)
    
    @staticmethod
    def _create_node(tx, item):
        tx.run("CREATE (:Node {name: $name, description: $description, parent: $parent})", name=item['name'], description=item['description'], parent=item['parent'])
        print("Node inserted: " + str(item))
   
    @staticmethod
    def _create_relationship(tx, item): 
        if item['parent']:
            tx.run("MATCH (parent:Node {name: $parent}), (child:Node {name: $name}) "
                   "CREATE (child)-[:child_of]->(parent)",
                   parent=item['parent'], name=item['name'])
            print("Relationship create: Parent: " + item['parent'] + " of child: " + item['name'])


    @staticmethod
    def _return_data(tx):
        result = tx.run("MATCH (n:Node) RETURN n.name AS name, n.description AS description, n.parent AS parent")
        data = [{"name": record["name"], "description": record["description"], "parent": record["parent"]} for record in result]
        return {"data": data}

uri = os.getenv('NEO4J_URI')
user = os.getenv('USER_NAME')
password = os.getenv('PASSWORD')

database = db(uri, user, password)

# Endpoint for debbuging purposes
@app.get("/")
def read_root():
    return {"Hello": "World"}

# Endpoint to load initial data into Neo4j
@app.post("/load_data")
def load_initial_data():
    initial_data = {
        "data": [
            {"name": "A", "description": "This is a description of A", "parent": ""},
            {"name": "B", "description": "This is a description of B", "parent": "A"},
            {"name": "C", "description": "This is a description of C", "parent": "A"},
            {"name": "D", "description": "This is a description of D", "parent": "A"},
            {"name": "B-1", "description": "This is a description of B-1", "parent": "B"},
            {"name": "B-2", "description": "This is a description of B-2", "parent": "B"},
            {"name": "B-3", "description": "This is a description of B-3", "parent": "B"}
        ]
    }
    database.insert_data(initial_data['data'])
    database.insert_relationships(initial_data['data'])
    return {"message": "Initial data loaded successfully"}

# Retrieves data
@app.get("/data")
def read_data():
    with database.driver.session() as session:
        result = session.read_transaction(database._return_data)
        return JSONResponse(result)



    