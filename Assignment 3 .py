def print_dates_in_week_day(start_date, days):

    print(start_date, '\t', (start_date + 7), 
                  '\t', (start_date + 14), '\t', (start_date + 21), end = '')

    if((start_date + 28) <= days):
        print('\t', (start_date + 28), end = '')

 

def print_calendar_vertically(month, year):

    week_days = ["Sun","Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

    start_day_pos = date_to_week_day(1, month, year)

    days = days_in_month(month, year)

    for i in range(7):

        print(week_days[i], end='')
        print('\t', end = '')

        if(i < start_day_pos):

            print('\t', end = ' ')

            start_date_in_row = (7 - start_day_pos) + i + 1

        else:

            start_date_in_row = (i - start_day_pos) + 1

        print_dates_in_week_day(start_date_in_row, days)
        print("\n")