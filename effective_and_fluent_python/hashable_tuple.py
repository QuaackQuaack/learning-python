# hashable object means a object whoose value never changes during a life time

def fixed(O):
    try:
        hash(O)
    except TypeError:
        return False
    return True

tf = (10,11)
tfd = [10,11]
print(fixed(tf))
print(fixed(tfd))
