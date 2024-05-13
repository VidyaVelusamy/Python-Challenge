import os
import csv
import datetime

Budget_data = os.path.join("C:/Users/vidya/pythonassignment/Python-Challenge/PyBank/","Resources","budget_data.csv")
print ("Financial Analysis")
print("----------------------------")
with open(Budget_data) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    # @NOTE: This time, we do not use `next(csv_reader)` because there is no header for this file
    count =0
    Total=0
    Change = 0
    change_count=0
    Total_Change = 0
    Period =[]
    Profit_loss =[]
    previous_change =0
    hidden=0
    maxperiod=""
    minperiod=""
    min=0
    max=0
    # Read through each row of data after the header
    csv_reader.__next__()
    for row in csv_reader:
       Period.append(row[0])
       Profit_loss.append(row[1])
    
    for  i in range(len(Period)):
           count = count + 1 
           Total = int(Profit_loss[i]) + Total
          
    for j in range(1, len(Profit_loss)):        
        change_count = change_count + 1
        Change = int(Profit_loss[j])-int(Profit_loss[j-1])
        Total_Change = Change + Total_Change
        if Change > previous_change and max <Change:
            max = Change
            greatest_increase=[f"{Change}"]
            maxperiod = Period[j]
        elif previous_change> Change and max< previous_change:
            max = previous_change
            greatest_increase=[f"{previous_change}"]
            maxperiod = Period[j]
        else:
            max = max
            greatest_increase=[f"{max}"]
            maxperiod = maxperiod
        if Change < previous_change and min >Change:
            min = Change
            greatest_decrease=[f"{Change}"]
            minperiod = Period[j]
        elif previous_change< Change and min >Change:
            min = previous_change
            greatest_decrease=[f"{previous_change}"]
            minperiod = Period[j]
        else:
            min = min
            greatest_decrease=[f"{min}"]
            minperiod = minperiod
        previous_change = Change    
        
    if count>0:
        Average_change =  Total_Change / change_count
        Average_change = round(Average_change,2)
    else:
        Average_change=0
    print(f"Total Months:{count}")
    print(f"Total:${Total}")

    print(f"Average Change:${Average_change}")
    print(f"Greatest increase in Profits: {maxperiod} ${greatest_increase[0]}")
    print(f"Greatest decrease in Profits: {minperiod} ${greatest_decrease[0]}")
output_path = os.path.join("C:/Users/vidya/pythonassignment/Python-Challenge/PyBank", "Analysis", "Budget_data_results.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, "w") as file:
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months:{count}\n")
    file.write(f"Total:${Total}\n")

    file.write(f"Average Change:${Average_change}\n")
    file.write(f"Greatest increase in Profits: {maxperiod} (${greatest_increase[0]})\n")
    file.write(f"Greatest decrease in Profits: {minperiod} (${greatest_decrease[0]})\n")