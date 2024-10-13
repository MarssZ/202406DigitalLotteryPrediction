#####################
###### 命名规则 ######
##### check是本期 ####
#### predict是下期 ###
#####################

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

### 检查本期指定列是否有指定数字
def check_number_in_column(df, column_name, value):
    """
    检查指定列中是否有等于给定数字的值，并返回一个布尔 Series。

    参数:
    df (pd.DataFrame): 输入的 DataFrame。
    column_name (str): 需要检查的列名。
    value (int or float): 需要比较的数字。

    返回:
    pd.Series: 布尔 Series，表示每一行是否在指定的列中包含等于给定值的元素。
    """
    # 使用指定列的比较结果
    result_series = df[column_name].eq(value)
    return result_series

### 检查下期指定列是否有指定数字（即预测）
def predict_number_in_lottery(df, column_name, value):
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
    previous_row = df[column_name].shift(1)
    result_series = (previous_row == value).any(axis=1)
    # 由于第一行没有前一行，所以第一行的结果应该是 False
    result_series.iloc[0] = False
    return result_series

### 检查下期指定位置（某一列）是否有指定数字（即预测）
def predict_number_in_column(df, column_name, value):
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
    previous_row = df[column_name].shift(1)
    result_series = (previous_row == value)
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

### 检查指定列中的值是否全部为偶数
def check_all_even_numbers(df, column_names):
    """
    检查指定列中的值是否全都是偶数，并返回一个布尔 Series。

    参数:
    df (pd.DataFrame): 输入的 DataFrame。
    column_names (list[str]): 需要检查的列名列表。

    返回:
    pd.Series: 布尔 Series，表示每一行在指定列中的所有元素是否全都是偶数。
    """
    # 检查每一列的每个元素是否为偶数，然后对这些布尔值使用 all 方法
    # 这将返回一个布尔 Series，其中每个元素表示相应行的所有指定列的值是否全都是偶数
    result_series = df[column_names].apply(lambda row: row % 2 == 0).all(axis=1)
    return result_series

### 预测指定列的号码是否全部为偶数
def predict_all_even_numbers(df, column_names):
    """
    检查指定列的前一行中的值是否全都是偶数，并返回一个布尔 Series。

    参数:
    df (pd.DataFrame): 输入的 DataFrame。
    column_names (list[str]): 需要检查的列名列表。

    返回:
    pd.Series: 布尔 Series，表示每一行的前一行在指定列中的所有元素是否全都是偶数。
    """
    # 将指定列的数据向上移动一行
    shifted_df = df[column_names].shift(1)
    
    # 检查移动后的每一行的指定列中的值是否全都是偶数
    result_series = shifted_df.apply(lambda row: all(x % 2 == 0 for x in row), axis=1)
    
    # 由于第一行没有前一行，所以其结果为 NaN，我们可以将其填充为 False
    result_series = result_series.fillna(False)
    
    return result_series

### 检查指定列中的值是否全部为奇数
def check_all_odd_numbers(df, column_names):
    """
    检查指定列中的值是否全都是奇数，并返回一个布尔 Series。

    参数:
    df (pd.DataFrame): 输入的 DataFrame。
    column_names (list[str]): 需要检查的列名列表。

    返回:
    pd.Series: 布尔 Series，表示每一行在指定列中的所有元素是否全都是奇数。
    """
    # 检查每一列的每个元素是否为偶数，然后对这些布尔值使用 all 方法
    # 这将返回一个布尔 Series，其中每个元素表示相应行的所有指定列的值是否全都是偶数
    result_series = df[column_names].apply(lambda row: row % 2 != 0).all(axis=1)
    return result_series

### 预测下一期号码是否全部为奇数
def predict_all_odd_numbers(df, column_names):
    """
    检查指定列前一行中的值是否全都是奇数，并返回一个布尔 Series。

    参数:
    df (pd.DataFrame): 输入的 DataFrame。
    column_names (list[str]): 需要检查的列名列表。

    返回:
    pd.Series: 布尔 Series，表示每一行在指定列中的所有元素是否全都是奇数。
    """
    # 将指定列的数据向上移动一行
    shifted_df = df[column_names].shift(1)
    
    # 检查移动后的每一行的指定列中的值是否全都是偶数
    result_series = shifted_df.apply(lambda row: all(x % 2 != 0 for x in row), axis=1)
    
    
    result_series = result_series.fillna(False)
    
    return result_series

### 检查是否组六
def check_no_same(df, column_names):
    def exactly_no_same(row):
        # 如果行中所有值都不相同，则 unique() 方法返回的数组长度等于行的长度
        return len(row.unique()) == len(row)    

    result_series = df[column_names].apply(exactly_no_same, axis=1)
    return result_series

### 预测是否组六
def predict_no_same(df, column_names):
    def exactly_no_same(row):
        # 如果行中所有值都不相同，则 unique() 方法返回的数组长度等于行的长度
        return len(row.unique()) == len(row)    

    shifted_df = df[column_names].shift(1)  # 将指定列的数据向上移动一行
    result_series = shifted_df.apply(exactly_no_same, axis=1)
    result_series = result_series.fillna(False) # 由于第一行没有前一行，所以其结果为 NaN，我们可以将其填充为 False
    return result_series

### 检查是否组三
def check_two_same(df, column_names):
    # 检查每一行中是否有正好两个数字相同
    def exactly_two_same(row):
        unique_values = row.unique()
        if len(unique_values) == 2 and (row.value_counts().max() == 2):
            return True
        return False

    result_series = df[column_names].apply(exactly_two_same, axis=1)
    return result_series

### 预测是否组三
def predict_two_same(df, column_names):
    # 检查每一行中是否有正好两个数字相同
    def exactly_two_same(row):
        unique_values = row.unique()
        if len(unique_values) == 2 and (row.value_counts().max() == 2):
            return True
        return False
    shifted_df = df[column_names].shift(1)  # 将指定列的数据向上移动一行
    result_series = shifted_df.apply(exactly_two_same, axis=1)
    result_series = result_series.fillna(False) # 由于第一行没有前一行，所以其结果为 NaN，我们可以将其填充为 False
    return result_series

### 检查是否豹子
def check_three_same(df, column_names):
    # 检查每一行中是否有正好两个数字相同
    def exactly_three_same(row):
        # 如果行中所有值都相同，则 unique() 方法返回的数组长度为 1
        return len(row.unique()) == 1
    result_series = df[column_names].apply(exactly_three_same, axis=1)
    return result_series

### 预测是否豹子
def predict_three_same(df, column_names):
    # 检查每一行中是否有正好两个数字相同
    def exactly_three_same(row):
        # 如果行中所有值都相同，则 unique() 方法返回的数组长度为 1
        return len(row.unique()) == 1
    shifted_df = df[column_names].shift(1)  # 将指定列的数据向上移动一行
    result_series = shifted_df.apply(exactly_three_same, axis=1)
    result_series = result_series.fillna(False) # 由于第一行没有前一行，所以其结果为 NaN，我们可以将其填充为 False
    return result_series