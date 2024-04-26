'''
Sort a list of dates in ascending order given the
data format shown below:

Each date is in the form dd mmm yyyywhere:
• dd is in the Set {0-31}
• mmm is in the set {Jan, Feb, Mar, Apr, May, Jun, Jul,
Aug, Sep, Oct, NOV, Dec}
• yyyy is four digits

Example
dates = ['01 Mar 2017','03 Feb 2017', '15 Jan 1998']

The array dates sorts to ['15 Jan 1998', '03 Feb
2017', '01 Mar 2017'].

Function Description
Complete the function sortDates in the editor
below.
'''
# solution:

from datetime import datetime

def sortDates(dates):
    # Define a custom function to parse the date strings
    def custom_date_parser(date_str):
        return datetime.strptime(date_str, '%d %b %Y')

    # Parse the dates into datetime objects using the custom parser
    parsed_dates = [custom_date_parser(date) for date in dates]

    # Sort the parsed dates
    sorted_dates = sorted(parsed_dates)

    # Convert the sorted dates back to the desired format
    sorted_dates_str = [date.strftime('%d %b %Y') for date in sorted_dates]

    return sorted_dates_str

# Example usage
dates = ['01 Mar 2017', '03 Feb 2017', '15 Jan 1998']
sorted_dates = sortDates(dates)
print(sorted_dates)


# optimize solution:

from datetime import datetime

def sortDates(dates):
    # Sort the dates using a lambda function to parse the date strings
    sorted_dates = sorted(dates, key=lambda x: datetime.strptime(x, '%d %b %Y'))
    
    return sorted_dates

# Example usage
dates = ['01 Mar 2017', '03 Feb 2017', '15 Jan 1998']
sorted_dates = sortDates(dates)
print(sorted_dates)

