import pandas as pd

import time
a = pd.read_excel("C:\\Users\\zhup\Documents\\WeChat Files\\wxid_6o98tt6k3jx121\\FileStorage\\File\\2022-06\\毒力基因统计(1).xlsx", 
                  engine='openpyxl',
                  index_col=0)
print(a)

print("- "*20, a.loc['KP-1']['IUT'])
now = time.strftime("%m-%d-%H-%M-%S", time.localtime()) 

a.to_excel(f"./table-{now}.xlsx", engine='openpyxl')
print(a)