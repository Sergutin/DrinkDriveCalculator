from datetime import datetime, timedelta
x = datetime.now().strftime("%H:%M %Y-%m-%d")
print(x)

y = 3
date = datetime.now() + timedelta(hours=y)
print(date)