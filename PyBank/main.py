import csv
import os

csv_path = os.path.join("Resources","budget_data.csv")

#Declaring Variables to keep track of numbers during the for loop
totalProfit = 0
total_months = 0

past_month_profit = 0.0
monthly_change_list = []

greatest_monthly_increase = ["",0]
greatest_monthly_decrease = ["",0]
first_row = True

with open(csv_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")
        
    # saving the header row
    file_header = next(csv_reader)    
        
    #looping through remaining rows
    for row in csv_reader:
        monthly_change = 0
        # if statement to make so the first row is not added to the monthly change list, since there's no previous month to compare it to. 
        if first_row == False: 
            monthly_change = float(row[1]) - past_month_profit 
            monthly_change_list.append(monthly_change) 
        first_row = False
        
        
        #find greatest increase/decrease
        if monthly_change > greatest_monthly_increase[1]:
            greatest_monthly_increase[0] = row[0]
            greatest_monthly_increase[1] = monthly_change
            
        if monthly_change < greatest_monthly_decrease[1]:
            greatest_monthly_decrease[0] = row[0]
            greatest_monthly_decrease[1] = monthly_change    
        
        #adding monthly profit/loss to calculate total
        totalProfit += int(row[1])
        #counting months
        total_months += 1
        past_month_profit = float(row[1])
        

#calculating average monthly change        
average_change = round(sum(monthly_change_list) / len(monthly_change_list),2)       

#list with results
pybank_analysis = ["\nFinancial Analysis\n\n","----------------------------------","\n\n","Total months: ", str(total_months),"\n\n","Total: $",str(totalProfit),"\n\n","Average Change: $",str(average_change),"\n\n","Greatest increase in profits: ",greatest_monthly_increase[0]," ($",str(greatest_monthly_increase[1]),")","\n\n","Greatest decrease in profits: ",greatest_monthly_decrease[0]," ($",str(greatest_monthly_decrease[1]),")"]

# printing results
print("".join(pybank_analysis))

# writing text file
txt_path = os.path.join("analysis","results.txt")
with open(txt_path, "w") as f:
        f.writelines(pybank_analysis)