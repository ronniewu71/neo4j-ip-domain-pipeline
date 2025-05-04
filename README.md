# Neo4j IP-Domain Pipeline

This project demonstrates a microservices architecture for ingesting, deduplicating, and storing suspicious IP-domain relationships in Neo4j, and visualizing/querying them via a React D3.js frontend.

## Services

- **ingestion**: Fetches and cleans data from sources.
- **dedup**: Generates SHA256 fingerprints and removes duplicates.
- **writer**: Writes nodes and relationships into Neo4j.
- **query-api**: Provides RESTful endpoints to query the graph.
- **frontend**: Visualizes the graph with React and D3.js.

## Setup

1. Build and start all services:
   ```bash
   docker-compose up --build
   ```
2. Access Neo4j browser at http://localhost:7474
3. Access frontend at http://localhost:3000
4. Access API at http://localhost:5000

