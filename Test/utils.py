### 检查本期是否有指定数字
def check_number_in_lottery(df, column_names, value):
    """
    检查指定列中是否有等于给定数字的值，并返回一个布尔 Series。

    参数:
    df (pd.DataFrame): 输入的 DataFrame。
    column_names (list): 需要检查的列名列表。
    value (int or float): 需要比较的数字。

    返回:
    pd.Series: 布尔 Series，表示每一行是否在任何指定的列中包含等于给定值的元素。
    """
    # 使用任何指定列的比较结果合并到一个单独的列
    result_series = df[column_names].eq(value).any(axis=1)
    return result_series

### 检查下期是否有指定数字（即预测）
def check_number_in_next(df, column_names, value):
    """
     检查指定列的前一行中是否有等于给定数字的值，并返回一个布尔 Series。

    参数:
    df (pd.DataFrame): 输入的 DataFrame。
    column_names (list): 需要检查的列名列表。
    value (int or float): 需要比较的数字。

    返回:
    pd.Series: 布尔 Series，表示每一行是否在任何指定的列中包含等于给定值的元素。
    """
    # 使用任何指定列的比较结果合并到一个单独的列
    previous_row = df[column_names].shift(1)
    result_series = (previous_row == value).any(axis=1)
    # 由于第一行没有前一行，所以第一行的结果应该是 False
    result_series.iloc[0] = False
    return result_series

### 检查指定列中的值是否为偶数
def check_even_number(df, column_name):
    """
    检查指定列中的值是否为偶数，并返回一个布尔 Series。

    参数:
    df (pd.DataFrame): 输入的 DataFrame。
    column_name (str): 需要检查的列名。

    返回:
    pd.Series: 布尔 Series，表示指定列中的每个元素是否为偶数。
    """
    # 使用模运算符检查每个元素是否为偶数
    result_series = df[column_name] % 2 == 0
    return result_series
