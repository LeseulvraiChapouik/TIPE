##importations
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as img
#import matplotlib.patches as patches
import ee
#ee.Authenticate()
ee.Initialize()
import math 
#global lat1,lon1,lat2,lon2,lx,ly,largeur,hauteur

#---------------Récupération de la carte CLPA------------------------------------------------------------------------------------

#ouverture d'une carte
filename='CLPA_AJ65.jpg' #nom du fichier
filedir='/Users/cyrian/Desktop/SpéBio1/TIPE/Cartes CLPA/' #emplacement du fichier
imgfile=filedir+filename
matriceCLPA=np.array(Image.open(imgfile).convert('RGB')) #convertion de la carte en matrice
ly,lx,bin=matriceCLPA.shape #renvoie la taille de l'image en pixel, bin = transparance de l'image (inexploitée ici)

#recupération des coordonées GPS
lat1=45.95795554778 #latitude coin haut gauche 
lon1=6.48127237609 #longitude coin haut gauche
lat2=45.88692231036 #latitude coin bas droit
lon2=6.61231466549 #longitude coin bas droit
largeur=lon2-lon1
hauteur=lat1-lat2

#convertion des coord de pixel en coord GPS
def coordGPS(x,y): 
    lat=lat1-y*(hauteur/ly)
    lon=lon1+x*(largeur/lx)
    return (lat,lon)
  

#---------------Sélection d'un polygone contenant la coulée sur la CLPA---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# on souhaite récupérer que les point rose/rouge correspondant à une coulée 
# l'utilisation d'un polygone permet de gagner du temps car le détourage nécessite moins de précision 

while True: #tant qu'on ne fait rien la carte reste affichée 
    data = [] #coord en pixel des points du polygone
    while len(data) < 3:
        image = img.imread(imgfile) #ouverture carte CLPA
        fig,ax = plt.subplots(frameon=False) #conversion en figure sans "frame" (=grille)
        fig.set_size_inches(lx/767,ly/767) # 1 pixel de la figure = 1 pixel de la CLPA
        ax.imshow(image,cmap="gray") # affichage image CLPA
        data = np.asarray(plt.ginput(-1, timeout=-1)) #entre matrice dans data, plt.ginput = tracer pts, "-1" = on peut faire autant de pts qu'on veut, appuie sur entrée arrête ginput
       
    # Le polygone apparait bleu sur la figure après avoir été dessiné sur l'image (la figure sert de calque, seule la figure est modifiée)
    counter = plt.fill(data[:, 0], data[:, 1], facecolor=(0,0,1), edgecolor='#000000', linewidth= 0.1) #forme polygone dont 4pts sont les angles et le remplis en bleu
    plt.axis('off')
  
   # plt.figure(figsize=(ly/1000, lx/1000), dpi=96) #met a l'echelle la figure
    plt.draw()#affichage polygone
    plt.savefig('polygone.jpg',dpi=1000,bbox_inches='tight',pad_inches=0)#sauvegarde figure tracée sur une figure, dpi = nb pixel par pouce, bbox et pad sauv sans bordures
    
    #sortie de la carte en appuyant sur une touche de clavier
    if plt.waitforbuttonpress():
        break   

polygone=Image.open('polygone.jpg')
#polygone.show() 


#---------------Sélection de la coulée dans le polygone, obtention de la liste des coordonées GPS des points de la coulée---------------------------------------------------------------------------------
# On récupère les coordonnées GPS des points rouges situés sous le polygone bleu

#def des couleurs sélectionnées (varie selon les cartes)
ri,gi,bi=180,50,50 #borne inf
rs,gs,bs=255,100,100 #borne sup

precoulée=[]
 
matricePoly=np.array(polygone) #figure=>image=>matrice
CLPAcopie=matriceCLPA.copy() #pour pouvoir la modifier

for x in range(lx): 
    for y in range(ly):
        color=matricePoly[y,x,] # recupération couleur sous forme de liste du polygone en un point (y,x)
        r,g,b = color[0],color[1],color[2]
        if r<10 and g<10 and b>245: #si le point appartient au polygone bleu
            color=matriceCLPA[y,x,] # recupération couleur sous forme de liste du point (y,x) sur la CLPA
            r,g,b=color[0],color[1],color[2]
            if ri<r<rs and gi<g<gs and bi<b<bs:
                 CLPAcopie[y,x,]=[255,0,0]
                 precoulée.append(coordGPS(x,y)) #si bleu dans matricePoly et rouge dans matriceCLPA alors le point appartient à la coulée sélectionnée
            else:
                 CLPAcopie[y,x,]=[255,255,255] #sinon le point devient blanc
       
        else:
            CLPAcopie[y,x,]=[255,255,255] #sinon le point devient blanc devient blanc

#Vérification coulée sélectionnée et séparée des autres
image=Image.fromarray(CLPAcopie) #CLPAcopie tous pts sélectionnés = rouges, les autres = blancs
image.show()

#on prend un point sur 10 pour former la liste coulée
coulée=[]
for k in range (0,len(precoulée),20):
    coulée.append(precoulée[k])

print(coulée)
print(len(coulée))


#-----------------Traitement de la liste 'coulée' obtenue---------------------------------------------------------------------------------


#données ee d'altitude:

def zpt(x,y): #return l'altitude pour un pt de coordonnées (x,y)    
    alt=ee.Image('USGS/SRTMGL1_003')
    u=ee.Geometry.Point(y,x) #longitude,latitude dans l'ordre
    scale=1 #en mètre
    z=alt.sample(u,scale).first().get('elevation').getInfo()
    return z 


def recupente(coulée): #nécessaire pour délimiter les 3 tronçons de la coulée
    Lalt=[] #liste des altitudes de chaque point
    for coord in coulée: #trouve zmin et z max
        x,y= coord
        print("alt=",zpt(x,y))
        Lalt.append(zpt(x,y))
    Laltcopy=sorted(Lalt)
    zmax,zmin=max(Lalt),min(Lalt)
    deltaz=zmax-zmin
    z1tiers=int(zmin+(2/3)*deltaz)
    z1tiers=Laltcopy[int(2*len(Laltcopy)/3)]
    i,j,k=Lalt.index(zmax),Lalt.index(zmin),Lalt.index(z1tiers) #pb si coulée large on a un point du bord de la coulée 
    (xmax,ymax)=coulée[i] #x=lat , y=lon
    (xmin,ymin)=coulée[j]
    (x1tiers,y1tiers)=coulée[k]
    print(x1tiers,y1tiers)
    
    deltay=(ymax-ymin)*40000000*math.cos(math.radians(xmin))/360
    deltax=111111*(xmax-xmin)
    deltay1tiers=(ymax-y1tiers)*40000000*math.cos(math.radians(x1tiers))/360
    deltax1tiers=111111*(xmax-x1tiers)
    d=(deltay**2+deltax**2)**0.5
    d1tiers=(deltay1tiers**2+deltax1tiers**2)**0.5
    
    pente=math.degrees(math.atan((zmax-zmin)/d)) #calcule la pente de chaque coulée
    pente1tiers=math.degrees(math.atan((zmax-z1tiers)/d1tiers))
    print("distance=",d)
    print('pente,pente1tiers,deltaz = ',pente,pente1tiers,deltaz)
    return (pente,pente1tiers,deltaz,d,zmin,zmax) #différence d'altitude 

def analyse(coulée): #renvoie la densité d'arbres par tronçon d'une coulée + dtot + pente
    fnf=ee.ImageCollection("JAXA/ALOS/PALSAR/YEARLY/FNF")
    a1,a2,a3= 0,0,0 #nb arbres par tronçon
    n1,n2,n3=0,0,0 #nb total de pts par tronçon
    pente,pente1tiers,deltaz,distance,zmin,zmax=recupente(coulée) 
    div=deltaz/3 #divise la coulée en 3 tronçons
    for coord in coulée:
        x,y=coord
        point = ee.Geometry.Point(y,x) #longitude,latitude
        arbreannée=fnf.getRegion(point,1).getInfo() # arbre liste de listes d'info par années
        if zpt(x,y)<=div+zmin: #1er tronçon
            n1+=1
            if arbreannée[1][-1]==1: #arbre[1][-1] on recuperer le dernier terme (info présence arbre) 1ere année
                a1+=1
        elif div+zmin<zpt(x,y)<2*div+zmin: #2ème tronçon
            n2+=1
            if arbreannée[1][-1]==1:
                a2+=1
        else:               #3ème tronçon
            n3+=1
            if arbreannée[1][-1]==1:
                a3+=1
        print('tronçon:',n1,n2,n3)
    dataCoulée=[a1/n1,a2/n2,a3/n3,(a1+a2+a3)/(n1+n2+n3),pente,pente1tiers,deltaz,distance,zmin,zmax]#(darbre1ertronçon, darbre2emetronçon, darbre3emetronçons,d totale, pente, dénivelé, longueur coulée, alt min, alt max)

    return dataCoulée 

print('dataCoulée=',analyse(coulée))
