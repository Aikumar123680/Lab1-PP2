from datetime import datetime

current_datetime = datetime.now()

datetime_without_microsec = current_datetime.replace(microsecond=0)

print("Cur_datetime:", current_datetime)
print("Datetime without microsec:", datetime_without_microsec)