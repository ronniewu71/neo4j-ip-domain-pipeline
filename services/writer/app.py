from flask import Flask
from neo4j import GraphDatabase

app = Flask(__name__)
driver = GraphDatabase.driver("bolt://neo4j:7687", auth=("neo4j", "test"))

@app.route('/write')
def write():
    with driver.session() as session:
        session.run("RETURN 1")
    return "Writer service placeholder"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8003)
