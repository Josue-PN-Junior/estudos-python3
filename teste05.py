def escolhe_taxi(tf1, vqr1, tf2, vqr2):
    # Empresa 1
    taxEmpreUm = float(tf1)
    valorKmUm = float(vqr1)
    print(taxEmpreUm)
    print(valorKmUm)

    # Empresa 2
    taxEmpreDois = float(tf2)
    valorKmDois = float(vqr2)
    print(taxEmpreDois)
    print(valorKmDois)

    # teste de kms
    testeKms = {
        1,
        10,
        30
    }

    # lista
    valorUm = []
    valorDois = []
    pontos = []

    # cálculos
    for kms in testeKms:
        valorUm.append(calculo(taxEmpreUm, valorKmUm, kms))
        valorDois.append(calculo(taxEmpreDois, valorKmDois, kms))

    # testes
    for indice in range(3):
        if valorUm[indice] == valorDois[indice]:
            pontos.append(0)
        elif valorUm[indice] < valorDois[indice]:
            pontos.append(1)
        else:
            pontos.append(2)

    print(pontos)

    # saída
    if pontos == [1, 1, 1]:
        msg = ("Empresa 1")

    elif pontos == [2, 2, 2]:
        msg = ("Empresa 2")

    elif pontos == [0, 0, 0]:
        msg = ("Tanto faz")

    else:
        if taxEmpreUm == 0.0:
            msg = (
                f"Empresa {pontos[0]} quando a distância < 7.14, Tanto faz quando a distância = 7.14, Empresa {pontos[2]} quando a distância > 7.14")
        else:
            msg = (
                f"Empresa {pontos[0]} quando a distância < 10.0, Tanto faz quando a distância = 10.0, Empresa {pontos[2]} quando a distância > 10.0")

    return msg


# função calculo
def calculo(taxa, valorKms, qt_kms):
    valor = taxa + valorKms * qt_kms
    return valor

"""
import unittest
from solution import escolhe_taxi
class Test(unittest.TestCase):
  def test_escolhe_taxi_teste(self):
    self.assertEqual(escolhe_taxi("2.5","1.0","5.0","0.75"), "Empresa 1 quando a distância < 10.0, Tanto faz quando a distância = 10.0, Empresa 2 quando a distância > 10.0")
"""