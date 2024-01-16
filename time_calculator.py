def add_time(start, duration, starting_day=None):

    new_time = ''
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    # Format starting time
    start_hour = int(start.split()[0].split(':')[0])
    start_minutes = int(start.split()[0].split(':')[1])
    period = start.split()[1]

    # Format duration
    duration_hour = int(duration.split(':')[0])
    duration_minutes = int(duration.split(':')[1])

    # New minutes and hours
    new_time_minutes = (start_minutes + duration_minutes) % 60
    if new_time_minutes in range(0, 10):
        new_time_minutes = '0'+str(new_time_minutes)
    surplus_hours = (start_minutes + duration_minutes) // 60
    new_time_hour = ((start_hour + duration_hour + surplus_hours) % 12)
    if new_time_hour == 0:
        new_time_hour = 12
    new_time += f'{new_time_hour}:{new_time_minutes}'

    # New time period
    time_period_change = (start_hour + duration_hour + surplus_hours) // 12
    new_period = period
    if time_period_change % 2 == 1:
        new_period = "PM" if period == "AM" else "AM"
    new_time += f' {new_period}'

    # Days elapsed
    days_elapsed = time_period_change // 2
    if period == 'PM' and time_period_change != 0:
        days_elapsed += 1

    # New day (optional)
    if starting_day:
        index = days.index(starting_day.capitalize())
        new_index = (index + days_elapsed) % 7
        new_time += f', {days[new_index]}'

    # Formatting days elapsed
    if days_elapsed == 1:
        new_time += f' (next day)'
    elif days_elapsed > 1:
        new_time += f' ({days_elapsed} days later)'

    return new_time


print(add_time("8:16 PM", "466:02", "tuesday"))

