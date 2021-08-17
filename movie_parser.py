import csv

input_file = open("movies.csv","r", newline='')
myreader = csv.reader(input_file)
header = next(myreader)
data = [row for row in myreader]
input_file.close()
output_file = open("movies_update.csv","w")
mywriter = csv.writer(output_file)
#creates header for my file
mywriter.writerow(header+["genre_count"])

for row in data:
  genres_count = len(row[2].split("|"))
  mywriter.writerow([row[0],row[1],row[2],genres_count])

output_file.close()

output_file = open("movies_updated.csv","r", newline='')
output_reader = csv.reader(output_file)
output_header = next(output_reader)
output_data = [row for row in output_reader]
num_rows = len(output_data)

if __name__ == "__main__":
    print(f"Data fields: {output_header}")
    print(f"Number Of Records: {num_rows}")
    print("\n First 10 Movies listed")
    for i in range(0,10):
        print(output_data[i])
    print("\n Last 10 Movies listed")
    for i in range(len(output_data)-10,len(output_data)):
        print(output_data[i])