import os
import csv

budgetdata_csv = "Resources/budget_data.csv"
totalMonth = 0
totalProfit_Losses = 0
previousProfit_Losses = 0
Profit_Losses_change = 0
ProfitLoss_change_list = []
month_change = []
greatestIncrease = 0
greatestDecrease = 9999999999999999

with open(budgetdata_csv) as profit_lossData:
    reader = csv.DictReader(profit_lossData)

    index=0
    for row in reader:
        if(index==0):
            totalMonth+=1
            totalProfit_Losses = totalProfit_Losses + int(row["Profit/Losses"])
            previousProfit_Losses = int(row["Profit/Losses"])
            month_change = month_change + [row["Date"]]
            index+=1
            continue


        totalMonth = totalMonth + 1

        totalProfit_Losses = totalProfit_Losses + int(row["Profit/Losses"])
        Profit_Losses_change = int(row["Profit/Losses"]) - previousProfit_Losses
        ProfitLoss_change_list.append(Profit_Losses_change)
        previousProfit_Losses = int(row["Profit/Losses"])
        month_change = month_change + [row["Date"]]

    greatestDecrease=min(ProfitLoss_change_list)
    greatestIncrease=max(ProfitLoss_change_list)

    greatestDecrease_month=ProfitLoss_change_list.index(greatestDecrease)+1
    greatestIncrease_month=ProfitLoss_change_list.index(greatestIncrease)+1
    
    print("Financial Analysis")

    print(f"Total Months: {totalMonth}\n")

    print(f"Total Profit/Losess: ${totalProfit_Losses}\n")

    print(f"Average Change: ${round(sum(ProfitLoss_change_list)/len(ProfitLoss_change_list),2)}")

    print(f"Greatest increase in Profits: {month_change[greatestIncrease_month]} (${(str(greatestIncrease))})")

    print(f"Greatest decrease in Profits: {month_change[greatestDecrease_month]} (${(str(greatestDecrease))})")

