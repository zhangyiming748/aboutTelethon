#
# This file is part of pyasn1 software.
#
# Copyright (c) 2005-2019, Ilya Etingof <etingof@gmail.com>
# License: http://snmplabs.com/pyasn1/license.html
#

'''
这个模块定义了ASN.1类型系统中的异常类。

主要包含：
- ValueConstraintError: 用于表示ASN.1类型系统中的值约束违反错误

这些异常类继承自pyasn1.error模块中的基础异常类PyAsn1Error。
'''

from pyasn1.error import PyAsn1Error


class ValueConstraintError(PyAsn1Error):
    """ASN.1类型系统中的值约束违反异常
    
    当ASN.1类型的值不满足其定义的约束条件时抛出此异常。
    例如：
    1. 整数值超出允许范围
    2. 字符串长度超出限制
    3. 枚举值不在允许的集合中
    
    这个异常类在type模块中重新定义，以便与error模块中的同名异常区分，
    主要用于ASN.1类型系统的内部实现。
    """
    pass
