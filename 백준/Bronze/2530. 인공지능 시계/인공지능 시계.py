hour,minute,second = map(int,input().split())
given_seconds = int(input())

given_hours = given_seconds // 3600
given_minutes = given_seconds // 60 % 60
given_seconds = given_seconds % 60


result_hours = hour + given_hours
result_minutes = minute + given_minutes
result_seconds = second + given_seconds

final_seconds = (result_seconds) % 60
final_minutes = (result_minutes + (result_seconds) // 60) % 60
final_hours = (result_hours + (result_minutes + (result_seconds) // 60) // 60) % 24

print(final_hours, final_minutes, final_seconds)