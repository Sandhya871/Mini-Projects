import time 
my_time = int(input("Enter your time in sec: "))
for x in range(my_time,0,-1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
print("TIME's UP!")


A Python countdown timer that accepts user input, displays the remaining time 
in HH:MM:SS format, and notifies the user when the countdown reaches zero.

# OUTPUT
Enter your time in sec: 3
00:00:03
00:00:02
00:00:01
TIME's UP!
