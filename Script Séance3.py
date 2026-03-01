# Importation des bibliothèques
import pandas as ps

# Affichage complet des lignes
# ps.set_option('display.max_rows',None)

# Importation CSV
sante = ps.read_csv('c:/Data/mesures.csv', sep=',')
#print(sante)

# Affichage des dimensions
# print("Les dimensions du DataFrame sont : ", sante.shape)

# Affichage du nombre d’éléments 
# print ("Le nombre d'éléments est : ", sante.size)

# Affichage des informations 
# print (sante.info())

# Affichage d'un résumé rapide
# print (sante.describe())

# Affichage des noms des colonnes
# print (sante.columns)

# Renommage des noms des colonnes/indices
# sante1 = sante.rename ( columns={"Duration":"c1"} )
# print(sante)
# print(sante1)

# sante2 = sante.rename ( index = {172 : "fin"} )
# print(sante)
# print(sante2)


# Suppression des colonnes
# aux1 = sante.drop ( columns = ["Duration", "Calories"] )
# print(sante)
# print(aux1)

# aux2 = sante.drop(["Pulse"], axis=1 )
# print(sante)
# print(aux2)

# Suppression des colonnes avec pop()
# s = sante.pop ( "Calories" )
# print(sante)
# print(s)

# Suppression des lignes
# aux1=sante.drop([0])
# aux2=sante.drop([0,5,100])
# print(aux1, aux2)
# aux3=sante.drop(sante.index[0:5])
# print(aux3)

# Affichage du contenu d’une colonne  
# print(sante.Duration) 
# print(sante["Duration"])

# Affichage du contenu de plusieurs colonnes
# print(sante[["Duration","Calories"]])

# Affichage du contenu d’une colonne entre 2 positions
# print(sante.Duration[0:10])

# Affichage du contenu d’une ligne
# print(sante.loc[0]) 

# Affichage du contenu des n premières lignes 
# print(sante.head(5))

# Affichage du contenu des n dernières lignes
# print(sante.tail(3))

# Affichage du contenu des lignes entre 2 positions 
# print(sante.loc[10:20])

# Affichage du contenu d’une cellule 
# print(sante.loc[3,'Pulse'])

# Modification du contenu d’un DataFrame
# sante.loc[0,"Maxpulse"]=132
# sante.loc[0]=[50,100,145,None]

# Ajout d'une colonne à un DataFrame
# sante["Test"]=50
# sante["Test"]=sante["Maxpulse"]-sante["Pulse"]

# Nettoyage d'un DataFrame
# sante1 = sante.drop_duplicates()
# print(sante.shape)
# print(sante1.shape)
# sante2 = sante1.dropna()
# print(sante1.shape)
# print(sante2.shape)
# sante3 = sante1.dropna(axis=1)
# print(sante1.shape)
# print(sante3.shape)