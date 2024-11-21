import json
import os

# 假设你的JSON文件名为data.json，并且它位于当前目录下
json_file_path = 'test.json'
readme_file_path = 'README.md'

# 读取JSON文件
with open(json_file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# 准备写入到README.md的内容
readme_content = "# 应用列表\n"
readme_content += "- 应用名称\t应用编号\n"

# 遍历JSON数据，格式化字符串
for key, value in data.items():
    readme_content += f"- {key}\t{value}\n"

# 将格式化后的内容写入到README.md文件中
with open(readme_file_path, 'w', encoding='utf-8') as file:
    file.write(readme_content)

print("README.md文件已更新。")
