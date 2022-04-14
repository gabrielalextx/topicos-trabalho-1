# -*- coding: utf-8 -*-
import py_compile
import unittest
import bissexto

class testBissexto (unittest.TestCase):
    
    def test_ct01(self):
        ano = 1999
        self.assertEqual(bissexto.Bissexto(ano), "INVÁLIDO")
    
    def test_ct02(self):
        ano = 2000
        self.assertEqual(bissexto.Bissexto(ano), "Bissexto")

    def test_ct03(self):
        ano = 2001
        self.assertEqual(bissexto.Bissexto(ano), "Ordinário")

    def test_ct04(self):
        ano = 10000
        self.assertEqual(bissexto.Bissexto(ano), "Bissexto")

    def test_ct05(self):
        ano = 10001
        self.assertEqual(bissexto.Bissexto(ano), "INVÁLIDO")

    def test_ct06(self):
        ano = 4515
        self.assertEqual(bissexto.Bissexto(ano), "Huluculu")
    
    def test_ct07(self):
        ano = 2420
        self.assertEqual(bissexto.Bissexto(ano), "Bissexto, Bulukulu")

    def test_ct08(self):
        ano = 3600
        self.assertEqual(bissexto.Bissexto(ano), "Bissexto, Huluculu")

    def test_ct09(self):
        ano = 2640
        self.assertEqual(bissexto.Bissexto(ano), "Bissexto, Huluculu, Bulukulu")

if __name__ == '__main__':
    unittest.main()