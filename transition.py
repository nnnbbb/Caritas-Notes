import re
import os
import sys

abspath = os.path.abspath(__file__)
dirname = os.path.dirname(abspath)
os.chdir(dirname)


def load(path):
    with open(path, 'r', encoding='utf-8') as f:
        s = f.read()
        return s


def save(data, path):
    with open(path, 'w+', encoding='utf-8') as f:
        f.write(data)


if __name__ == "__main__":
    # 删除知乎复制过来的markdown文本里包含关键词的超链接
    args = sys.argv[1:]
    path = args[0]

    frase = load(path)
    # 匹配超链接文本格式 例如: [Google](http://www.google.com/)
    result = re.findall(r"\[.+?\]\(.+?\)", frase)

    for text in result:
        # 关键词的链接都包含 search_source, 用这个条件判断是关键词链接, 而不是其他链接
        if text.find("search_source") != -1:
            word = re.search(r"\[(.+?)\]", text)
            s = word.group(1)
            frase = frase.replace(text, s)

    save(frase, path)
