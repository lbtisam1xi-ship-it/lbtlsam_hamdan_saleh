total_seconds = int(input("Enter total seconds : "))
minute = 60
hour = 3600
day = 86400

days = total_seconds // day
remaining = total_seconds % day

hours = remaining // hour
remaining = remaining % hour

minutes = remaining // minute
seconds = remaining % minute

print(f"Total seconds: {total_seconds}")
print(f"Days:    {days}")
print(f"Hours:   {hours}")
print(f"Minutes: {minutes}")
print(f"Seconds: {seconds}")
print(f"Formatted: {days}d {hours:02d}h {minutes:02d}m {seconds:02d}s")
