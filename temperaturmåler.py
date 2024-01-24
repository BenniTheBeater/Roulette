import matplotlib.pyplot as plt
import numpy as np
import statistics as stat

#Yr er den blåe streken i grafen og Storm er den røde

#xpoints er dagene, mens ypoints er hvilken temperatur det er
xpoints1 = np.array(["Ons.29.nov ","Tor.30.nov", "Fre.1.des", "Lør.2.des", "Søn.3.des", "Man.4.des", "Tir.5.des", "Ons.6.des", "Tor.7.des"])
ypoints1 = np.array([-1, -1, -4, -8, -4, -5, -2, -2, -3])
ypoints2 = np.array([-8, -10, -11, -11, -11, -6, -3, -8, -9])

#Her er spredningsmålene til Yr

print("Her er spredningstallene til Yr")


#Deler summen til temperaturen og deler på antall dager
average = ypoints1.sum() / xpoints1.size

#Regner ut typetallet
print("Typetallet til Yr sine temperaturer er", stat.mode(ypoints1))

#Regner ut gjennomsnittet
print("Gjennomsnittet til Yr er", average)

#Regner ut medianen
print("Medianen til Yr er", stat.median(ypoints1))

#Trenger dette for å regne ut variasjonsbredden
max = np.max(ypoints1)
min = np.min(ypoints1)

#Regner ut variasjonsbredden
variation = max - min
print("Variasjonsbredden til Yr er", variation)

#Under her er spredningsmålene til Storm

print("Her under er spredningsmålene til Storm")


#Deler summen til temperaturen og deler på antall dager
average = ypoints2.sum() / xpoints1.size

#Regner ut typetallet
print("Typetallet til Storm sine temperaturer er", stat.mode(ypoints2))

#Regner ut gjennomsnittet
print("Gjennomsnittet til Storm er", average)

#Regner ut medianen
print("Medianen til Storm er", stat.median(ypoints2))

#Trenger dette for å regne ut variasjonsbredden
max = np.max(ypoints2)
min = np.min(ypoints2)

#Regner ut variasjonsbredden
variation = max - min
print("Variasjonsbredden til Storm er", variation)

#Lager fonts til å ha på tittelen og labelsene
font1 = {"family":"serif","color":"black","size":20}
font2 = {"family":"serif","color":"black","size":17}

#legger forskjellige fonts på tittelen og labelsene
plt.title("Temperaturforskjeller", fontdict = font1)
plt.xlabel("Dager", fontdict = font2)
plt.ylabel("Temperatur", fontdict = font2)

#Fargene på linjene som viser temperaturene
plt.plot(xpoints1, ypoints1, color = "blue", label = "Yr")
plt.plot(xpoints1, ypoints2, color = "red", label = "Storm")

#Fargen på "griden", altså de linjene lagd av små linjer
plt.grid(color = "black", linestyle = "--", linewidth = 0.5)

plt.legend()
plt.show()

#Kilder var W3 schools