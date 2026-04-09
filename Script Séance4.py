# Importation des bibliothèques
import pandas as ps

# Affichage complet des lignes
# ps.set_option('display.max_rows',None)

# Importation CSV
sante = ps.read_csv('c:/Data/mesures.csv', sep=',')
# print(sante)

# Nettoyage des lignes vides
sante = sante.dropna()
# print(sante)

# Application des fonctions sur un DataFrame
# print(sante.mean())
# print(sante.max())
# print(sante.min())
# print(sante.count())
# print(sante.sum())

# Application des fonctions sur une colonne d'un DataFrame
# print("Moyenne Duration = ", sante["Duration"].mean())
# print("Max Calories = ", sante["Calories"].max())
# print("Min Pulse = ", sante["Pulse"].min())
# print("Nombre Maxpulse = ", sante["Maxpulse"].count())
# print("Somme Calories = ", sante["Calories"].sum())

''' Activité 2
print("La moyenne des calories consommées est : ", sante["Calories"].mean())
print("La pulsation minimale enregistrée est : ", sante["Pulse"].min())
print("La pulsation maximale enregistrée est : ", sante["Pulse"].max())
print("La somme est : ", sante.Calories[0:10].sum())
print("La somme est : ", sante.Calories.head(10).sum()) '''

# Tri
'''sante1 = sante.rename(index={170:180})
print(sante1)
sante1 = sante1.sort_index()
print(sante1)'''
'''sante2 = sante.sort_index(axis=1)
print(sante)
print(sante2)'''
'''sante3 = sante.sort_values(by=["Calories" ,"Duration"], ascending = [False, True])
print(sante)
print(sante3)'''

# Affichage des données d’un DataFrame selon une ou plusieurs conditions
# print(sante[sante["Calories"] >= 1000])
# print(sante["Calories"][sante["Calories"] >= 1000])
# print(sante[["Pulse", "Calories"]][sante["Calories"] >= 1000])
# print(sante[(sante["Pulse"]>=85) & (sante["Pulse"]<95)])
# print(sante[["Pulse","Calories"]][(sante["Pulse"]>=85) & (sante["Pulse"]<95)])

# Activité 3
# print("La nombre est : ", sante["Calories"][sante["Calories"]>400].count())
# print("La moyenne est : ", sante["Calories"][(sante["Pulse"]>=110) & (sante["Pulse"]<=115)].mean())

# Ajout d’une colonne remplie par des données suite à une condition simple
'''import numpy as np
sante ["Etat"] = np.where (sante["Calories"]>=400, "Elevée", "Normale")
print(sante)'''

# Exportation
# sante.to_csv ("health.csv", sep ="\t" , index = False , encoding ="utf-8-sig")

# Graphique
import  matplotlib.pyplot as plt
sante=sante.sort_values(by="Pulse", ascending=True)

sante.plot.scatter(x="Pulse", y="Calories", title="Consommation Calories en fonction des battements", color="green")
plt.tight_layout()
plt.show()

sante.plot.line(x="Pulse", y=["Duration", "Calories"], title="Consommation calories", color=["green", "red"],
                legend = True, figsize=(12,6), rot=45)
plt.tight_layout()
plt.savefig ("Fig1.png")
plt.show()
