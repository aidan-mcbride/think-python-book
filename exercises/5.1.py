import time

total_seconds = time.time()

s_in_min = 60
s_in_hour = s_in_min * 60
s_in_day = s_in_hour * 24

days = total_seconds // s_in_day
seconds_remaining = total_seconds % s_in_day

hours = seconds_remaining // s_in_hour
seconds_remaining = seconds_remaining % s_in_hour

minutes = seconds_remaining // s_in_min
seconds = seconds_remaining % s_in_min

print('days since epoch: {}'.format(days))
print('hours: {}'.format(hours))
print('minutes: {}'.format(minutes))
print('seconds: {}'.format(seconds))
