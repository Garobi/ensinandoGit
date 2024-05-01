import json

def escape_quotes(text):
    return text.replace('"', '\\"')

def generate_cypher_script(json_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    cypher_script = []

    for movie in data:
        movie_id = movie['id']
        title = movie['title']
        cast = movie['cast']

        # Create movie node
        cypher_script.append(f'CREATE (:Movie {{id: {movie_id}, title: "{title}"}})')

        # Create cast nodes and relationships
        for actor in cast:
            escaped_actor = escape_quotes(actor)
            cypher_script.append(f'MERGE (:Actor {{name: "{escaped_actor}"}})')
            cypher_script.append(f'WITH 1 AS _ MATCH (m:Movie {{id: {movie_id}}}), (a:Actor {{name: "{escaped_actor}"}}) CREATE (a)-[:ACTED_IN]->(m)')

    return '\n'.join(cypher_script)

# Example usage
json_file = 'latest_movies.json'
cypher_script = generate_cypher_script(json_file)

with open('output.cypher', 'w', encoding='utf-8') as f:
    f.write(cypher_script)

print("Cypher script generated successfully.")
