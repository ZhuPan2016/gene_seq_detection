'''
此文件存放一些小功能
'''

def get_KP_from_seq_file_name(seq_file_name):
    file_name = seq_file_name.split('\\')[-1]
    KP = file_name.split('.')[0]
    return KP.upper()

def get_max_target_len(*targets):
    ret = 0
    for target in targets:
        for t in target:
            ret = max(ret, len(t))
    return ret