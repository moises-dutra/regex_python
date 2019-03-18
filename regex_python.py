#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 15:39:04 2019

@author: moises
"""

import re

nome_arquivo = '   ' #defina aqui o arquivo no qual será executada a mineração

arquivo = open(nome_arquivo, 'r')
texto = arquivo.read()
arquivo.close()

print ('\n##### Início do arquivo: #####')
print (texto)
print ('##### Fim do arquivo: #####\n')
       
regex = r'    ' #defina aqui a expressão regular a ser pesquisada

print ("regex:", regex)

lista = re.findall(regex, texto, re.MULTILINE)

if (lista):
  print("Sequência encontrada!")
else:
  print("Sequência NÃO encontrada!")

print ("\nQuantidade de elementos:", len(lista))
print (lista)

