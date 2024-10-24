def convert_to_ywd_format(d):

    DAYS_IN_YEAR = 365
    DAYS_IN_WEEK = 7

    years = d // DAYS_IN_YEAR
    d = d % DAYS_IN_YEAR
    weeks = d // DAYS_IN_WEEK
    d = d % DAYS_IN_WEEK

    # is it possible to return multiple values
    return years, weeks, d


d = int(input("Insert the number of days : "))
if d < 0:
    print("ERROR : the number of days must be non-negative!")
else:
    years, weeks, days = convert_to_ywd_format(d)
    print(d, "days =", years, "years +", weeks, "weeks +", days, "days")