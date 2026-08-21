def newString(s):
    n = len(s)
    letter = ""
    digit = ""
    if(s[0].isdigit()):
        digit += s[0]
    elif (s[0].isalpha()):
        letter += s[0]
    for ind in range(1,n):
        if((s[ind-1].isdigit() and s[ind].isalpha() or s[ind-1].isalpha() and s[ind].isdigit())):
            if(s[ind].isplha()):
                letter += s[ind]
            else:
                digit += s[ind]
    return letter + digit
s = input()
print(newString(s))
