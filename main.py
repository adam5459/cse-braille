valuemap = {
    'a': '@ n  n  ',
    'b': '@ n@ n  ',
    "c": '@@n  n  ',
    "d": '@@n @n  ',
    "e": '@ n @n  ',
    "f": '@@n@ n  ',
    "g": '@@n@@n  ',
    "h": ' @n@@n  ',
    'i': ' @n@ n  ',
    'j': ' @n@@n  ',
    "k": '@ n  n@ ',
    "l": '@ n@ n@ ',
    "m": '@@n  n@ ',
    'n': '@@n @n@ ',
    'o': '@ n @n@ ',    
    'p': '@@n@ n@ ',
    'q': '@@n@@n@ ',
    'r': '@ n@@n@ ',
    's': ' @n@ n@ ',
    't': ' @n@@n@ ',
    'u': '@ n  n@@',
    'v': '@ n@ n@@',    
    'w': ' @n@@n @',
    'x': '@@n  n@@',
    'y': '@@n @n@@',
    'z': '@ n @n@@',
    " ": '  n  n  ',
}
f,s,t = "", "", ""
word = input()
for letter in word:
    a,b,c = valuemap[letter].split("n")
    f+=a
    s+=b
    t+=c
print(f"{f}\n{s}\n{t}\n")
