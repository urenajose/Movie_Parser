import csv

input_file = open("movies.csv", newline='')
myreader = csv.reader(input_file)
header = next(myreader)
data = [row for row in myreader]
num_rows = len(data)
output_file = open("movies_update.csv","w")
mywriter = csv.writer(output_file)
#creates header for my file
mywriter.writerow(header+["genre_count"])

for row in data:
  genres_count = len(row[2].split("|"))
  mywriter.writerow([row[0],row[1],row[2],genres_count])

output_file = open("movies_update.csv", newline='')
output_reader = csv.reader(output_file)
output_header = next(output_reader)
output_data = [row for row in output_reader]

if __name__ == "__main__":
    print(f"Original Header: {header}")
    print(f"Number Of Records: {num_rows}")
    print("\n First 10 Movies listed")
    for i in range(0,10):
        print(data[i])
    print("\n Last 10 Movies listed")
    for i in range(len(data)-10,len(data)):
        print(data[i])
        