import math
rup1 = int(input("count of 1 rupes"))
rup2 = int(input("count of 2 rupes"))*2
rup5 = int(input("count of 5 rupes"))*5
rup10 = int(input("count of 10 rupes"))*10
rup20 = int(input("count of 20 rupes"))*20
rup50 = int(input("count of 50 rupes"))*50
rup100 = int(input("count of 100 rupes"))*100
rup200 = int(input("count of 200 rupes"))*200
rup500 = int(input("count of 500 rupes"))*500
rup2000 = int(input("count of 2000 rupes"))*2000

total_rup = rup1+rup2+rup5+rup10+rup20+rup50+rup100+rup200+rup500+rup2000
a=""
if total_rup==a:
    print("pelase enter value you dont enter any value")

else:
    print(f"this is total money {total_rup}")
