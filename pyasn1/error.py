#
# This file is part of pyasn1 software.
#
# Copyright (c) 2005-2019, Ilya Etingof <etingof@gmail.com>
# License: http://snmplabs.com/pyasn1/license.html
#


class PyAsn1Error(Exception):
    """
    pyasn1基础异常类
    
    PyAsn1Error是所有ASN.1相关错误的基础异常类，继承自Python标准库的Exception类。
    它用于表示在ASN.1编码、解码和处理过程中可能出现的所有类型的错误。
    
    这个异常类作为pyasn1库中其他所有特定异常类的父类，提供了统一的错误处理机制。
    当遇到ASN.1相关的错误时，要么直接抛出这个异常，要么抛出它的子类异常。
    """


class ValueConstraintError(PyAsn1Error):
    """
    ASN.1类型约束违反异常
    
    ValueConstraintError异常表示违反了ASN.1值的约束条件。这种错误可能发生在以下情况：
    
    1. 实例化标量类型的值对象时：例如，给一个INTEGER类型赋值超出其允许范围
    2. 序列化构造类型时：例如，一个SEQUENCE类型的必需字段缺失
    
    这个异常通常表明输入的数据不符合ASN.1规范中定义的约束条件。
    """


class SubstrateUnderrunError(PyAsn1Error):
    """
    ASN.1数据结构反序列化错误
    
    SubstrateUnderrunError异常表示在反序列化过程中，输入的序列化数据不足。
    这通常发生在以下情况：
    
    1. 解码ASN.1数据时发现数据不完整
    2. BER/DER/CER解码器期望读取更多数据，但已到达输入流末尾
    
    这个错误表明输入的ASN.1编码数据可能被截断或损坏。
    """


class PyAsn1UnicodeError(PyAsn1Error, UnicodeError):
    """
    Unicode文本处理错误
    
    PyAsn1UnicodeError是处理Unicode文本序列化和反序列化相关错误的基础异常类。
    它同时继承自：
    1. PyAsn1Error - 保持与ASN.1错误体系的一致性
    2. UnicodeError - 便于调用者捕获Unicode相关错误
    
    这个异常类主要用于处理ASN.1字符串类型（如UTF8String、BMPString等）的编码解码过程中
    遇到的Unicode相关错误。
    """
    def __init__(self, message, unicode_error=None):
        if isinstance(unicode_error, UnicodeError):
            UnicodeError.__init__(self, *unicode_error.args)
        PyAsn1Error.__init__(self, message)


class PyAsn1UnicodeDecodeError(PyAsn1UnicodeError, UnicodeDecodeError):
    """
    Unicode文本解码错误
    
    PyAsn1UnicodeDecodeError表示在反序列化Unicode文本时发生的失败。
    它继承自：
    1. PyAsn1UnicodeError - ASN.1 Unicode错误基类
    2. UnicodeDecodeError - Python标准解码错误类
    
    这个异常通常发生在：
    1. 解码ASN.1 UTF8String类型时遇到无效的UTF-8序列
    2. 解码其他ASN.1字符串类型时遇到编码问题
    """


class PyAsn1UnicodeEncodeError(PyAsn1UnicodeError, UnicodeEncodeError):
    """
    Unicode文本编码错误
    
    PyAsn1UnicodeEncodeError表示在序列化Unicode文本时发生的失败。
    它继承自：
    1. PyAsn1UnicodeError - ASN.1 Unicode错误基类
    2. UnicodeEncodeError - Python标准编码错误类
    
    这个异常通常发生在：
    1. 编码ASN.1 UTF8String类型时，遇到无法用UTF-8表示的字符
    2. 编码其他ASN.1字符串类型时遇到字符集限制问题
    """


