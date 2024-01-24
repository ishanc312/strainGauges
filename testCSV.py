import csv

x_temp = [1, 2, 3, 4, 5, 6, 7, 8]
y_temp = [2, 3, 4, 5, 6, 7, 8, 9]

# simple example that displays functionality of writing data to a CSV file
with open('test.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["X Values", "Y Values"])
    for x, y in zip(x_temp, y_temp):
        writer.writerow([x, y])
# note we can later import a CSV file into Google Sheets