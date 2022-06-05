import pandas as pd
from code1 import get_target
from utils import *
import sys
import os
def segment_get_result_from_single_file(target_file_name, seq_file_name, statistic_file_name):
    count = 20000
    

    target_name, target_f, target_r = get_target(target_file_name)
    target_name, target_f, target_r = get_target(target_file_name)
    cache_len = get_max_target_len(target_f, target_r) + 10

    for idx, elem in enumerate(target_name):
        found_f = False
        found_r = False
        file_tell_f = 0
        file_tell_r = 0
        with open(seq_file_name) as f:
            i = 0
            cache = ''
            seq = ''
            while True:
                line = f.readline()
                if not line:
                    break
                i += 1
                seq += line.strip()
                if i == count:
                    i = 0
                    seq = cache + seq
                    cache = seq[-cache_len:]
                    # print(seq)
                    # print('- '*20)
                    if not found_f:
                        position_f = seq.find(target_f[idx])
                        if position_f >= 0:
                            found_f = True
                    if not found_r:
                        position_r = seq.find(target_r[idx])
                        if position_r >= 0:
                            found_r = True
                    seq = ''
                if not found_f:
                    position_f = seq.find(target_f[idx])
                    if position_f >= 0:
                        found_f = True
                        file_tell_f = f.tell()
                
                position_r = seq.rfind(target_r[idx])
                if position_r >= 0:
                    found_r = True
                    file_tell_r = f.tell()
        
        if found_f and found_r :
            if file_tell_f > file_tell_r:
                print(seq_file_name, elem, "f r 位置颠倒")
            else:
                KP_number = get_KP_from_seq_file_name(seq_file_name)
                gene_name = elem.upper()
                try:
                    _ = statistic_table.loc[KP_number][gene_name]
                except KeyError:
                    print(f"错误基因名{gene_name}(不区分大小写), 程序退出。请检查基因名")
                    sys.exit()
                else:
                    statistic_table.loc[KP_number][gene_name] = 1
    
if __name__ == "__main__":
    seq_base = "F:\\AI\\code\\htt\\test_file\\BASE"  # 序列库文件夹
    target_file = 'F:\\AI\\code\\htt\\test_file\\mytarget.csv'  # 引物序列
    statistic_table = "F:\\AI\\code\\htt\\test_file\\statistics.xlsx"  # 统计表
    statistic_table = pd.read_excel(statistic_table, 
                  engine='openpyxl',
                  index_col=0)
    statistic_table.columns = statistic_table.columns.map(lambda x:x.upper())
    # 将表的列名设置为大写，防止大小写的问题
    for file_ in os.listdir(seq_base):
        segment_get_result_from_single_file(target_file, os.path.join(seq_base, file_), statistic_table)
        statistic_table.to_excel(f"./table-test-seg.xlsx", engine='openpyxl')      