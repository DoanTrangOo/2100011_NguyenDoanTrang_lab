# python code to print even length words
n="geeks for geek"
s=n.split(" ")
print([x for x in s if len(x)%2==0])
