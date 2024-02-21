def reverseorder(S: str) -> str:
# reverse space, multi spaces
# get space1, get string1, get space2, get string2 
# output = space1+string2+space2+string1 eg hello world to world hello

    spacecnt = 1
    output = ''
    string = ''

    for chara in S:
        if chara == ' ':
            output = ' ' * spacecnt + string + output
            spacecnt = 1
            string = '*'
            print(string)
        else:
            string += chara
            print(string)

    output = ' ' * spacecnt + string + output

    return output

inputstring = "   chan     code"
outputstring = reverseorder(inputstring)
print(outputstring)
