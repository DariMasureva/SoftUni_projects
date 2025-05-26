hour_start = int(input())
minute_start = int(input())
hour_arrival = int(input())
minute_arrival = int(input())

start_in_minutes = hour_start * 60 + minute_start
arrival_in_minutes = hour_arrival * 60 + minute_arrival

# to check difference and separate late cases from early cases
diff = arrival_in_minutes - start_in_minutes

# unified way to calculate the difference in all cases
diff_abs = abs(diff)
hours = diff_abs // 60
minutes = diff_abs - hours * 60

# formatting leading zeros in the specific case
if minutes < 10:
    minutes = f"{minutes:02d}"

if diff > 0:
    print("Late")
    if diff_abs >= 60:
        print(f"{hours}:{minutes} hours after the start")
    else:
        print(f"{diff_abs} minutes after the start")
elif -30 <= diff <= 0:
    print("On time")
    if diff_abs >= 60:
        print(f"{hours}:{minutes} hours before the start")
    elif diff_abs > 0:
        print(f"{diff_abs} minutes before the start")
elif diff < -30:
    print("Early")
    if diff_abs >= 60:
        print(f"{hours}:{minutes} hours before the start")
    else:
        print(f"{diff_abs} minutes before the start")
