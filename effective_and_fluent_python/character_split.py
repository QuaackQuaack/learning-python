#in python we deal with byte and str

def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8') # decode means bytes to str

    else:
        value = bytes_or_str
    return value
print(type(b'foo')) # this is bytes
print(type(repr(to_str(b'foo')))) # this is byte, but after function call, it is str
print(repr(to_str('boo')))


def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8') #encode means str to bytes
    else :
        value = bytes_or_str
    return value

print(type(to_bytes('bar')))
print(type(to_bytes(b'foo')))
