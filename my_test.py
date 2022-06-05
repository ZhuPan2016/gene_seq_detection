from mymain import get_single_file_result
import os
import pandas as pd
'''
在命令行里运行 pip install openpyxl

'''
seq_base = "F:\\AI\\code\\htt\\test_file\BASE"  # 序列库文件夹 需要修改
target_file = 'F:\\AI\\code\\htt\\test_file\\mytarget.csv'  # 引物序列 需要修改
statistic_table = "F:\\AI\\code\\htt\\test_file\\statistics.xlsx"  # 统计表格 需要修改

statistic_table = pd.read_excel(statistic_table, 
                  engine='openpyxl',
                  index_col=0)
statistic_table.columns = statistic_table.columns.map(lambda x:x.upper())
# 将表的列名设置为大写，防止大小写的问题

for file_ in os.listdir(seq_base):
    
    
    get_single_file_result(target_file_name=target_file,
                           statistic = statistic_table,
                           seq_file_name=os.path.join(seq_base, file_),
                           output_seq=False)
    statistic_table.to_excel(f"./table-test2.xlsx", engine='openpyxl')