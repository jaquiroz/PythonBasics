name = "Sally"
greeting = "Nice to meet you"
s = "Hello, {}. {}."

print(s.format(name,greeting)) # will print Hello, Sally. Nice to meet you.

print(s.format(greeting,name)) # will print Hello, Nice to meet you. Sally.

print(s.format(name)) # 2 {}s, only one interpolation item! Not ideal.