import pandas as pd
import sys
import time
a = pd.read_excel("C:\\Users\\zhup\Documents\\WeChat Files\\wxid_6o98tt6k3jx121\\FileStorage\\File\\2022-06\\毒力基因统计(1).xlsx", 
                  engine='openpyxl',
                  index_col=0)
a.columns = a.columns.map(lambda x:x.upper())
print(a)
gene_name = 'IUT'
try:
    
    _ = a.loc['KP-1'][gene_name]
except KeyError:
    print(f"错误基因名{gene_name}, 程序退出")
    sys.exit()
else:
    a.loc['KP-1'][gene_name] = 100
now = time.strftime("%m-%d-%H-%M-%S", time.localtime()) 

a.to_excel(f"./table-{now}.xlsx", engine='openpyxl')
print(a)