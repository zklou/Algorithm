def alpcount(S: str) -> str:
    cnt = 0
    char = S[0]  # Corrected from "input" to "S" and "input[0]" to "S[0]"
    outputt = ''

    for chara in S:
        if chara == char:
            cnt += 1  # Corrected from "cnt + 1" to "cnt += 1"
        else:
            outputt += char + str(cnt)
            char = chara  # Corrected from "chara = char" to "char = chara"
            cnt = 1

    outputt += char + str(cnt)
    
    return outputt if len(outputt) < len(S) else S  # Corrected from "len(char)" to "len(S)"

inputstring = "abcde"
output = alpcount(inputstring)
print(output)
