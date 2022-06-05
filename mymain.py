from code1 import get_target
import pandas as pd
import os
from utils import *
import sys
def get_single_file_result(target_file_name,
                           seq_file_name,
                           statistic,
                           output_seq=False
):
    '''
    参数说明：
            target_file_name: 需要查找的目标基因序列文件名 .csv文件
                              如："C:\\Users\\l\\Desktop\\引物序列.csv"

                              文件形式：
                                    K1-f, GGTGCTCTTTACATCATTGC
                                    K1-r, CTAACGCAAATGGCCATTGC
                                    K2-f, GACCCGATATTCATACTTGACAGAG
                                    K2-r, ATCTATTTACGATTTTACTTCAGG
                                                ...
            seq_file_name: 基因序列文件名
                           如："C:\\Users\\l\\Desktop\\KP-1.fasta"

            statistic: 统计表
                            

            output_seq: 是否输出查找成功的中间序列, 默认不输出
    '''
    

    target_name, target_f, target_r = get_target(target_file_name)

    # target_name = [
    # "K1",
    # "K2",
    # "FK1",
    # "FK3",
    # ]
    # target_f = ['GGTGCTCTTTACATCATTGC',
    #             "GACCCGATATTCATACTTGACAGAG",
    #             "GTGAAAGTGGATGTCTCCGACCG",
    #             "ATACCGGTAGCAAGCTGG"
    #  ]
    # target_r = ['CTAACGCAAATGGCCATTGC',
    #             "ATCTATTTACGATTTTACTTCAGG",
    #             "ATGATATCGGTAATAAAGGACCT",
    #             "TGAAGCCGATTACCGGGCGGTCGCAC"
    # ]

    seq = ''
    with open(seq_file_name) as file_:
        for line in file_:
            seq += line.strip()

    for idx, ele in enumerate(target_name):
        position_f = seq.find(target_f[idx])
        position_r = seq.rfind(target_r[idx])
        
        if position_f >=0 and position_r > position_f:
            KP_number = get_KP_from_seq_file_name(seq_file_name)
            gene_name = ele.upper()
            try:
                _ = statistic.loc[KP_number][gene_name]
            except KeyError:
                print(f"错误基因名{gene_name}(不区分大小写), 程序退出。请检查基因名。")
                sys.exit()
            else:
                statistic.loc[KP_number][gene_name] = 1
            if output_seq:
                print(seq[position_f:(position_r+len(target_r))])
                print('- '*20)
    


            

