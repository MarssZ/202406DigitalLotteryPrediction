### 计算历史开奖次数 ###

import pandas as pd
# 超参数
COLS_ALL = ['期号', '开奖日期', '开奖号码']
COLS_Y = ['开奖号码']
file_path = 'Data\福彩3D历史开奖.csv'
# 读取excel文件并获取指定列
df = pd.read_csv(file_path,usecols=COLS_ALL, encoding='GBK')
print('读取cvs文件: '+file_path)

# 如果遇到错误，可以打印文件的列名来检查
if df.empty:
    print("列名可能不匹配，这里是文件的列名：")
    with open(file_path, 'r') as f:
        print(f.readline().strip().split(','))  # 假设CSV文件使用逗号分隔

### 计算某号码历史中奖次数 ###
def count_occurrences(target_number):
    """
    计算指定数字在DataFrame列中出现的次数
    
    参数:
    target_number : str or int
        要搜索的数字，可以是字符串或整数形式。
        
    返回:
    int
        指定数字在列中出现的次数。
    """

    # 计算目标数字出现的次数, 适用于开奖号码是object类型的情况。
    return (df[COLS_Y] == target_number).sum().iloc[0]
    
# #测试代码
# number = 944
# count = int(count_occurrences(number))
# print(f"数字 {number} 出现了 {count} 次。")


### 获取历史中奖号码 ###
def get_lottery_numbers_list(n=None):
    """
    读取CSV文件中指定列的数据(开奖数据），并以数组形式返回。

    参数:
    n : int，可选
        要返回的开奖结果的数量。如果为None，则返回全部结果。

    返回:
    list
        包含开奖号码的数组。
    """
    # 将指定列的数据转换为数组
    lottery_numbers = df[COLS_Y[0]].values.tolist()
    
    # 如果n为None，则返回全部结果，否则返回前n个结果
    return lottery_numbers if n is None else lottery_numbers[:n]


# #测试代码
#print(get_lottery_numbers_list())