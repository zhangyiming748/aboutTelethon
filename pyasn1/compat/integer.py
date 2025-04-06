#
# This file is part of pyasn1 software.
#
# Copyright (c) 2005-2019, Ilya Etingof <etingof@gmail.com>
# License: http://snmplabs.com/pyasn1/license.html
#

'''
这个模块提供了Python不同版本间整数与字节序列转换的兼容实现。

主要功能：
1. from_bytes(): 将字节序列转换为整数
2. to_bytes(): 将整数转换为字节序列
3. bitLength(): 计算整数的位长度

实现策略：
- Python 3.2+ (CPython): 直接使用内置的int.from_bytes和int.to_bytes方法
- 其他Python版本：使用自定义实现，通过二进制转十六进制等方式实现转换

支持：
- 有符号和无符号整数的转换
- 可指定输出字节序列的长度
- 自动处理大小端序（固定使用大端序）
'''

import sys

try:
    import platform

    implementation = platform.python_implementation()

except (ImportError, AttributeError):
    implementation = 'CPython'

from pyasn1.compat.octets import oct2int, null, ensureString

if sys.version_info[0:2] < (3, 2) or implementation != 'CPython':
    # 在Python 3.2以下版本或非CPython实现中使用自定义实现
    from binascii import a2b_hex, b2a_hex

    if sys.version_info[0] > 2:
        long = int  # Python 3中不再有long类型，使用int代替

    def from_bytes(octets, signed=False):
        """将字节序列转换为整数
        
        参数：
            octets (bytes): 要转换的字节序列
            signed (bool): 是否作为有符号整数处理
            
        返回：
            int: 转换后的整数值
        
        说明：
            - 使用十六进制转换实现
            - 对于有符号整数，处理二进制补码形式
        """
        if not octets:
            return 0

        # 将字节序列转换为十六进制，再转为整数
        value = long(b2a_hex(ensureString(octets)), 16)

        # 处理有符号整数的负数情况（二进制补码）
        if signed and oct2int(octets[0]) & 0x80:
            return value - (1 << len(octets) * 8)

        return value

    def to_bytes(value, signed=False, length=0):
        """将整数转换为字节序列
        
        参数：
            value (int): 要转换的整数
            signed (bool): 是否作为有符号整数处理
            length (int): 期望的字节序列长度（字节数）
            
        返回：
            bytes: 转换后的字节序列
            
        异常：
            OverflowError: 当无符号模式下试图转换负数，或结果超出指定长度时
        """
        if value < 0:
            if signed:
                bits = bitLength(value)

                # 计算二进制补码形式
                maxValue = 1 << bits
                valueToEncode = (value + maxValue) % maxValue

            else:
                raise OverflowError('can\'t convert negative int to unsigned')
        elif value == 0 and length == 0:
            return null  # 特殊情况：0值且未指定长度
        else:
            bits = 0
            valueToEncode = value

        hexValue = hex(valueToEncode)[2:]
        if hexValue.endswith('L'):
            hexValue = hexValue[:-1]

        if len(hexValue) & 1:
            hexValue = '0' + hexValue

        # padding may be needed for two's complement encoding
        if value != valueToEncode or length:
            hexLength = len(hexValue) * 4

            padLength = max(length, bits)

            if padLength > hexLength:
                hexValue = '00' * ((padLength - hexLength - 1) // 8 + 1) + hexValue
            elif length and hexLength - length > 7:
                raise OverflowError('int too big to convert')

        firstOctet = int(hexValue[:2], 16)

        if signed:
            if firstOctet & 0x80:
                if value >= 0:
                    hexValue = '00' + hexValue
            elif value < 0:
                hexValue = 'ff' + hexValue

        octets_value = a2b_hex(hexValue)

        return octets_value

    def bitLength(number):
        """计算整数的位长度
        
        参数：
            number (int): 要计算位长度的整数
            
        返回：
            int: 整数的位长度
            
        说明：
            - 通过转换为十六进制字符串计算
            - 每个十六进制字符表示4位
            - 处理了Python 2中长整型的'L'后缀
        """
        # 计算无符号数的位数
        hexValue = hex(abs(number))
        bits = len(hexValue) - 2  # 减去'0x'前缀
        if hexValue.endswith('L'):  # 处理Python 2的长整型
            bits -= 1
        if bits & 1:  # 确保位数为4的倍数
            bits += 1
        bits *= 4  # 转换为位数（每个十六进制字符4位）
        return bits

else:
    # Python 3.2+ (CPython)版本使用内置方法
    def from_bytes(octets, signed=False):
        """将字节序列转换为整数（使用内置方法）
        
        参数：
            octets (bytes): 要转换的字节序列
            signed (bool): 是否作为有符号整数处理
            
        返回：
            int: 转换后的整数值
        """
        return int.from_bytes(bytes(octets), 'big', signed=signed)

    def to_bytes(value, signed=False, length=0):
        """将整数转换为字节序列（使用内置方法）
        
        参数：
            value (int): 要转换的整数
            signed (bool): 是否作为有符号整数处理
            length (int): 期望的字节序列长度（位数）
            
        返回：
            bytes: 转换后的字节序列
        """
        length = max(value.bit_length(), length)

        # 对于有符号数，可能需要额外的符号位
        if signed and length % 8 == 0:
            length += 1

        return value.to_bytes(length // 8 + (length % 8 and 1 or 0), 'big', signed=signed)

    def bitLength(number):
        """计算整数的位长度（使用内置方法）
        
        参数：
            number (int): 要计算位长度的整数
            
        返回：
            int: 整数的位长度
        """
        return int(number).bit_length()
