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
def convert_tabs_to_spaces(text):
    

    lines = text.split('\n')
    new_lines = []

    for line in lines:
        tab_positions = []
        index = 0
        while True:
            index = line.find('\t', index)
            if index == -1:
                break
            tab_positions.append(index)
            index += 1

        new_line = line
        for pos in tab_positions:
            spaces_num = 8 - (pos % 8)
            new_line = new_line.replace('\t', ' '*spaces_num, 1)

        new_lines.append(new_line)

    new_text = "\n".join(new_lines)

    with open("README.md", "w", encoding='utf-8') as f:
        f.write(new_text)

if __name__ == "__main__":
    convert_tabs_to_spaces(readme_content)
    # 将格式化后的内容写入到README.md文件中


    print("README.md文件已更新。")
