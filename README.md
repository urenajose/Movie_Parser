![movie_parser.py]

[movie_parser.py]: images/movie_parser.py.gif

# Movie Parser
## Python 3 script that takes a list of movies from the movielens dataset and 
1. Reads in the file named movies.csv
    > Each row contains 3 fields: movieId, title, and genres
2. Writes a new file named movies. with the exact same fields plus 1 additional field called `genre_count`
3. Prints out Count how many genres each movie has
4. Prints out the average number of genres per movie
5. Prints out the most common genre in this dataset
6. Prints out the least common genre in this dataset
7. Prints out Number of movies with no genre listed
8. Prints out First 10 Movies listed in dataset
9. Prints out Last 10 Movies listed in dataset


![git clone] clone repo

[git clone]: images/gitclone1.gif

## Installation
1. Open windows powershell, cmd or linux terminal
    > ensure python path is in system environment variable
2. Clone repo to your local computer
   ```
   git clone https://github.com/urenajose/Movie_Parser.git
   ```

3. Inside terminal navigate to repo folder where movie_parser.py is located

4. Run the movie_parser.py file by typing or copying following command line:
```
py movie_parser.py 
```
**Script should return**
```
Data fields: ['movieId', 'title', 'genres', 'genre_count']
Number Of Records: 9742
The average number of genres per movie: 2.26
Most common genre in this dataset: Drama
Least common genre in this dataset: Film-Noir
Number of movies with no genre listed: 34

 First 10 Movies listed
['1', 'Toy Story (1995)', 'Adventure|Animation|Children|Comedy|Fantasy', '5']
['2', 'Jumanji (1995)', 'Adventure|Children|Fantasy', '3']
['3', 'Grumpier Old Men (1995)', 'Comedy|Romance', '2']
['4', 'Waiting to Exhale (1995)', 'Comedy|Drama|Romance', '3']
['5', 'Father of the Bride Part II (1995)', 'Comedy', '1']
['6', 'Heat (1995)', 'Action|Crime|Thriller', '3']
['7', 'Sabrina (1995)', 'Comedy|Romance', '2']
['8', 'Tom and Huck (1995)', 'Adventure|Children', '2']
['9', 'Sudden Death (1995)', 'Action', '1']
['10', 'GoldenEye (1995)', 'Action|Adventure|Thriller', '3']

 Last 10 Movies listed
['193565', 'Gintama: The Movie (2010)', 'Action|Animation|Comedy|Sci-Fi', '4']
['193567', 'anohana: The Flower We Saw That Day - The Movie (2013)', 'Animation|Drama', '2']
['193571', 'Silver Spoon (2014)', 'Comedy|Drama', '2']
['193573', 'Love Live! The School Idol Movie (2015)', 'Animation', '1']
['193579', 'Jon Stewart Has Left the Building (2015)', 'Documentary', '1']
['193581', 'Black Butler: Book of the Atlantic (2017)', 'Action|Animation|Comedy|Fantasy', '4']
['193583', 'No Game No Life: Zero (2017)', 'Animation|Comedy|Fantasy', '3']
['193585', 'Flint (2017)', 'Drama', '1']
['193587', 'Bungo Stray Dogs: Dead Apple (2018)', 'Action|Animation', '2']
['193609', 'Andrew Dice Clay: Dice Rules (1991)', 'Comedy', '1']
(Movie_Parser-RpuSP3F5) root@Jose-PC:/mnt/z/DataScience/Job_Hunt_code_challenge/Movie_Parser# /root/.virtualenvs/Movie_Parser-RpuSP3F5/bin/python /mnt/z/DataScience/Job_Hunt_code_challenge/Movie_Parser/movie_parser.py
Data fields: ['movieId', 'title', 'genres', 'genre_count']
Number Of Records: 9742
The average number of genres per movie: 2.26
Most common genre in this dataset: Drama
Least common genre in this dataset: Film-Noir
Number of movies with no genre listed: 34

 First 10 Movies listed
['1', 'Toy Story (1995)', 'Adventure|Animation|Children|Comedy|Fantasy', '5']
['2', 'Jumanji (1995)', 'Adventure|Children|Fantasy', '3']
['3', 'Grumpier Old Men (1995)', 'Comedy|Romance', '2']
['4', 'Waiting to Exhale (1995)', 'Comedy|Drama|Romance', '3']
['5', 'Father of the Bride Part II (1995)', 'Comedy', '1']
['6', 'Heat (1995)', 'Action|Crime|Thriller', '3']
['7', 'Sabrina (1995)', 'Comedy|Romance', '2']
['8', 'Tom and Huck (1995)', 'Adventure|Children', '2']
['9', 'Sudden Death (1995)', 'Action', '1']
['10', 'GoldenEye (1995)', 'Action|Adventure|Thriller', '3']

 Last 10 Movies listed
['193565', 'Gintama: The Movie (2010)', 'Action|Animation|Comedy|Sci-Fi', '4']
['193567', 'anohana: The Flower We Saw That Day - The Movie (2013)', 'Animation|Drama', '2']
['193571', 'Silver Spoon (2014)', 'Comedy|Drama', '2']
['193573', 'Love Live! The School Idol Movie (2015)', 'Animation', '1']
['193579', 'Jon Stewart Has Left the Building (2015)', 'Documentary', '1']
['193581', 'Black Butler: Book of the Atlantic (2017)', 'Action|Animation|Comedy|Fantasy', '4']
['193583', 'No Game No Life: Zero (2017)', 'Animation|Comedy|Fantasy', '3']
['193585', 'Flint (2017)', 'Drama', '1']
['193587', 'Bungo Stray Dogs: Dead Apple (2018)', 'Action|Animation', '2']
['193609', 'Andrew Dice Clay: Dice Rules (1991)', 'Comedy', '1']
```
