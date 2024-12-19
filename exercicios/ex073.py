"""
    Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de
 colocação. Depois mostre:

 a) Os 5 primeiros times.
 b) Os últimos 4 colocados.
 c) Times em ordem alfabética.
 d) Em que posição está o time da Chapecoense.
"""
print("~ Tuplas com Times de Futebol", '-'*20)
times = ("Botafogo", "Palmeiras", "Flamengo", "Fortaleza", "Internacional",
         "São Paulo", "Corinthians", "Bahia", "Cruzeiro", "Vasco",
         "Vitória", "Atlético-MG", "Fluminense", "Grêmio", "Juventude",
         "Bragantino", "Athletico-PR", "Criciuma", "Atlético-GO", "Cuiabá")
print(f"Times: {times}")
print('- '*50)
print(f"Os cinco primeiros times: {times[:5]}")
print('- '*50 )
print(f"Os 4 últimos colocados: {times[-4:]}")
print('- '*50)
print(f"Times em ordem alfabética: {sorted(times)}")
print('- '*50)
for i, time in enumerate(times) :
    if time == "Chapecoense" :
        print(f"> Chapecoense foi encontrada na {i+1}ª posição")
        break
    elif i == 19:
        print("> Chapecoense NÃO foi encontrada!")

# forma Guanabara
if "Chapecoense" in times:
    print(f"> O Chapecoense está na {times.index("Chapecoense")+1}ª posição")
else :
    print("> Não a Chapecoense!")

