x = [{"id":101,"name":"Rohit kumar sharma","phy":90,"chem":75,"maths":98},
     {"id":102,"name":"Ravi","phy":80,"chem":74,"maths":100},
     {"id":103,"name":"Ram","phy":33,"chem":33,"maths":48},
     {"id":104,"name":"Ramesh","phy":60,"chem":85,"maths":80},
     {"id":105,"name":"Mukesh","phy":0,"chem":7,"maths":8}]

'''
for data in x:

    avg = (data["phy"]+data["chem"]+data["maths"])//3
    data["avg"] = avg
    print(data["id"],data["name"],data["avg"])
    
'''
import pandas as pd
df = pd.DataFrame(x)
print(df)
