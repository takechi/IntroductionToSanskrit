# -*- coding: utf-8 -*-

import sys
import re

def main():
    args = sys.argv

    suffix = "-vg"

    replaceDict = {}

    selectorAndCharList = (("󠄀", "海練連咬飲蓮"),
                           ("󠄁", "交更硬使暗遣運遠音過近誤斜弱終習勝消情聖請"
                                + "前全造速退隊達追通半婦平文飢便遺採伴分避要"
                                + "覆尊磨削槪選飾灰空認食"),
                           ("󠄂", "望慧響"), )

    for (selector, charList) in selectorAndCharList:
        for c in charList:
            replaceDict[c] = c + selector

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
