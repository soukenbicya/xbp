import random
a = random.randint(0, 255)
b = random.randint(0, 255)
c = random.randint(0, 255)

R = a
G = b
B = c
color_code = '#{}{}{}'.format(hex(R), hex(G), hex(B))
color_code = color_code.replace('0x', '')
print (R,G,B)