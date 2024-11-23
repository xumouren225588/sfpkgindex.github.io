import json


def generate_checkbox_html(json_data):
    checkbox_html = ""
    for key, value in json_data.items():
        checkbox_html += f'        <input type="checkbox" id="{value}" value="{value}">{key}<br>'
    return checkbox_html


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
# 生成复选框的HTML代码
checkbox_html = generate_checkbox_html(data)

html_template = f"""<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-height=1.0">
    <title>Checkbox to JSON and Download</title>
</head>

<body>
    <form id="myForm">
{checkbox_html}
        <input type="submit" value="提交">
    </form>

    <script>
        document.getElementById("myForm").addEventListener("submit", function (event) {{
            event.preventDefault();

            var selectedItems = [];
            var checkboxes = document.querySelectorAll('input[type="checkbox"]:checked');

            checkboxes.forEach(function (checkbox) {{
                selectedItems.push(checkbox.value);
            }});

            var jsonData = JSON.stringify(selectedItems);
            console.log(jsonData);

            // 创建一个临时的 <a> 元素用于下载
            var link = document.createElement('a');
            var blob = new Blob([jsonData], {{ type: 'text/plain' }});
            link.href = URL.createObjectURL(blob);
            link.download = 'selected_items.txt';

            // 模拟点击链接进行下载
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
        }});
    </script>

</body>

</html>
"""
# 这里可以将生成的html_template内容保存为一个新的HTML文件，比如：
with open('index.html', 'w', encoding='utf-8') as html_file:
    html_file.write(html_template)

