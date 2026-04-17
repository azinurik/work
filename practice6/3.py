from datetime import datetime
d = input()
b = input()
date1 = datetime.strptime(d, "%Y-%m-%d")
date2 = datetime.strptime(b, "%Y-%m-%d")
s = (date2 - date1).days
print(s)