from pickle import STRING
from typing import Union
from neo4j import GraphDatabase
import os
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

class db:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()
        
    def insert_data(self, data):
        with self.driver.session() as session:
            for item in data:
                session.write_transaction(self._create_node, item)

    @staticmethod
    def _create_node(tx, item):
        tx.run("CREATE (:Node {name: $name, description: $description})", name=item['name'], description=item['description'])
        if item['parent']:
            tx.run("MERGE (parent:Node {name: $parent}) "
                "MERGE (child:Node {name: $name}) "
                "CREATE (parent)-[:HAS_CHILD]->(child)",
                parent=item['parent'], name=item['name'])
    @staticmethod
    def _return_data(tx):
        result = tx.run("MATCH (n:Node)-[:HAS_CHILD]->(parent:Node) RETURN n.name AS name, n.description AS description, parent.name AS parent")
        data = []
        for record in result:
            data.append({
                "name": record["name"],
                "description": record["description"],
                "parent": record["parent"]
            })
        return data


uri = os.getenv('NEO4J_URI')
user = os.getenv('USER_NAME')
password = os.getenv('PASSWORD')

obj = db(uri, user, password)

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
    obj.insert_data(initial_data['data'])
    return {"message": "Initial data loaded successfully"}

@app.get("/data")
def read_data():
    with obj.driver.session() as session:
        result = session.write_transaction(obj._return_data)
        data = [{"name": record["name"], "description": record["description"], "parent": record["parent"]} for record in result]
        return JSONResponse(content={"data": data})