import csv
import json

def json_to_csv(json_data):
    # Define the fieldnames for the movie CSV
    movie_fieldnames = ['id', 'title']
    # Define the fieldnames for the actor CSV
    actor_fieldnames = ['actor_id', 'actor_name', 'movie_title']

    # Initialize actor ID counter
    actor_id_counter = 1

    # Create CSV files for movies and actors
    with open('movies.csv', 'w', newline='') as movie_csvfile, \
            open('actors.csv', 'w', newline='') as actor_csvfile:
        movie_writer = csv.DictWriter(movie_csvfile, fieldnames=movie_fieldnames)
        actor_writer = csv.DictWriter(actor_csvfile, fieldnames=actor_fieldnames)
        movie_writer.writeheader()
        actor_writer.writeheader()

        for movie in json_data:
            # Write movie to movie CSV
            movie_writer.writerow({'id': movie['id'], 'title': movie['title']})
            # Write actors to actor CSV
            for actor_name in movie['cast']:
                actor_writer.writerow({'actor_id': actor_id_counter, 'actor_name': actor_name, 'movie_title': movie['title']})
                actor_id_counter += 1

if __name__ == "__main__":
    # Read JSON data from file
    with open('movies.json', 'r') as json_file:
        json_data = json.load(json_file)

    json_to_csv(json_data)
