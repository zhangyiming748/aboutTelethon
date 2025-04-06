#
# This file is part of pyasn1 software.
#
# Copyright (c) 2005-2019, Ilya Etingof <etingof@gmail.com>
# License: http://snmplabs.com/pyasn1/license.html
#

'''
这个模块提供了Python不同版本间callable()函数的兼容实现。

callable()函数用于判断一个对象是否可调用（即是否能像函数一样被调用）。
在不同的Python版本中，这个函数的实现和可用性有所不同：

1. Python 2.x和Python 3.2+：内置callable()函数可用
2. Python 3.0-3.1：内置callable()函数被移除，需要使用isinstance()和collections.Callable判断

这个模块根据Python版本自动选择合适的实现。
'''

from sys import version_info

__all__ = ['callable']  # 模块公开的接口


if (2, 7) < version_info[:2] < (3, 2):
    # Python 3.0和3.1需要特殊处理
    # 在这些版本中，内置的callable()被移除了
    import collections

    def callable(x):
        """判断对象是否可调用
        
        参数：
            x: 要检查的对象
            
        返回：
            bool: 如果对象是可调用的（如函数、方法等）返回True，否则返回False
        """
        return isinstance(x, collections.Callable)

else:
    # 对于Python 2.x和Python 3.2+，直接使用内置的callable函数
    callable = callable
