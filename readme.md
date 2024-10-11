# 数字彩工具
## 背景
    一直以来，人们认为彩票都只是纯概率。正如一些人试图证明股市是随机波动一样。的确，如果彩票没有人为干预而是纯随机的，我们的确没有办法进行预测。但值得注意的是，随着彩票反腐纪录片等事实被曝光，我们可以确信彩票正在被人为干预。那么，有一些基本的假设是可以被印证的：例如主办方自己想中大奖，则会规避掉其它彩民大量选中的号码（因为这会稀释奖金）。在以上假设的基础上，我们会通过深度学习与神经网络来寻找其中的蛛丝马迹，据此排除掉一些错误的可能性，以增加大家命中二、三等奖的概率。
## 博弈问题：避免与他人选择同样的数字
    当人们玩彩票时，他们往往会做出类似的选择。在过去的三十年中，研究人员已经确定了彩票玩家选择的号码的许多特征。例如，玩家倾向于选择“视情况而定”的号码和彩票中心的号码，以及“注重美观”的组合（Wang et al., 2016）。一个潜在的原因可能是人们忽视了他们处于战略形势的事实：最大化预期收益意味着不仅要选择正确的数字，还要选择很少有人选择的数字。

## 截图

## 文件说明
    Data/排列3历史开奖.csv    #从2004年起6900余期的历史数据。
    Data/福彩3D历史开奖.csv
    
    tools.py                        #与历史中奖号码有关的工具类

    Test/Test_Hist.ipynb            #查看各号码的直方图
    Test/Test_Hist_SumNum.ipynb     #查看和值的直方图
    Test_Hist_MissingNum.ipynb      #查看遗漏值的直方图
    Test/Test_Keras.ipynb           #测试用python训练神经网络
    Test/Test_curvefit.ipynb        #用函数拟合结果找参数
    
    Test/Test_DecisionTree          #使用决策树寻找公式
    Test/Test_RandomForest.ipynb    #使用随机森林寻找公式

    Calc_MissingNum.ipynb           #计算遗漏值，即某一开奖号码有多久没有被开出来了。

    Findnum_cold_warm.ipynb         #获取冷热号
    Findnum_consecutive.ipynb       #判断是否为连续号，计算连续号模式下的中奖率
    Findnum_SumNum.ipynb            #判断是否为和值极限情况，计算和值极限情况模式下的中奖率

    llm_normal.ipynb                #大模型回答普通版

## 维护者
[@MarssZ](https://github.com/MarssZ)

## 使用许可
[MIT](LICENSE) © MarssZ
