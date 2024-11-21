import json


def read_json_and_write_to_md(json_file_path, md_file_path):
    # 读取JSON文件
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)

    # 准备要写入Markdown文件的内容
    markdown_content = "# 应用列表\n"

    for app in data:
        app_name = app.get("应用名称", "")
        app_id = app.get("应用编号", "")
        markdown_content += f"- {app_name}\t{app_id}\n"

        for key, value in app.items():
            if key not in ["应用名称", "应用编号"]:
                markdown_content += f"- {key}\t{value}\n"

    # 覆盖写入Markdown文件
    with open(md_file_path, 'w') as md_file:
        md_file.write(markdown_content)


if __name__ == "__main__":
    json_file_path = "test.json"  # 替换为实际的JSON文件路径
    md_file_path = "README.md"  # 替换为实际的Markdown文件路径
    read_json_and_write_to_md(json_file_path, md_file_path)
