import string
def solution(cell1, cell2):
    alphabet_upper=list(string.ascii_uppercase)
    letter1=alphabet_upper.index(cell1[0])+1
    letter2=alphabet_upper.index(cell2[0])+1
    print(ord(cell1[0]))
    if (letter1+int(cell1[1]))%2==0 and (letter2+int(cell2[1]))%2==0:
        return True
    else:
        return False
print(solution("A1","C3"))