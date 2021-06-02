NUM_MONTHS = 12


def calculate_monthly_balance(balance, months, month, year, rate):
    for i in range(months):
        print(f"Year {year}, Month {month}, Balance: {balance}")
        balance += balance * rate
        month += 1
        if month > NUM_MONTHS:
            month = 1
            year += 1


def main():
    initial_balance = float(input("Initial balance: "))
    start_year = int(input("Start Year: "))
    start_month = int(input("Start Month: "))
    end_year = int(input("End Year: "))
    end_month = int(input("End Month: "))
    number_of_months = (NUM_MONTHS - start_month + 1) + end_month + (end_year - start_year - 1) * NUM_MONTHS
    initial_rate = float(input("Enter initial rate: "))

    while initial_rate != 0:
        calculate_monthly_balance(initial_balance, number_of_months, start_month, start_year, initial_rate)
        initial_rate = float(input("Enter initial rate: "))


if __name__ == '__main__':
    main()
