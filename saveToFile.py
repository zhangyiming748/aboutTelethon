# 保存信息到文件
def saveFile(fullName, content):
    with open(fullName, "a+", encoding="utf-8") as f:
        f.write(content)
        f.write("\n")
        f.flush()


if __name__ == '__main__':
    path = "test.txt"
    text = 'xxx'
    saveFile(path,text)
