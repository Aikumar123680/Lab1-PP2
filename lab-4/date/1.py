from datetime import datetime, timedelta

current_date = datetime.now()


new_date = current_date - timedelta(days=5)

print("Cur.date:", current_date.strftime("%Y-%m-%d"))
print("New date:", new_date.strftime("%Y-%m-%d"))