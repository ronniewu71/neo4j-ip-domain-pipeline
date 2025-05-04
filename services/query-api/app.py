from flask import Flask, jsonify
from neo4j import GraphDatabase

app = Flask(__name__)
driver = GraphDatabase.driver("bolt://neo4j:7687", auth=("neo4j", "test"))

@app.route('/graph')
def graph():
    result = driver.session().run("MATCH (n)-[r]->(m) RETURN n, r, m LIMIT 5")
    data = []
    for record in result:
        data.append({
            'n': dict(record['n']),
            'r': type(record['r']).__name__,
            'm': dict(record['m'])
        })
    return jsonify(data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
