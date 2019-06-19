#hashlib 提供字符串加密功能
import hashlib
string = 'jiangxiaolong'
md5 = hashlib.md5()
md5.update(string.encode('utf-8'))  #使用update传入字符串(要有编码),获得md5加密的值
res = md5.hexdigest()   # 使用hexdigest 获取MD5的值







