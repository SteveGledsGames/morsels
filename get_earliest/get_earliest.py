# 16 September 2019 started. Next step: checkfor earliest date. next find pythonic way
def convert_to_date(datestring):
    day = int(datestring[3:5])
    month = int(datestring[:2])
    year = int(datestring[6:])
    return [month, day, year]
def get_earliest(datestring1, datesstring2):
    date1 = convert_to_date(datestring1)
    print(date1)


get_earliest("01/27/1832", "01/27/1756")
# "01/27/1756"
get_earliest("02/29/1972", "12/21/1946")
# "12/21/1946"
get_earliest("02/24/1946", "03/21/1946")
# "02/24/1946"
get_earliest("06/21/1958", "06/24/1958")
# "06/21/1958"