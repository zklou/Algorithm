# to rearrage 1,check letter count, we alp.single<=1  alp.2n>=2
#basiclly count alp first

def tfdecision(inputstr):
#first we need to get char count by each alp
    count = {}
    odd_count = 0
# then we count alp in our char it will search thru the list 1,1,2
    for char in inputstr:
        count[char] = count.get(char,0) + 1



# to check odd we need compare count%2 and 0
# if we have more than 2 odd count then return false, else return true
    for ocount in count.values():
        if ocount % 2 !=0:
            odd_count += 1
            print(odd_count)
    
    if odd_count <= 1:
        print("False")
    else: print("True")


input = "abaa"
output = tfdecision(input)
