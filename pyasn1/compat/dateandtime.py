#
# This file is part of pyasn1 software.
#
# Copyright (c) 2005-2019, Ilya Etingof <etingof@gmail.com>
# License: http://snmplabs.com/pyasn1/license.html
#

'''
这个模块提供了Python不同版本间strptime()函数的兼容实现。

strptime()函数用于将字符串解析为datetime对象。在不同的Python版本中，
这个函数的实现位置和使用方式有所不同：

1. Python 2.4及以下版本：
   - datetime.strptime不可用
   - 使用time.strptime配合datetime构造函数实现

2. Python 2.5及以上版本：
   - 可直接使用datetime.strptime

这个模块会根据Python版本自动选择合适的实现方式。
'''

import time
from datetime import datetime
from sys import version_info

__all__ = ['strptime']  # 模块公开的接口


if version_info[:2] <= (2, 4):
    # Python 2.4及更早版本的实现
    def strptime(text, dateFormat):
        """将字符串解析为datetime对象
        
        在Python 2.4及以下版本中，通过组合time.strptime和datetime构造函数实现。
        
        参数：
            text (str): 要解析的日期时间字符串
            dateFormat (str): 日期时间格式字符串
            
        返回：
            datetime: 解析后的datetime对象
        """
        return datetime(*(time.strptime(text, dateFormat)[0:6]))

else:
    # Python 2.5及更高版本直接使用datetime.strptime
    def strptime(text, dateFormat):
        """将字符串解析为datetime对象
        
        在Python 2.5及以上版本中，直接使用datetime.strptime实现。
        
        参数：
            text (str): 要解析的日期时间字符串
            dateFormat (str): 日期时间格式字符串
            
        返回：
            datetime: 解析后的datetime对象
        """
        return datetime.strptime(text, dateFormat)
