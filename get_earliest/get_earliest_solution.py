def get_earliest(date1, date2):
    """Return earliest of two MM/DD/YYYY-formatted date strings."""
    m1, d1, y1 = date1.split('/')
    m2, d2, y2 = date2.split('/')
    if (y1, m1, d1) < (y2, m2, d2):
        return date1
    else:
        return date2