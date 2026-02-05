# Importation des bibliothèques
import pandas as ps
import numpy as np
import matplotlib.pyplot as plt

# Création de Series avec indices par défaut
s1 = ps.Series(['Amine', 10, 'Monastir'])

# Création de Series avec indices personnalisés
s2=ps.Series(['Amine', 10, 'Monastir'], index=['Prénom', 'Age', 'Ville'])

# Création de Series vide
s0=ps.Series()

# Affichage de tout le contenu d’une Series
print(s1)
print(s2)
print(s0)

# Affichage d'une valeur d’une Series
print(s1[0])
print(s1[[0]])
print(s2['Ville'])
print(s2[['Ville']])

# Affichage de valeurs multiples non successives
print(s1[[0,2]])
print(s2[['Prénom','Ville']])

# Affichage de valeurs multiples successives
print(s1[0:2])
print(s2['Prénom':'Ville'])

# Modification des données d’une Series
s3=ps.Series([10, 20, 30, 40], index = ['a', 'b', 'c', 'd'])
s3['c']=300
s3['z']=50
print(s3)

# Filtrage des données d’une Series
print(s3[s3>40])
print(s3[(s3<15) | (s3>150)])
print(s3[(s3>20) & (s3<100)])