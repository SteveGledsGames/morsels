# 16 September 2019 started. next find pythonic way
def convert_to_date(datestring):
    day = int(datestring[3:5])
    month = int(datestring[:2])
    year = int(datestring[6:])
    return month, day, year
def get_earliest(datestring1, datestring2):
    month1, day1, year1 = convert_to_date(datestring1)
    month2, day2, year2 = convert_to_date(datestring2)
    print(month1, day1, year1)
    print(month2, day2, year2)
    if year1 < year2:
        return datestring1
    elif year1 == year2:
        if month1 < month2 : 
            return datestring1
        elif month1 == month2 :
            if day1 < day2 :
                return datestring1    
        return datestring2
    return datestring2


print(get_earliest("01/27/1832", "01/27/1756"))
# "01/27/1756"
print(get_earliest("02/29/1972", "12/21/1946"))
# "12/21/1946"
print(get_earliest("02/24/1946", "03/21/1946"))
# "02/24/1946"
print(get_earliest("06/21/1958", "06/24/1958"))
# "06/21/1958"

