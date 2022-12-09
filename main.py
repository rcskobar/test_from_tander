# -*- encoding: utf-8 -*-

def changer(inval: str) -> str:
    result = ''
    i = 0
    while i < len(inval):
        if inval[i].isalpha():
            result += inval[i]
            i += 1
        elif inval[i].isdigit() and inval[i+1].isalpha():
            result += int(inval[i]) * inval[i+1]
            i += 2
        else:
            _open, _close = 0, 0
            tmp_i = i + 1 if inval[i].isdigit() else i
            for index, char in enumerate(inval[tmp_i:]):
                if char == '(':
                    _open += 1
                elif char == ')':
                    _close += 1
                if _open == _close:
                    index_stop = tmp_i + index
                    break
            multiplier = int(inval[i]) if inval[i].isdigit() else 1
            result += multiplier * changer(inval[tmp_i+1: index_stop])
            i += index_stop - i + 1
    return result


if __name__ == '__main__':
    print(changer("3ab2(z3k)"))
    print(changer("(a2s2d2f)"))
    print(changer("sad2(as2(df)2(gh))"))
