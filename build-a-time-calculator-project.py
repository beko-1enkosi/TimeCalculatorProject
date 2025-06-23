** start of main.py **

def add_time(start, duration, weekday=None):
# STEP 1: Pulling out the useful pieces from a string
    colon_index = start.index(':')
    space_index = start.index(' ')
    start_hour = int(start[:colon_index])
    start_minute = int(start[colon_index + 1:space_index])
    period = start[space_index + 1:]

    duration_hour, duration_minute = map(int, duration.split(':'))

# STEP 2: Convert start time to 24-hour format
    if period.upper() == 'PM' and start_hour != 12:
        start_hour += 12
    elif period.upper() == 'AM' and start_hour == 12:
        start_hour == 0

# STEP 3: Add duration
    end_minute = start_minute + duration_minute
    extra_hour = end_minute // 60
    end_minute = end_minute % 60

    end_hour = start_hour + duration_hour + extra_hour
    days_later = end_hour // 24
    end_hour = end_hour % 24

 # Step 4: Convert back to 12-hour format
    if end_hour == 0:
        final_hour = 12
        final_period = 'AM'
    elif end_hour < 12:
        final_hour = end_hour
        final_period = 'AM'
    elif end_hour == 12:
        final_hour = 12
        final_period = 'PM'
    else:
        final_hour = end_hour - 12
        final_period = 'PM'

# STEP 5: Handling weekdays
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    if weekday:
        index = weekdays.index(weekday.capitalize())
        new_index = (index + days_later) % 7
        new_weekday = weekdays[new_index]
    else:
        new_weekday = None
    
# STEP 6: Build result string
    new_time = f"{final_hour}:{end_minute:02} {final_period}"

    if new_weekday:
        new_time += f", {new_weekday}"

    if days_later == 1:
        new_time += " (next day)"
    elif days_later > 1:
        new_time += f" ({days_later} days later)"

    return new_time



** end of main.py **

