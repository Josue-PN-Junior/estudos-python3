# testar a variável

#entrada
print("~ Dissecando uma Variável ---------------------------")
v = input("Digite algo: ")

#testes e saída
print("~ Resultado -----------------------------------------")
print("É alfanúmerico?", v.isalnum())
print("É alfabético?", v.isalpha())
print("É ASCII?", v.isascii())
print("É um digito?",v.isdigit())
print("Está em letras minúsculas?", v.islower())
print("É um decimal?", v.isdecimal())
print("É def ou class??", v.isidentifier())
print("É um número?", v.isnumeric())
print("É printável?", v.isprintable())
print("É um espaço?", v.isspace())
print("É um título/capitalizado?", v.istitle())
print("Está em letras maiúsculas?", v.isupper())
# print(v.capitalize()) #Deixa capitalizado