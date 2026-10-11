from datetime import datetime
from additional import brows
li=brows()
print(li)
hour=datetime.now().strftime("%H")
min=datetime.now().strftime("%M")
full_time=hour+"."+min


for i in li:
    if i[0]==full_time:
        print(i[1]+" " +"time")
    else:
        continue

