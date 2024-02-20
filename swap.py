def swapc(input):
    output=''
    for char in input:
        if char =='i':
            output = 'e'
        elif char == 'e':
            output == 'i'
        else:
            output += char

    return output

inputstr ="Hello World"
answer = swapc(inputstr)
print(answer)