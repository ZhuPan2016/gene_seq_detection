from code1 import get_target
import os
def get_single_file_result(target_file_name,
                           seq_file_name
):
        
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

    for idx, ele in enumerate(target_f):
        if ele in seq and target_r[idx] in seq:
            print(target_name[idx], "在", seq_file_name)

seq_base = "C:\\Users\\l\\Desktop\\seqBase\\"  
for file_ in os.listdir(seq_base):
    get_single_file_result(target_file_name='C:\\Users\\l\\Desktop\\引物序列 - 副本.csv',seq_file_name=seq_base+file_)