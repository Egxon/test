# return string without spaces
def erase_simple(cc):
    lenStr = len(cc)
    i = 0

    if lenStr > 1:
        if cc[0] == ' ':
            if cc[1] != ' ':
                cc = cc[1:]
                lenStr -= 1

        while i < lenStr:
            if cc[i] == ' ':
                if i == lenStr - 1 and cc[i - 1] != ' ':
                    cc = cc[:i]
                    lenStr = len(cc)

                elif cc[i + 1] != ' ' and cc[i - 1] != ' ':
                    cc = cc[:i] + cc[i + 1:]
                    lenStr -= 1
            
            i += 1

    elif cc[0] == ' ':
        cc = ''

    return cc