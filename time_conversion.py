def time_conversion(time_with_period):
    time = time_with_period[:8]
    period = time_with_period[8:]
    hour = int(time[:2])
    if period == "PM" and hour < 12:
        hour += 12
        return f"{hour}:{time[3:5]}:{time[6:8]}"
    if period == "AM" and hour >= 12:
        hour -= 12
        return f"0{hour}:{time[3:5]}:{time[6:8]}"
    
    return time


input = "12:45:54PM"
print(time_conversion(input))
