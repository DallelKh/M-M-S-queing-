from math import *
fic=open("donnees.txt","r")
for ligne in fic :
 param = ligne.split()

s=int(param[0])
l=float(param[1])
uu=float(param[2])
print(s,l,uu)

def mu(k):
 return min(k,s);
def p(k):
 if (k==0):
       Sum=0
       ss = s - 1
       for k in range(0,ss): 
         Sum=+  (u**k)/factorial(k)
       Sum=+ (s*(u**s))/(factorial(s)*(s-u))
       return (1/Sum);
 elif (k<=s):
	   return ((u**k)*p(0)/factorial(k)); 
 elif (k>s):
           return( (u**k)*p(0)/(factorial(s)*(s**(k-s))));
 else:   print("probleme avec les donnees ")

u = l/uu 
ro = l/(s*uu)  


if (ro<1) : 
 nf= (ro*p(s))/((1-ro)**2)
 tf= nf/l
 ns= nf + u
 ts=ns/l
 proba=p(s)/(1-ro)
 fichier = open("resultats.txt", "w")
 fichier.write("\n le nf= ")
 fichier.write(str(nf))
 fichier.write("\n le tf= ")
 fichier.write(str(tf))
 fichier.write("\n le ns= ")
 fichier.write(str(ns))
 fichier.write("\n le ts= ")
 fichier.write(str(ts))
 fichier.write("\n la proba d attente est de  ")
 fichier.write(str(proba))
 fichier.close()
 print("calcul termine,veuillez verifier le fichier des resultats ",factorial(2),p(0),p(3))
else: print("le regime stationnaire n existe pas  (ro>>>1)")


