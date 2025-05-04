from flask import Flask
app = Flask(__name__)

@app.route('/ingest')
def ingest():
    return "Ingestion service placeholder"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8001)
