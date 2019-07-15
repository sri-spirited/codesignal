def firstNotRepeatingCharacter(s):
    lis = [a for a in s if s.count(a)==1]
    if len(lis)==0:
        return '_'
    else:
        return lis[0]
