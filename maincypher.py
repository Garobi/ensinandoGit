from neo4j import GraphDatabase
import time

# Function to execute Cypher query
def execute_query(uri, username, password, query):
    # Connect to the Neo4j database
    with GraphDatabase.driver(uri, auth=(username, password)) as driver:
        # Start a session
        with driver.session() as session:
            # Run the Cypher query
            start_time = time.time()
            result = session.run(query)
            records = list(result)  # Convert result to list to consume it immediately
            end_time = time.time()
            execution_time = end_time - start_time
            return records, execution_time

# Function to read and execute Cypher queries from file in batches
def execute_queries_from_file(uri, username, password, file_path, batch_size=500):
    # Open the file and read Cypher queries line by line
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        total_lines = len(lines)
        for i in range(0, total_lines, batch_size):
            batch_lines = lines[i:i + batch_size]
            print(f"Executing batch {i//batch_size + 1} of {total_lines//batch_size + 1}")
            batch_queries = [line.strip() for line in batch_lines]
            batch_query = "\n".join(batch_queries)
            # Execute the current batch of Cypher queries
            records, _ = execute_query(uri, username, password, batch_query)
            # Process the records if needed
            for record in records:
                print(record)

# Define the URI, username, and password for your Neo4j database
uri = "neo4j://localhost:7687"
username = "neo4j"
password = "12345678"  # Replace 'your_password' with your actual password

# Path to the file containing Cypher queries
cypher_query_file = "output.cypher"

# Execute Cypher queries from file in batches
execute_queries_from_file(uri, username, password, cypher_query_file)
