from datetime import datetime, timedelta

bugin = datetime.now()

keshe = bugin - timedelta(days=1)
erten = bugin + timedelta(days=1)

print("yesterday:", keshe.strftime("%Y-%m-%d"))
print("today:", bugin.strftime("%Y-%m-%d"))
print("tomorrow:", erten.strftime("%Y-%m-%d"))