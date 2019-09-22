# 16 September 2019 success for first part now working on bonus.
# using *args I get it to work but code is clumsy
def convert_to_date(datestring):
    day = int(datestring[3:5])
    month = int(datestring[:2])
    year = int(datestring[6:])
    return month, day, year


def find_earliest(earlymonth, earlyday, earlyyear, newmonth, newday, newyear):
    earliestdate = "early"
    if newyear < earlyyear:
        earliestdate = "new"
    elif newyear == earlyyear:
        if newmonth < earlymonth:
            earliestdate = "new"
        elif newmonth == earlymonth:
            if newday < earlyday:
                earliestdate = "new"
    if earliestdate == "new":
        return newmonth, newday, newyear
    else:
        return earlymonth, earlyday, earlyyear

    

def get_earliest(datestring, *args):
    # month1, day1, year1 = convert_to_date(datestring1)
    # month2, day2, year2 = convert_to_date(datestring2)
    earlymonth, earlyday, earlyyear = convert_to_date(datestring)
    # print(earlymonth, earlyday, earlyyear)
    if args:
        for date in args:
            newmonth, newday, newyear = convert_to_date(date)
            earlymonth, earlyday, earlyyear = find_earliest(earlymonth, earlyday, earlyyear, newmonth, newday, newyear)

    return str(earlymonth).zfill(2) + "/" + str(earlyday).zfill(2) + "/" + str(earlyyear)

print(get_earliest("02/24/1946", "01/29/1946", "03/29/1945"))
# "01/29.1946"
print(get_earliest("02/24/1946", "01/29/1946", "03/29/1945", "01/27/1832", "01/27/1756"))
# # "01/27/1756"
print(get_earliest("02/29/1972", "12/21/1946"))
# # "12/21/1946"
print(get_earliest("02/24/1946", "03/21/1946"))
# # "02/24/1946"
print(get_earliest("06/21/1958", "06/24/1958"))
# # "06/21/1958"

