import random as rd

CHG=[[45.786747290,6.584905024],[45.296145373,6.203814104],[46.22749187434,6.73787216678],
[46.06017204079,6.72420508720],[45.55450277967,6.79828370116],[45.38248396809,7.00506331041],
[45.498768147636,6.899363817391],[46.28320191449,6.74254267588],[45.54984236442,6.91353739928],
[45.90217029841,6.47705530921],[45.94459229341,6.82959963610],[45.33147529241,6.88558093134],
[45.60469998853,6.91980902900],[45.78230630223,6.70066334193],[45.95795554778,6.48127237609],
[46.17258095769,6.73189198884]]
CBD=[[45.714873906,6.714413259],[45.226677867,6.329816394],[46.1573928263,6.8655054074],
[45.99006119732,6.85160570094],[45.48237917816,6.92699448095],[45.30080941808,7.15212645662],
[45.4172306706044,7.0468897684005],[46.21314561373,6.87002563247],[45.47758632303,7.04208671062],
[45.83114206987,6.60797059750],[45.87315660005,6.96015983940],[45.24995851118,7.03268458422],
[45.53445570868,7.04550475301],[45.71029960177,6.83000974038],[45.88692231036,6.61231466549],
[46.10052772837,6.86214541731]]

def generateur():
    aleat=[]
    for k in range(len(CHG)):
        for i in range (5):
            y=rd.randint(int(CHG[k][1]*1000),int(CBD[k][1]*1000))
            x=rd.randint(int(CBD[k][0]*1000),int(CHG[k][0]*1000))
            aleat.append([x/1000,y/1000])
    lea=[aleat[k] for k in range(26)]
    sam=[aleat[k+26] for k in range(26)]
    cyrian=[aleat[k+52] for k in range(28)]
    #print(aleat,len(aleat))
    print("lea=",lea)
    print("sam=",sam)
    print("cyrian=",cyrian)

generateur()
