def solution(st):
    for i in range(0,len(st)):
        if(st[i:len(st)] == st[i:len(st)][::-1]):
            return st[0:i] + st[i:len(st)] + st[0:i][::-1]