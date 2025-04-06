#
# This file is part of pyasn1 software.
#
# Copyright (c) 2005-2019, Ilya Etingof <etingof@gmail.com>
# License: http://snmplabs.com/pyasn1/license.html
#

'''
这个模块提供了Python不同版本间字符串partition方法的兼容性实现。

partition()方法将字符串按照指定的分隔符分割成三部分：
1. 分隔符前的子字符串
2. 分隔符本身
3. 分隔符后的子字符串

实现策略：
- Python 2.5及以下版本：使用split()方法模拟partition()的功能
- Python 2.6及以上版本：直接使用内置的partition()方法
'''

from sys import version_info

if version_info[:2] <= (2, 5):  # Python 2.5及更早版本

    def partition(string, sep):
        """将字符串分割成三部分
        
        参数：
            string (str): 要分割的字符串
            sep (str): 分隔符
            
        返回：
            tuple: 包含三个元素的元组 (head, separator, tail)
                - 如果找到分隔符：返回(分隔符之前部分, 分隔符, 分隔符之后部分)
                - 如果未找到分隔符：返回(原字符串, '', '')
        """
        try:
            # 尝试用分隔符分割字符串，最多分割一次
            a, c = string.split(sep, 1)

        except ValueError:
            # 分隔符未找到时的处理
            a, b, c = string, '', ''

        else:
            # 分隔符找到时，将其保存在b中
            b = sep

        return a, b, c

else:  # Python 2.6及更高版本

    def partition(string, sep):
        """将字符串分割成三部分
        
        在新版本Python中直接使用内置的partition方法。
        
        参数：
            string (str): 要分割的字符串
            sep (str): 分隔符
            
        返回：
            tuple: 包含三个元素的元组 (head, separator, tail)
        """
        return string.partition(sep)
