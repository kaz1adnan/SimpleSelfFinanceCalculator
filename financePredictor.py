import sys
from sys import intern


def calculateWealthByYear(currentWealth, rateOfReturn, monthlySavings, years):
    totalSavings = currentWealth

    for year in range(1, years+1):
        interest = totalSavings * (rateOfReturn/100)
        totalSavings += interest + (monthlySavings*12)
        print(f"Year {year}: Total wealth = {totalSavings:.2f}")

    return 0

def calculateYearsTillFreedom(currentWealth, rateOfReturn, monthlySavings, targetWealth):
    totalSavings = currentWealth
    years2freedom = 0

    while True:
        years2freedom += 1
        interest = totalSavings * (rateOfReturn/100)
        totalSavings += interest + (monthlySavings*12)
        if totalSavings > targetWealth:
            print(f"You will reach financial freedom in {years2freedom} years! Keep Grinding!!")
            return 0

def main():
    prog = input("Which program would you like to run? Type 'returns' or 'freedom' ")

    try:
        currentWealth = float(input("Enter your current wealth: "))
        rateOfReturn = float(input("Enter estimated rate of return (%): "))
        monthlySavings = float(input("Enter how much you can save per month: "))

    except ValueError:
        print("Invalid input. You must only enter numbers, fuckin' idiot")
        sys.exit()

    if prog == 'returns':
        years = int(input("Enter investment period in years: "))
        calculateWealthByYear(currentWealth, rateOfreturn, monthlySavings, years)

    elif prog == 'freedom':
        try:
            targetWealth = float(input("How much money do you need to be financially free? "))
            calculateYearsTillFreedom(currentWealth, rateOfReturn, monthlySavings, targetWealth)

        except ValueError:
            print("Invalid input. You must only enter numbers, fuckin' idiot")
            sys.exit()
    else:
        print("Invalid input. Type 'returns' or 'freedom'")

main()
