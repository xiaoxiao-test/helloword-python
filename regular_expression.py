#  re模块使python拥有全部的正则表达式功能
import re
"""
    re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None
    re.search匹配整个字符串，直到找到一个匹配，如果全不匹配，函数返回None
"""

# 从起始位置开始匹配pattern，成功返回一个对象，否则返回none
line1 = "Cats are smarter than dogs"
match_obj = re.match(r'(.*) are (.*?) .*', line1, re.M | re.I)
print(match_obj)
print('\nsearchObj.span:', match_obj.span())  # span 获取匹配对象的起止索引
if match_obj:

    print("match_obj.group() : ", match_obj.group())  # 获取对象匹配的整个pattern的内容
    print("match_obj.group(1) : ", match_obj.group(1))  # 获取对象匹配的pattern中的第1个分组
    print("match_obj.group(2) : ", match_obj.group(2))
    print("match_obj.groups() : ", match_obj.groups())  # 获取对象匹配的所有分组，返回tuple
else:
    print("No match!!")

# 扫描整个字符串返回第一个匹配的起止位置, 成功返回一个对象，否则返回none
line2 = ' hua xdd is true '
search_obj = re.search(r'd is (.*?) .*', line2, re.M | re.I)
print(search_obj)
print('\nsearch_obj.span:', search_obj.span())
if search_obj:
    print("search_obj.group() : ", search_obj.group())
    print("search_obj.group(1) : ", search_obj.group(1))
    print("search_obj.groups() : ", search_obj.groups())
else:
    print("No search!!")

"""
    re.sub替换字符串中的匹配项，检索并替换
"""
line3 = '2004-959-559 # 这是一个国外电话号码'

num = re.sub(r'#.*$', "？", line3)  # 替换字符串中的 Python注释为？
print("\nre.sub : ", num)

num = re.sub(r'\D', "", line3, count=4)  # 删除4个非数字(-)的字符串count默认0替换所有
print("re.sub : ", num)


def double(matched):  # 将匹配的数字乘以 2
    value = int(matched.group('value'))
    return str(value * 2)


def_sub_str = 'A23G4HFD567'
print('def re.sub : ', re.sub('(?P<value>\d+)', double, def_sub_str))

"""
 re.compile 生成pattern对象给match和search方法使用
"""
line_compile = "one12twothree34four"
compile_pattern = re.compile(r'(\d+).*(\d+)')
compile_obj = compile_pattern.match(line_compile, 3, 15)  # 可设置匹配的起止所有位置为(3,4)
print(compile_obj)
if compile_obj:
    print('\ncompile_obj.end() ：', compile_obj.end(1))  # 获取匹配到的第1个分组的最后一个元素的索引
    print('compile_obj.start() ：', compile_obj.start(2))  # 获取匹配到的第2个分组的第一个元素的索引
    print('compile_obj.span() ：', compile_obj.span(2))  # 获取匹配到的第2个分组的起止索引
    print('compile_obj.group() ：', compile_obj.group())
"""
 re.findall 返回字符串中所有匹配正则表达式的字串列表，若无返回空列表 
 re.finditer 查找字符串所有匹配的字串并作为迭代器返回
"""

line_findall = '12a32bc43jf3'
pattern_findall = re.compile(r'\d')   # 匹配数字
findall_list = pattern_findall.findall(line_findall, 0, 5)  # 可设置匹配的起止位置为(0, 5)

print('\nfindall ：', findall_list)
it = re.finditer(r"\d+ab", "12a32bc43jf3")
print(it)
for item in it:
    print('finditer ：', item.group())

"""
    re.split 使用匹配正则表达式的内容分割字符串，返回列表，分割内容不包含匹配的内容
"""
line_split = 'sd73ve92ddd0'
pattern_split = re.compile(r'\d+')
split_list = pattern_split.split(line_split, 2)
print('\nsplit ：', split_list)
