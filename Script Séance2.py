# Importation des bibliothèques
import pandas as ps
import numpy as np
import matplotlib.pyplot as plt

# Affichage complet
ps.set_option('display.max_rows',None)
ps.set_option('display.max_columns',None)
ps.set_option('display.max_colwidth',None)

# Création d'un DataFrame (Syntaxe1)
df1 = ps.DataFrame(columns = ['Prénom', 'Age', 'Ville'],
                   index = [1, 2, 3, 4],
                   data = [ ['Amine', 14, 'Sousse'],
                            ['Sarra', 15, 'Gafsa'],
                            ['Malek', 15, 'Bizerte'],
                            ['Ahmed', 13, 'Gabes'] ] )
#print(df1)

# Création d'un DataFrame (Syntaxe2)
df2 = ps.DataFrame({'Prénom':['Amine','Sarra','Malek','Ahmed'],     
         'Age':[14,15,15,13], 'Ville':['Sousse','Gafsa','Bizerte','Gabes']})
#print(df2)

# Création d'un DataFrame (Syntaxe3)
df3 = ps.DataFrame({'Prénom':['Amine','Sarra','Malek','Ahmed'],  
           'Age':[14,15,15,13], 'Ville':['Sousse','Gafsa','Bizerte','Gabes']},  
           index=['Candidat1','Candidat2','Candidat3','Candidat4'])
#print(df3)

# Création d'un DataFrame vide
df0 = ps.DataFrame()
#print(df0)

# Importation Excel
fifa = ps.read_excel ('c:/Data/fifa2018.xlsx','Equipes')
#print(fifa)

# Importation CSV
sante = ps.read_csv('c:/Data/mesures.csv', sep=',')
#print(sante)

# Importation Json
etudiant = ps.read_json('c:/Data/isimm.json')
#print(etudiant)

# Deactivation de l'affichage complet
ps.reset_option('display.max_rows')
ps.reset_option('display.max_columns')
ps.reset_option('display.max_colwidth')

# Activité
cereale = ps.DataFrame(columns = ['Nom', 'Prix'],
                       index = ['Code1', 'Code2', 'Code3', 'Code4'],
                       data = [ ['Blé Dur', 87.255], ['Blé Tendre', 67.732],
                                ['Orge', 56.500], ['Triticale', None] ] )
#print(cereale)

capt = ps.read_csv('c:/Data/capture.csv', sep=';')
#print(capt)
