def fn(s):
    s=list(s)
    s.reverse()
    n=0
    while s:
        t = s.pop()
        if t == "(": 
            n += 1
        elif t == ")": 
            n -= 1

        if n < 0:
            return -1
    if n:
        return 1
    else:
        return 0

def test_fn():
    import random 
    assert 1 == fn("((()()()()())()(()(")
    assert 0 == fn("(())")
    assert -1 == fn(")(")
