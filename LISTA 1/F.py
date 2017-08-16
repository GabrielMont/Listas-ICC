inp = int(input())
hora = int(inp/3600)
inp -= hora*3600

minuto = int(inp/60)
inp -= minuto*60

segundo = inp

print('%dh:%dm:%ds' %(hora, minuto, segundo))
