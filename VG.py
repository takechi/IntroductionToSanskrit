# -*- coding: utf-8 -*-

import sys
import re

def main():
    args = sys.argv

    suffix = "-vg"

    charToCIDDict = {
        "練": 13399,
        "交": 13439,
        "更": 13441,
        "硬": 13443,
        "使": 13450,
        "遺": 13642,
        "運": 13649,
        "音": 13664,
        "過": 13669,
        "弱": 13811,
        "終": 13816,
        "習": 13817,
        "消": 13836,
        "情": 13842,
        "聖": 13869,
        "請": 13872,
        "全": 13890,
        "退": 13905,
        "隊": 13907,
        "達": 13912,
        "追": 13938,
        "通": 13939,
        "半": 13986,
        "婦": 14002,
        "望": 14036,
        "連": 14097,
        "文": 20131,
    }

    replaceDict = {k: "\\CID{" + str(v) + "}" for k, v in charToCIDDict.items()}

    inputTexFilenames = [args[i] for i in range(1, len(args))]
    outputTexFilenames = [fn.replace(".tex", suffix + ".tex") for fn in inputTexFilenames]

    for (ifn, ofn) in zip(inputTexFilenames, outputTexFilenames):
        replaceDict[r"input{" + ifn + r"}"] = r"input{" + ofn + r"}"

    pattern = re.compile("|".join(replaceDict.keys()))

    for (ifn, ofn) in zip(inputTexFilenames, outputTexFilenames):
        string = open(ifn, encoding = "utf-8").read()
        replacedString = pattern.sub(lambda x: replaceDict[x.group(0)], string)
        open(ofn, "w", encoding = "utf-8").write(replacedString)

if __name__ == '__main__':
    main()
