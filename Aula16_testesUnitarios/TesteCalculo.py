import unittest


from Calculo import *


class TesteCalculo_soma( unittest.TestCase ):
        def testeSomar(self):
            self.assertEqual(Calculo.somar(2, 5), 7)

        def testeSomarErrado(self):
            self.assertEqual(Calculo.somar(2,5), 9)


class TesteCalculo_diminuir(unittest.TestCase):
    def testeDiminuir(self):
        self.assertEqual(Calculo.diminuir(10, 5), 5)

    def testeDiminuirDiminuir(self):
        self.assertEqual(Calculo.diminuir(2, 5), 20)





class TesteCalculo_dividir(unittest.TestCase):
    def testeDiminuir(self):
        self.assertEqual(Calculo.dividir(10, 5), 2)

    def testeDiminuirErrado(self):
        self.assertEqual(Calculo.diminuir(2, 5), 20)



class TesteCalculo_multiplicar( unittest.TestCase ):
        def testeMultiplicar(self):
             self.assertEqual(Calculo.multiplicar(2, 5), 10)

        def testeMultiplicarErrado(self):
            self.assertEqual(Calculo.somar(2, 5), 20)





