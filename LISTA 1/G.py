inp = int(input())
aux = inp

c100 = int(inp/100)
inp %= 100

c50 = int(inp/50)
inp %= 50

c20 = int(inp/20)
inp %= 20

c10 = int(inp/10)
inp %= 10

c5 = int(inp/5)
inp %= 5

c2 = int(inp/2)
inp %= 2

c1 = int(inp)

print("""
%d
%d notas de R$ 100,00
%d
%d
%d
%d
%d
%d
""" % (aux, c100, c50, c20, c10, c5, c2, c1))
