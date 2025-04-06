#
# This file is part of pyasn1 software.
#
# Copyright (c) 2005-2019, Ilya Etingof <etingof@gmail.com>
# License: http://snmplabs.com/pyasn1/license.html
#

'''
这个模块提供了Python 2和Python 3之间字节序列和字符串处理的兼容性实现。

主要功能：
1. 整数与字节的转换（int2oct, oct2int）
2. 整数序列与字节序列的转换（ints2octs, octs2ints）
3. 字符串与字节序列的转换（str2octs, octs2str）
4. 类型检查函数（isOctetsType, isStringType）

实现策略：
- Python 2: 使用str类型作为字节序列，使用chr/ord进行转换
- Python 3: 使用bytes类型作为字节序列，直接进行转换
'''

from sys import version_info

if version_info[0] <= 2:  # Python 2.x版本
    # 整数转字节：使用chr将0-255的整数转换为单个字符
    int2oct = chr
    
    # 整数序列转字节序列：将多个整数转换为字符串
    ints2octs = lambda s: ''.join([int2oct(x) for x in s])
    
    # 空字节序列
    null = ''
    
    # 字节转整数：使用ord将单个字符转换为0-255的整数
    oct2int = ord
    
    # 字节序列转整数序列：将字符串中的每个字符转换为整数
    octs2ints = lambda s: [oct2int(x) for x in s]
    
    # 字符串与字节序列转换：在Python 2中str即为字节序列，无需转换
    str2octs = lambda x: x
    octs2str = lambda x: x
    
    # 类型检查：在Python 2中str类型用作字节序列
    isOctetsType = lambda s: isinstance(s, str)
    
    # 字符串类型检查：包括str和unicode类型
    isStringType = lambda s: isinstance(s, (str, unicode))
    
    # 确保输入为字符串类型
    ensureString = str
else:  # Python 3.x版本
    # 整数序列转字节序列：直接使用bytes类型
    ints2octs = bytes
    
    # 整数转字节：将单个整数转换为只包含该整数的bytes对象
    int2oct = lambda x: ints2octs((x,))
    
    # 空字节序列
    null = ints2octs()
    
    # 字节转整数：在Python 3中bytes的元素本身就是整数，无需转换
    oct2int = lambda x: x
    octs2ints = lambda x: x
    
    # 字符串与字节序列转换：使用iso-8859-1编码（单字节编码）
    str2octs = lambda x: x.encode('iso-8859-1')
    octs2str = lambda x: x.decode('iso-8859-1')
    
    # 类型检查：在Python 3中使用bytes类型作为字节序列
    isOctetsType = lambda s: isinstance(s, bytes)
    
    # 字符串类型检查：在Python 3中只有str类型
    isStringType = lambda s: isinstance(s, str)
    
    # 确保输入为bytes类型
    ensureString = bytes
