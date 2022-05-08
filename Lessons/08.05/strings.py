# print(type(""))

s = "my very long string"
print(len(s))

print(s[0], s[1], s[2], s[3], s[4], sep=',')

print(s[len(s)-1])
print(s[-1], s[-2], s[-19])

print(s[1:7], s)

print(s[3:-3])

print(s[::-1])

# s[0] = 't'

# s[2.5]

s = "my " + "very " + "long " + "string"
print(s)

# s = "test"*8
# print(s)

print("my  " in s)
print(s.find('y'), s[s.find('y')])
print(s.find('long'), s[s.find('long')])
print(not not s.find('!'))

s = s.replace("my", "My")
print(s.replace(' ', '_'))
print(s[1:10].replace(' ','-') + s[10:])

print(s.upper().lower(), s)

print(s.split())
sku = "2345-adidas-g75"
info = sku.split('-')
print(info[0], info[1], info[2])

sku = "2345:adidas-g75"
print(sku.replace(':', '-').replace('-','_'))
info = sku.replace(':', '-').replace('-','_').split('_')
print(info[0], info[1], info[2])

print('_--_'.join(s.split()))

s = "My_--_very_--_long_--_string"
print(s.split('_--_'))

print('/'.join(["C:", "My documents", "Images"]))

print(type(str(2020)))

c = 'cat'
d = 'dog'
p = 'parrot'

"a cat, a dog and a parrot"
print("a " + c + ", a " + d + " and a " + p)
"a cat"
"a cat, a "
"a cat, a dog"
"a cat, a dog and a "
"a cat, a dog and a parrot"

print("a {}, a {} and a {}".format(c, d, p))
print("a {1}, a {2} and a {0}".format(c, d, p))
print("a {c}, a {d} and a {p}".format(c="camel", d="dino", p="pinguin"))

print(f"a {c}, a {d} and a {p}")
print(f"your answer is {'positive' if 13 + 4 - 144**0.5 > 0 else 'negative'}")

x = f"""line {12-11}
line {4**0.5}
line {9/3}"""

print(x)

print(len("some test\n string"))
print(len(r"some test\n string"))
print(r"C:\Projects\IT Academy\Python\Md-PT1-48-22\repo\Md-PT1-48-22\Lessons\08.05")