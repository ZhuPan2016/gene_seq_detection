import pandas as pd
def get_target(file_name="C:\\Users\\l\\Desktop\\引物序列.csv"):
    '''
        参数说明: 
                file_name: 引物序列的文件名
                           如："C:\\Users\\l\\Desktop\\引物序列.csv"
    '''
    target_f = []
    target_r = []
    target_name = []
    target = pd.read_csv(file_name, sep=',', header=None, encoding='utf-8')
    
    lines = target.shape[0]
    for i in range(lines):
        if i%2 == 0:
            target_f.append(target.loc[i][1])
            target_name.append(target.loc[i][0].split('-')[0])
        else:
            target_r.append(target.loc[i][1])
    return target_name,target_f,target_r


