from datetime import datetime

date_one = datetime(2025, 2, 11, 14, 30, 0)  
date_two = datetime(2025, 2, 12, 16, 45, 0)  

difference = date_two - date_one


seconds_difference = difference.total_seconds()

print(f"The difference between the two dates is {seconds_difference} seconds.")