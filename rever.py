def reversechar(S:str)->str:
    
    spacecnt = 1
    charac = ''
    result = ''

    for char in S:
        if char == ' ':
            spacecnt += 1
            result = ' ' * spacecnt + result
        else:
            charac += char

        result = ' ' * spacecnt + charac + result
        return result

input = "bee  boo"
output = reversechar(input)
print(output)

