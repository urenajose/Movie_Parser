import csv

# simply a short list of movies from the movielens dataset
input_file = open("movies.csv", "r", newline='', encoding="utf-8")
myreader = csv.reader(input_file)
# field names from file header
header = next(myreader)
# list of rows from file
data = [row for row in myreader]
input_file.close()

output_file = open("movies_updated.csv", "w", newline='')
mywriter = csv.writer(output_file)

# creates fields header for the new output file
# adds 'genre_count' field to previous 3 fields: movieId, title, and genres
mywriter.writerow(header+["genre_count"])

# running sum of genres count
genres_counter = 0
# dictionary to hold count of movie genres
genres_dict = {}
# number of movies with no genres listed
no_genre = 0
for row in data:
    # if there is no genres listed for the movie returns 0 for genres_count
    if row[2] == "(no genres listed)":
        genres_count = 0
        no_genre += 1
    else:
        # list of genres of each movie
        g_list = row[2].split("|")
        for i in g_list:
            if i in genres_dict:
                genres_dict[i] += 1
            else:
                genres_dict[i] = 1
        # count of genre per movie
        genres_count = len(g_list)
        genres_counter += genres_count
    mywriter.writerow([row[0], row[1], row[2], genres_count])

# returns most common genre
max_genre = max(genres_dict, key=genres_dict.get)
# returns least common genre
min_genre = min(genres_dict, key=genres_dict.get)
output_file.close()

# reads updated csv file
output_file = open("movies_updated.csv", "r", newline='')
output_reader = csv.reader(output_file)
output_header = next(output_reader)
output_data = [row for row in output_reader]

# number of rows in the dataset
num_rows = len(output_data)
# Average number of genres
average_genres = round(genres_counter/num_rows, 2)

if __name__ == "__main__":
    print(f"Data fields: {output_header}")
    print(f"Number Of Records: {num_rows}")
    print(f"The average number of genres per movie: {average_genres}")
    print(f"Most common genre in this dataset: {max_genre}")
    print(f"Least common genre in this dataset: {min_genre}")
    print(f"Number of movies with no genre listed: {no_genre}")
    print("\n First 10 Movies listed")
    for i in range(0, 10):
        print(output_data[i])
    print("\n Last 10 Movies listed")
    for i in range(len(output_data)-10, len(output_data)):
        print(output_data[i])
