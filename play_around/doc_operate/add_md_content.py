#!/bin/python
import re
import os
import sys

def add_contents(in_file,out_file):
    """
        添加直达目录
    """

    nf = open(out_file, "w",encoding="utf-8")

    nf.write("# 目录\n")

    with open(in_file, "r",encoding="utf-8") as f:
        lines = f.readlines()

    tno_regx = r"(#){1,5} ((\d){1,2}\.((\d){1,2}\.)*(\d){1,2}|(\d){1,2}\.)"
    
    
    tno_regx = r"(#){1,5} ((\d){1,2}\.((\d){1,2}\.)*(\d){1,2}|(\d){1,2}\.)"
    title_regx = r"(#){1,5} ((\d){1,2}\.((\d){1,2}\.)*(\d){1,2}|(\d){1,2}\.)(.)*"

    for line in lines:

        tno = re.match(tno_regx,line)
        title = re.match(title_regx,line)

        if title:

            t1 = title.group().split(" ")[0]
            t2 = tno.group().split(" ")[1]

            head_len = len(t1) + 1
            tabs = len(t1) - 1

            tab_str = tabs*"\t"
            
            t3 = title.group()[head_len:]

            # print(f"{tab_str}- [{t3}](#ch{t2})\n")
            nf.write(f"{tab_str}- [{t3}](#ch{t2})\n")


    nf.close()
    print(f"File {in_file} contents has been added!")


def modify_title_style(in_file):
    """
        根据原文修改标题样式
    """
    if not os.path.exists(in_file):
        print("File doesn't exist, please ensure it again.")
        return

    if not (".md" in in_file and in_file.split(".")[-1] == "md"):
        print("The type of the file is not markdown, please ensure agin.\n")
        return

    filename = in_file[:-3]
    out_file = f"{filename}_new.md"

    if os.path.exists(out_file):
        os.remove(out_file)

    # 添加直达目录
    add_contents(in_file,out_file)

    outf = open(out_file, "a",encoding="utf-8")

    with open(in_file, "r",encoding="utf-8") as f:
        lines = f.readlines()

    tno_regx = r"(#){1,5} ((\d){1,2}\.((\d){1,2}\.)*(\d){1,2}|(\d){1,2}\.)"
    title_regx = r"(#){1,5} ((\d){1,2}\.((\d){1,2}\.)*(\d){1,2}|(\d){1,2}\.)(.)*"

    for line in lines:

        tno = re.match(tno_regx,line)
        title = re.match(title_regx,line)

        if title:

            t1 = title.group().split(" ")[0]
            t2 = tno.group().split(" ")[1]

            head_len = len(t1) + 1

            t3 = title.group()[head_len:]
            
            # print(f"{t1} <a id=\"ch{t2}\">{t3}</a>")
            outf.write(f"{t1} <a id=\"ch{t2}\">{t3}</a>\n")

        else:
          outf.write(line)

    outf.close()

    print(f"File {in_file} title mark has been added!")

def main():
    # python 没有 && 符号，哈哈
    if len(sys.argv) == 1:
        files = input("Please input a markdown filename: \n")
    elif len(sys.argv) == 2:
        files = sys.argv[1]
    else:
        files = sys.argv[1:]

    if type(files) == str:
        modify_title_style(files)
    else:
        for file in files:
            modify_title_style(file)
            print()

if __name__ == '__main__':
    main()
