# teste 1

    """
    linha = len(grid)
    print(linha)
    for linha in range(linha) :
      linhaX = grid[linha]
      if linhaX.find('h') != -1 :
        print("A cabeça está nessa linha: ", linhaX)
        lista = List.(f"[{linha}, {linhaX.find('h')}]")
        print(f"[{linha}, {linhaX.find('h')}]")
    """
# quantidade de linhas
# qt_linhas = len(grid)
# print(qt_linhas)
"""
# linhas 
for linhaX in grid :
  qt_car = len(linhaX)
  print(qt_car)
  for LinhaY in linhaX :
    if LinhaY == 'h' :
      cabeca = LinhaY
      linhaXY = linhaX

print("Aqui a cabeça: ", cabeca)
print("Olha onde: ", linhaXY)
"""
print(grid.find('h'))

# fim teste 1

# teste 2
"""

    linha = len(grid)
    
    for linha in range(linha) :
      linhaY = grid[linha]
      if linhaY.find('h') != -1:
        lista = [[linhaY.find('h'), linha]]
        corpo = False
        # se cabeça já encontrada
      if ('<' or '>' or 'v' or '^') in linhaY :
        corpo = True

    ultimo = (lista[len(lista)-1])
    cordX = ultimo[0]
    cordY = ultimo[1]
    print(ultimo)
    print(grid[cordX][cordY])

    #teste 3
        if corpo:
      ultimo = (lista[len(lista)-1])
      cordX = ultimo[0]
      cordY = ultimo[1]
      if grid[cordX][cordY-1] == 'v' :
        print("Aqui! v ")
      if grid[cordX][cordY+1] == 'v' :
        print("Aqui! ^ ")
      if grid[cordX+1][cordY] == '<' : 
        print("Aqui! < ")
      if grid[cordX-1][cordY] == '>' :
        print("Aqui! > ")
    else : 
      return lista


"""
# fim teste 2

# teste 3
"""
from typing import List

def find_snake_on_grid(grid: List[str]) -> List[List[int]]:
    # Verificar se a cobra
    for busca in grid :
      if 'h' in busca :
        temCobra = True

    if not temCobra :
      return "0"
   
    linha = len(grid)
    
    for linha in range(linha) :
      corpo = False
      linhaY = grid[linha]
      if linhaY.find('h') != -1:
        lista = [[linhaY.find('h'), linha]]
        # se cabeça já encontrada
      if ('<' or '>' or 'v' or '^') in linhaY :
        corpo = True

     # cabeça já encontrada
    if corpo:
      ultimo = (lista[len(lista)-1])
      print(ultimo)
      cordX = ultimo[0]
      cordY = ultimo[1]
      
      if grid[cordY-1][cordX] == 'v' :
        print("Aqui! v ")
      if grid[cordY+1][cordX] == '^' :
        print("Aqui! ^ ")
      if grid[cordY][cordX+1] == '<' : 
        print(f"Aqui! < ")
      if grid[cordY][cordX-1] == '>' :
        print(f"Aqui! > ")
    
    else : 
      return lista

    return lista
"""
# fim teste 3

# teste 4
"""
    if corpo:
      ultimo = (lista[len(lista)-1])
      print(ultimo)
      cordX = ultimo[0]
      cordY = ultimo[1]
      
      if grid[cordY-1][cordX] == 'v' :
        print("Aqui! v ")
        
      elif grid[cordY+1][cordX] == '^' :
        print("Aqui! ^ ")
      elif grid[cordY][cordX+1] == '<' : 
        print(f"Aqui! < ")
      elif grid[cordY][cordX-1] == '>' :
        print(f"Aqui! > ")
        
      else :
        continuar = false
"""

# teste 5
"""
from typing import List

def find_snake_on_grid(grid: List[str]) -> List[List[int]]:
    # Verificar se a cobra
    for busca in grid :
      if 'h' in busca :
        temCobra = True

    if not temCobra :
      return []
     
    linha = len(grid)
    
    for linha in range(linha) :
      corpo = False
      linhaY = grid[linha]
      if linhaY.find('h') != -1:
        lista = [[linhaY.find('h'), linha]]
        # se cabeça já encontrada
      if ('<' or '>' or 'v' or '^') in linhaY :
        corpo = True

     # cabeça já encontrada
      while corpo:
        ultimo = (lista[len(lista)-1])
        print(ultimo)
        cordX = ultimo[0]
        cordY = ultimo[1]

        if grid[cordY-1][cordX] == 'v' :
          print("Aqui! v ")
          lista.append([cordY-1][cordX] )
          
        elif grid[cordY+1][cordX] == '^' :
          print("Aqui! ^ ")
          lista.append([cordY+1][cordX] )
          
        elif grid[cordY][cordX+1] == '<' : 
          print(f"Aqui! < ")  
          lista.append([cordY][cordX+1] )
          
        elif grid[cordY][cordX-1] == '>' :
          print(f"Aqui! > ")
          lista.append([cordY][cordX-1] )
          

        else :
          # parar while
          corpo = False
        corpo = False
        # fim while  
        

    return lista    
"""
# fim teste 5

# teste 6
"""
from typing import List

def find_snake_on_grid(grid: List[str]) -> List[List[int]]:
    # Verificar se a cobra
    for busca in grid :
      if 'h' in busca :
        temCobra = True
        lista = {}

    if not temCobra :
      return []
     
    linha = len(grid)
    
    for linha in range(linha) :
      corpo = False
      linhaY = grid[linha]
      if linhaY.find('h') != -1:
        lista.append([[linhaY.find('h'), linha]])
        print(lista[0])
        # se cabeça já encontrada
      if ('<' or '>' or 'v' or '^') in linhaY :
        corpo = True

     # cabeça já encontrada
      for i in range(3) :
      #while corpo:
        ultimo = lista[len(lista)-1]
        cordX = ultimo[0]
        cordY = ultimo[1]

        if  (cordY-1) >= (len(grid)-1):
          if  (grid[cordY-1][cordX] == 'v') :
            print("Aqui! v ")
            lista += ([cordY-1][cordX] )
          
        elif (cordY+1) <= (len(grid)-1) :
          if grid[cordY+1][cordX] == '^':
            print("Aqui! ^ ")
            lista += ([cordY+1][cordX])
          
        elif (cordX+1) >= (len(grid[0])-1) : 
          if grid[cordY][cordX+1] == '<' :
            print(f"Aqui! < ")  
            lista += ([cordY][cordX+1] )
          
        elif (cordX-1) <= (len(grid[0])-1):
          if grid[cordY][cordX-1] == '>':
            print(f"Aqui! > ")
            lista += ([cordY][cordX-1] )
          
        #corpo = False
        """
        else :
          # parar while
          corpo = False
        """
        # fim while  
        
    print(lista)
    return lista
"""
# fim teste 6

# teste 7
"""
from typing import List

def find_snake_on_grid(grid: List[str]) -> List[List[int]]:
    # Verificar se a cobra
    for busca in grid :
      if 'h' in busca :
        temCobra = True

    if not temCobra :
      return []
     
    linha = len(grid)
    
    for linha in range(linha) :
      corpo = False
      linhaY = grid[linha]
      if linhaY.find('h') != -1:
        lista = ([[linhaY.find('h'), linha]])
        # se cabeça já encontrada
      if ('<' or '>' or 'v' or '^') in linhaY :
        corpo = True

    # cabeça já encontrada
    #ultimo = lista[len(lista)-1]
    
   # cabeça já encontrada
    for i in range(3) :
    #while corpo:
      ultimo = lista[len(lista)-1]
      cordX = ultimo[0]
      cordY = ultimo[1]

      if  (cordY-1) >= (len(grid)-1):
        if  (grid[cordY-1][cordX] == 'v') :
          print("Aqui! v ")
          print("Num ", i, " : ", [cordY-1][cordX] )

      elif (cordY+1) <= (len(grid)-1) :
        if grid[cordY+1][cordX] == '^':
          print("Aqui! ^ ")
          print("Num ", i, " : ", [cordY+1][cordX])

      elif (cordX+1) >= (len(grid[0])-1) : 
        if grid[cordY][cordX+1] == '<' :
          print(f"Aqui! < ")  
          print("Num ", i, " : ", [cordY][cordX+1] )

      elif (cordX-1) <= (len(grid[0])-1):
        if grid[cordY][cordX-1] == '>':
          print(f"Aqui! > ")
          print("Num ", i, " : ", [cordY][cordX-1] )

      #corpo = False
      """
      else :
        # parar while
        corpo = False
      """
      # fim while  

    print(lista)
        
    return lista
"""
# fim teste 7

# teste 8
"""
from typing import List

def find_snake_on_grid(grid: List[str]) -> List[List[int]]:
    # Verificar se a cobra
    for busca in grid :
      if 'h' in busca :
        temCobra = True

    if not temCobra :
      return []
     
    linha = len(grid)
    
    for linha in range(linha) :
      corpo = False
      linhaY = grid[linha]
      if linhaY.find('h') != -1:
        lista = ([[linhaY.find('h'), linha]])
        # se cabeça já encontrada
      if ('<' or '>' or 'v' or '^') in linhaY :
        corpo = True

    # cabeça já encontrada
    #ultimo = lista[len(lista)-1]
    
   # cabeça já encontrada
    for i in range(3) :
      ultimo = lista[len(lista)-1]
      cordX = ultimo[0]
      cordY = ultimo[1]

      if (cordY-1) >= (len(grid)-1) and (grid[cordY-1][cordX] == 'v') :
      
      if  (cordY-1) >= (len(grid)-1):
        print("Achei 1!")
        if  (grid[cordY-1][cordX] == 'v') :
          print("Aqui! v ")
          print("Num ", i, " : ", [cordY-1][cordX] )

      if (cordY+1) <= (len(grid)-1) :
        print("Achei 2!")
        if grid[cordY+1][cordX] == '^':
          print("Aqui! ^ ")
          print("Num ", i, " : ", [cordY+1][cordX])

      if (cordX+1) >= (len(grid[0])-1) : 
        print("Achei 3!")
        if grid[cordY][cordX+1] == '<' :
          print(f"Aqui! < ")  
          print("Num ", i, " : ", [cordY][cordX+1] )

      if (cordX-1) <= (len(grid[0])-1):
        print("Achei 4!")
        if grid[cordY][cordX-1] == '>':
          print(f"Aqui! > ")
          print("Num ", i, " : ", [cordY][cordX-1] )

      #corpo = False
      
      else :
        print(f"{i} não achei!")
      
      # fim while  

    print(lista)
        
    return lista
"""
# fim teste 8

# teste 9
"""
from typing import List

def find_snake_on_grid(grid: List[str]) -> List[List[int]]:
    # Verificar se a cobra
    for busca in grid :
      if 'h' in busca :
        temCobra = True

    if not temCobra :
      return []
     
    linha = len(grid)
    
    for linha in range(linha) :
      corpo = False
      linhaY = grid[linha]
      if linhaY.find('h') != -1:
        lista = ([[linhaY.find('h'), linha]])
        # se cabeça já encontrada
      if ('<' or '>' or 'v' or '^') in linhaY :
        corpo = True

    # cabeça já encontrada
    #ultimo = lista[len(lista)-1]
    
    # cabeça já encontrada
    for i in range(10) :
      ultimo = lista[len(lista)-1]
      cordX = ultimo[0]
      cordY = ultimo[1]

      if (cordY-1) <= (len(grid)-1) :
        if (grid[cordY-1][cordX] == 'v') :
          print(f"Achei 1! rodada {i}")
          lista.append([cordX , cordY-1])

      if (cordY+1) <= (len(grid)-1) :
        if (grid[cordY+1][cordX] == '^'):
          print(f"Achei 2! rodada {i}")
          lista.append([cordX , cordY+1])

      if (cordX+1) <= (len(grid[0])-1) :
        if (grid[cordY][cordX+1] == '<') : 
          print(f"Achei 3! rodada {i}")
          lista.append([cordX+1 , cordY])
        
      if (cordX-1) <= (len(grid[0])-1) : 
        if (grid[cordY][cordX-1] == '>'):
          print(f"Achei 4! rodada {i}")
          lista.append([cordX-1 , cordY])
        
      else:
        print(f"Não achei! rodada {i}")


    print(lista)
        
    return lista
"""
# fim teste 9

# teste 10
"""
from typing import List

def find_snake_on_grid(grid: List[str]) -> List[List[int]]:
    # Verificar se a cobra
    for busca in grid :
      if 'h' in busca :
        temCobra = True

    if not temCobra :
      return []
     
    linha = len(grid)
    
    for linha in range(linha) :
      corpo = False
      linhaY = grid[linha]
      if linhaY.find('h') != -1:
        lista = ([[linhaY.find('h'), linha]])
        # se cabeça já encontrada
      if ('<' or '>' or 'v' or '^') in linhaY :
        corpo = True
    
    # cabeça já encontrada
    passar = len(grid) * len(grid[0])
    for caracater in range(passar) :
      ultimo = lista[len(lista)-1]
      cordX = ultimo[0]
      cordY = ultimo[1]

      if (cordY-1) <= (len(grid)-1) :
        if (grid[cordY-1][cordX] == 'v') :
          lista.append([cordX , cordY-1])

      if (cordY+1) <= (len(grid)-1) :
        if (grid[cordY+1][cordX] == '^'):
          lista.append([cordX , cordY+1])

      if (cordX+1) <= (len(grid[0])-1) :
        if (grid[cordY][cordX+1] == '<') : 
          lista.append([cordX+1 , cordY])
        
      if (cordX-1) <= (len(grid[0])-1) : 
        if (grid[cordY][cordX-1] == '>'):
          lista.append([cordX-1 , cordY])



    print(lista)
        
    return lista
"""
# fim teste 10