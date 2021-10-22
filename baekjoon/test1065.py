def hans(n):
    if len(str(n)) == 1 or len(str(n))==2:
        return n
    elif len(str(n)) > 2:
        result = []
        for i in range(100, n+1):
            if (i-i//100*100)//10 - i//100 == i%10 - (i-i//100*100)//10:
                result.append(i)
        return 99 + len(result)
