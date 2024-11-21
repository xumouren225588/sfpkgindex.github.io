import json

# 假设你的JSON文件名为data.json
json_file = 'test.json'

# 读取JSON文件
with open(json_file, 'r', encoding='utf-8') as file:
    data = json.load(file)

# 初始化两个列表，分别存储键和值
keys = []
values = []

# 遍历JSON对象，将键和值添加到列表中
for key, value in data.items():
    keys.append(key)
    values.append(value)

# 写入README.md文件
with open('README.md', 'w', encoding='utf-8') as md_file:
    # 写入Markdown表格头部
    md_file.write('# 应用安装器索引\n')
    md_file.write('| 应用名称 | ID |\n')
    md_file.write('| --- | --- |\n')
    
    # 遍历键和值列表，写入表格行
    for key, value in zip(keys, values):
        md_file.write(f'| {key} | {value} |\n')
