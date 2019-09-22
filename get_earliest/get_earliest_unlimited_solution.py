def get_earliest(*dates):
    """Return earliest of given MM/DD/YYYY-formatted date strings."""
    def date_key(date):
        (m, d, y) = date.split('/')
        return (y, m, d)
    return min(dates, key=date_key)

'''
Our key function tells the min function what criteria we'd like to use for determining whether one date string is less than (earlier than) another one. 
The key function will be called with each date string and the returned date string will be the one with the resulting key tuple which is smallest. 
If you're not familiar with that * operator, the min built-in, or the optional key argument you can provide to min, 
you might want to look these things up to use in the future!
'''