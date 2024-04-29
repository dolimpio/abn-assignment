# ABN-Assignment

## Prerequisites

Have docker installed on your PC.

## Usage
```bash
cd ABN
docker compose up
```
Wait for it to complete :)
> [!IMPORTANT] 
### __The frontend should be empty.__

As loading data into Neo4j was beyond the scope of this assignment, I've provided an endpoint to populate the database.

To load the data, visit http://localhost:8000/docs and execute the endpoint __/load_data__ by clicking on __Try it out__ and then __Execute__. Alternatively, you can use the following command in your terminal:
```bash
curl -X 'POST' \
  'http://localhost:8000/load_data' \
  -H 'accept: application/json' \
  -d ''
```

After doing this the data should appear instantly on the frontend.

> [!CAUTION]
If you execute the endpoint/command more than once the data will be duplicate.

> [!NOTE] 
If you want to restart everything from scratch, don't forget to delete the contents of database/data and database/logs.

If you have any doubts or inquiries please don't doub contacting me by email or LinkedIn:
[LinkedIn](https://www.linkedin.com/in/david-olimpio-silva/)


