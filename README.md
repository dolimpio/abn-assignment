# ABN-Assignment

## Prerequisites

Have docker installed on your PC.

## Usage
```bash
cd ABN
docker compose up
```

Because the process of loading data into Neo4j was out of the scope of the assignment, I decided to create an endpoint that writes the data into the database.

To load this data go to:
 
    http://localhost:8000/docs  

And execute the endpoint __/load_data__

## Front-end usage
```bash
cd abn-assignment
npm install
npm run format
npm run dev
```

