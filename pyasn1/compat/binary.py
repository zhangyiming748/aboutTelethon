#
# This file is part of pyasn1 software.
#
# Copyright (c) 2005-2019, Ilya Etingof <etingof@gmail.com>
# License: http://snmplabs.com/pyasn1/license.html
#

'''
这个模块提供了Python 2.6以下版本的bin()函数兼容实现。

bin()函数用于将整数转换为其二进制字符串表示形式。在Python 2.6之前的版本中
并不包含这个内置函数，因此这个模块提供了一个自定义实现。

主要功能：
1. 对于Python 2.6及以上版本：直接使用内置的bin()函数
2. 对于Python 2.6以下版本：提供一个自定义的bin()函数实现
   - 支持正数、负数和零的转换
   - 生成的格式与Python内置bin()函数一致（如"0b1010"）
'''

from sys import version_info

if version_info[0:2] < (2, 6):
    def bin(value):
        """将整数转换为二进制字符串表示。
        
        参数：
            value (int): 要转换的整数值
            
        返回：
            str: 整数的二进制字符串表示，格式如：
                - 正数：'0b1010'
                - 负数：'-0b1010'
                - 零：'0b0'
        """
        bitstring = []  # 用于存储二进制位的列表

        # 确定二进制字符串的前缀
        if value > 0:
            prefix = '0b'
        elif value < 0:
            prefix = '-0b'
            value = abs(value)  # 对负数取绝对值
        else:
            prefix = '0b0'  # 零的特殊情况

        # 通过不断右移和按位与操作提取每一位
        while value:
            if value & 1 == 1:  # 检查最低位是否为1
                bitstring.append('1')
            else:
                bitstring.append('0')

            value >>= 1  # 右移一位

        bitstring.reverse()  # 反转列表得到正确的二进制表示

        return prefix + ''.join(bitstring)
else:
    # Python 2.6及以上版本直接使用内置的bin函数
    bin = bin
