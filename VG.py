# -*- coding: utf-8 -*-

import sys
import re

def main():
    args = sys.argv

    suffix = "-vg"

    replaceDict = {}

    selectorAndCharList = (("󠄀", "海練連咬飲蓮祝諸憎祥神羽祐精難禍"),
                           ("󠄁", "交更硬使暗遣運遠音過近誤斜弱終習勝消情聖請"
                                + "前全造速退隊達追通半婦平文飢便遺採伴分避要"
                                + "覆尊磨削槪選飾灰空認食濯呈捨忍僧急遮尋送返"
                                + "肩迎肉益飽侮程述還置住者乳翔遍服尊逝鎮摩起"
                                + "評躍僧"),
                           ("󠄂", "望慧響節返害翼船"))

    for (selector, charList) in selectorAndCharList:
        for c in charList:
            replaceDict[c] = c + selector

    inputTexFilenames = [args[i] for i in range(1, len(args))]
    outputTexFilenames = [fn.replace(".tex", suffix + ".tex") for fn in inputTexFilenames]

    for (ifn, ofn) in zip(inputTexFilenames, outputTexFilenames):
        replaceDict[r"input{" + ifn + r"}"] = r"input{" + ofn + r"}"

    # {} で囲まれている場合は置換しない
    pattern = re.compile("|".join([r"([^{])" + c + r"([^}])" for c in replaceDict.keys()]))

    def repl_func(x):
        matched_string = x.group(0)
        pre = matched_string[0]
        s = matched_string[1:-1]
        post = matched_string[-1]
        return pre + replaceDict[s] + post
    for (ifn, ofn) in zip(inputTexFilenames, outputTexFilenames):
        string = open(ifn, encoding="utf-8").read()
        replacedString = pattern.sub(repl_func, string)
        open(ofn, "w", encoding="utf-8").write(replacedString)

if __name__ == '__main__':
    main()
