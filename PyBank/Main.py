import os
import csv

Budget_data = os.path.join("..", "Resources", "budget_data.csv")

with open(Budget_data) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    # @NOTE: This time, we do not use `next(csv_reader)` because there is no header for this file

    # Read through each row of data after the header
    for row in csv_reader:

        # Convert row to float and compare to grams of fiber
      
            print(len(row))