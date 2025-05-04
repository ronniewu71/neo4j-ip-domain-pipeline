from flask import Flask
app = Flask(__name__)

@app.route('/dedup')
def dedup():
    return "Deduplication service placeholder"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8002)
