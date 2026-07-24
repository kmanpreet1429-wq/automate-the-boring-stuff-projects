
import re
dateDetection = re.compile(r''' 
                           ([0][1-9]|[12][0-9]|[3][01])
                           /
                           ([0][1-9]|[1][0-2])
                           /
                           ([12][0-9]{3})                           
                           ''',re.VERBOSE)

text = input('Enter a date (dd/mm/yy):')
match = dateDetection.search(text)

if match:
    day = int(match.group(1))
    month = int(match.group(2))
    year = int(match.group(3))

    print('Day:' ,day)
    print('Month:' ,month)
    print('Year:' , year)

    if month in (4,6,9,11):
        if day <= 30:
            print('Valid Date')
        else:
            print('Invalid Date')

    elif month == 2:
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            if day <= 29:
                print('Valid Date')
            else:
                print('Invalid Date')
        else:
            if day <= 28:
                print('Valid Date')
            else:
                print('Invalid Date')

    else:
        print('Valid Date')
else:
    print('Invalid Format')
            


    
