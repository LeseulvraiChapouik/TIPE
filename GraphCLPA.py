import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

#longueur coulée = f(d arbre , pente)
#nb coulée = f(d arbre , pente)
#d arbre = f(pente , alt max)

Data=[[1.0, 0.07650273224043716, 0.0, 0.21608040201005024, 29.11887775559068, 38.08291850418205, 662, 1188.457622528473, 1196, 1858], [1.0, 0.5625, 0.0, 0.4444444444444444, 31.207670224424803, 31.470817296759943, 316, 521.6204123498161, 1232, 1548], [1.0, 0.8431372549019608, 0.0, 0.5272727272727272, 32.079593255301745, 38.51302008188361, 799, 1274.7234707749706, 1108, 1907], [1.0, 0.6151685393258427, 0.7533875338753387, 0.7327080890973037, 24.283025105614527, 31.15286859882105, 427, 946.4476984724582, 1438, 1865], [0.007142857142857143, 0.0, 0.0, 0.0045871559633027525, 25.088479741161127, 36.780794881557455, 308, 657.8538933872748, 1824, 2132], [0.036585365853658534, 0.0, 0.0, 0.012, 23.54104098603282, 21.102457049228114, 310, 711.5569330737654, 1618, 1928], [0.0, 0.0, 0.0, 0.0, 30.565843916888422, 25.851846406333625, 206, 348.80137685032224, 1729, 1935], [0.0, 0.0, 0.0, 0.0, 36.36650517244682, 31.579719255900066, 246, 334.074989958095, 1739, 1985], [0.0, 0.0, 0.0, 0.0, 26.60604059315036, 41.94959291850707, 569, 1135.9675938559635, 1730, 2299], [0.0, 0.0, 0.0, 0.0, 39.43297772859761, 49.25837033738022, 340, 413.4373806768667, 1752, 2092], [0.0, 0.0, 0.0, 0.0, 33.53749545571398, 28.23359992999491, 197, 297.21175345360007, 1619, 1816], [0.0, 0.0, 0.15151515151515152, 0.08450704225352113, 25.806663235342718, 25.897374672163597, 386, 798.2424289270773, 1866, 2252], [0.0, 0.0, 0.0, 0.0, 26.433670120972575, 40.00335862554407, 711, 1430.1892997795348, 2699, 3410], [0.0, 0.0, 0.0, 0.0, 25.654691175350592, 24.234050960350825, 435, 905.6954121310987, 2802, 3237], [0.5384615384615384, 0.01606425702811245, 0.0, 0.04641775983854692, 26.833374526888345, 26.39578793240221, 1253, 2476.9322594243704, 1444, 2697], [0.2, 0.0, 0.0, 0.002066115702479339, 27.21519891637165, 28.310083468014632, 1341, 2607.6021235607905, 1730, 3071], [0.725, 0.028368794326241134, 0.0, 0.047042052744119746, 28.18692003889227, 32.55531169974958, 1528, 2851.2707274715412, 1453, 2981], [0.22809457579972184, 0.30656934306569344, 0.0, 0.18674698795180722, 25.03264073081631, 25.811485168167252, 927, 1985.0047330593095, 1470, 2397], [0.0, 0.0, 0.0, 0.0, 24.902669210668346, 17.408478498482545, 310, 667.7563719161053, 2109, 2419], [0.24154589371980675, 0.015345268542199489, 0.0, 0.06015037593984962, 26.520069038665167, 27.006522006831172, 1193, 2390.6904062067474, 1454, 2647], [0.0, 0.0, 0.0, 0.0, 25.307065343306764, 28.783177465023776, 886, 1873.7494269730248, 2307, 3193], [0.0, 0.0, 0.0, 0.0, 27.746537021478307, 46.174840111659165, 734, 1395.3091825523472, 2453, 3187], [0.10869565217391304, 0.07894736842105263, 0.0, 0.05701754385964912, 35.4192001307535, 40.95522288666176, 448, 629.9500669860529, 1698, 2146], [0.453125, 0.0, 0.0, 0.17261904761904762, 30.025565439292365, 32.197478929696786, 719, 1244.062247224729, 2178, 2897], [0.9333333333333333, 0.0, 0.0, 0.15155615696887687, 28.65200202059337, 32.423260233914036, 873, 1597.7432140874523, 2008, 2881], [1.0, 1.0, 0.7718120805369127, 0.8645418326693227, 25.935401980684162, 30.815857940595368, 773, 1589.4305343364192, 1687, 2460], [0.9607843137254902, 0.010416666666666666, 0.0, 0.096045197740113, 23.455973344864038, 23.486939716485903, 557, 1283.708902659274, 2024, 2581], [0.0, 0.0, 0.0, 0.0, 28.881828379039657, 36.539518344312604, 916, 1660.5756927323089, 2318, 3234], [0.9878542510121457, 0.12545454545454546, 0.0, 0.3351177730192719, 31.33664393887861, 36.74514646096158, 1102, 1809.8630259492893, 1747, 2849], [1.0, 0.17905405405405406, 0.0, 0.26727509778357234, 31.672658343395916, 36.68052029941769, 1273, 2063.3644014416764, 1692, 2965], [0.6674364896073903, 0.006472491909385114, 0.0, 0.2623985572587917, 32.83540253031886, 30.545460713953524, 1349, 2090.4004872831874, 1929, 3278], [0.9632352941176471, 0.0, 0.0, 0.1585956416464891, 28.75152040699126, 30.105118259152423, 1518, 2766.7745221541177, 1759, 3277], [1.0, 1.0, 1.0, 1.0, 27.327319557645712, 0, 298, 576.6895773893963, 1407, 1705], [1.0, 1.0, 1.0, 1.0, 25.8152051065823, 0, 227, 469.254209201097, 1526, 1753], [1.0, 1.0, 0.8914728682170543, 0.9828850855745721, 26.611432920489268, 0, 386, 770.4401627985894, 1619, 2005], [0.8007736943907157, 0.021897810218978103, 0.0, 0.2484186313973548, 24.441913671183837, 0, 512, 1126.5065271875685, 1648, 2160], [1.0, 0.3333333333333333, 0.004975124378109453, 0.34054054054054056, 36.982329845182726, 0, 445, 590.9140244013871, 1497, 1942], [1.0, 1.0, 1.0, 1.0, 24.19515966363186, 23.216022359178435, 511, 1137.2835169805332, 1129, 1640], [1.0, 0.6368159203980099, 0.39444444444444443, 0.6367265469061876, 21.422266393762616, 25.24032071241702, 477, 1215.769554916826, 1443, 1920], [1.0, 0.8695652173913043, 0.02054794520547945, 0.1797752808988764, 29.02402458194629, 34.93961698108566, 567, 1021.8843233189739, 1256, 1823], [0.7887323943661971, 1.0, 1.0, 0.9044585987261147, 32.2758942875134, 39.38607057832354, 509, 805.9088788803509, 1176, 1685], [1.0, 1.0, 1.0, 1.0, 31.58125447477177, 33.751182654667495, 489, 795.441165179226, 1181, 1670], [0.8378378378378378, 1.0, 1.0, 0.9285714285714286, 32.11798207008815, 40.58206146275069, 579, 922.3619001361305, 1184, 1763], [0.03773584905660377, 0.19736842105263158, 0.0, 0.09444444444444444, 26.815395055402444, 37.87214818399684, 372, 735.9434080799755, 1182, 1554], [1.0, 0.6, 0.5955056179775281, 0.6770186335403726, 23.608989709881502, 22.99874811401482, 520, 1189.724119647595, 1234, 1754], [0.9375, 1.0, 1.0, 0.9761904761904762, 31.689203396158852, 33.07013665253593, 537, 869.8436804354059, 1195, 1732], [0.9259259259259259, 1.0, 1.0, 0.9577464788732394, 33.856944835497984, 41.560797513471556, 369, 550.0222979037253, 1214, 1583], [0.0, 0.024734982332155476, 0.0, 0.009446693657219974, 30.165641777613367, 32.736983289457065, 955, 1643.1199157978149, 1703, 2658], [0.343804537521815, 0.0, 0.0, 0.11257142857142857, 25.454477071857315, 28.175551344533154, 1550, 3256.2982929862283, 1698, 3248], [0.0, 0.0, 0.0, 0.0, 33.900402126135205, 43.47672061581084, 1258, 1872.0731170432598, 2326, 3584], [0.0, 0.0, 0.0, 0.0, 26.2369858448712, 28.79360106450345, 1027, 2083.7430181628797, 2223, 3250], [0.0, 0.0, 0.0, 0.0, 32.33081071461093, 33.40519174793148, 485, 766.2815031170927, 2286, 2771], [0.0, 0.0, 0.0, 0.0, 26.715002574086558, 14.421673347561565, 618, 1227.9551110328453, 2416, 3034], [0.0, 0.0, 0.0, 0.0, 29.032115648205416, 38.85750688412876, 515, 927.8576635453549, 2896, 3411], [0.0, 0.0, 0.0, 0.0, 30.080833038001785, 32.62146130611792, 1489, 2570.6413890276917, 1629, 3118], [0.0, 0.0, 0.0, 0.0, 28.935559470644733, 24.461759057058057, 580, 1049.1287190645874, 2269, 2849], [1.0, 1.0, 0.8125, 0.9338235294117647, 18.533719253960488, 15.393321512040608, 284, 847.1293954316025, 1790, 2074], [1.0, 0.6031746031746031, 1.0, 0.8922413793103449, 26.631935585370233, 28.869875059737826, 455, 907.3504563025957, 1575, 2030], [0.0, 0.0, 0.0, 0.0, 31.406134236065984, 37.62657995525258, 319, 522.4800995364327, 2633, 2952], [0.0, 0.0, 0.0, 0.0, 32.97971634076483, 27.021589531306937, 356, 548.6170289486705, 1712, 2068], [0.0, 0.0, 0.0, 0.0, 27.274810784760458, 33.73856708483356, 760, 1474.0627196039925, 2707, 3467], [1.0, 1.0, 1.0, 1.0, 30.862870399019446, 30.38281935556207, 392, 655.9485528472012, 1432, 1824], [1.0, 1.0, 1.0, 1.0, 30.34103173306091, 23.483018097405726, 339, 579.1764055676572, 1551, 1890], [1.0, 1.0, 1.0, 1.0, 27.473320928720884, 35.064604809956855, 371, 713.4953291532424, 1369, 1740], [1.0, 1.0, 1.0, 1.0, 29.90426351785165, 28.177590777933926, 295, 512.9323947675082, 1331, 1626], [1.0, 1.0, 1.0, 1.0, 35.15977703056434, 51.92795850944911, 313, 444.3677446110143, 1424, 1737], [0.08139534883720931, 1.0, 1.0, 0.38996138996138996, 26.646718202296093, 36.14264976729825, 367, 731.391900376117, 1508, 1875], [0.875, 1.0, 1.0, 0.9230769230769231, 27.276347768283056, 44.30688263009215, 215, 416.9771226090822, 1508, 1723], [1.0, 1.0, 1.0, 1.0, 34.444790202356685, 36.91323997716482, 312, 454.9012461648871, 1245, 1557], [1.0, 1.0, 1.0, 1.0, 30.78203509913385, 34.00676859297707, 350, 587.5492423807652, 1183, 1533], [1.0, 1.0, 1.0, 1.0, 29.907146334214463, 34.443377392633444, 511, 888.399800737495, 1043, 1554], [1.0, 1.0, 1.0, 1.0, 34.444790202356685, 36.91323997716482, 312, 454.9012461648871, 1245, 1557], [0.7391304347826086, 0.2421875, 0.0, 0.16308040770101925, 22.1265226268154, 25.51745211515837, 484, 1190.3671948456074, 1802, 2286], [0.0, 0.0, 0.0196078431372549, 0.006430868167202572, 22.54643678685163, 22.563620141752196, 298, 717.7896499253669, 1901, 2199], [0.0, 0.2012779552715655, 0.8424657534246576, 0.23876765083440307, 26.33396505185897, 20.73981644847759, 319, 644.4853244813406, 2165, 2484], [0.0, 0.2138728323699422, 0.25757575757575757, 0.1377551020408163, 24.976650884947343, 22.128506163376205, 324, 695.560147336711, 2169, 2493], [0.0, 0.0, 0.0, 0.0, 17.490236785668074, 20.329804408774844, 205, 650.5634573778522, 2164, 2369], [1.0, 1.0, 1.0, 1.0, 31.701433647153674, 38.38184769940293, 764, 1236.9521888806958, 1091, 1855], [1.0, 1.0, 1.0, 1.0, 28.30155631650655, 37.11989307881738, 780, 1448.5229432981293, 1060, 1840], [1.0, 1.0, 0.9512317747611865, 0.9858104154476302, 27.245309399857355, 22.738922430213655, 1314, 2551.801842726056, 1097, 2411], [1.0, 1.0, 1.0, 1.0, 38.351571505732295, 43.94795404413086, 470, 594.0231608680587, 1423, 1893], [0.9696428571428571, 1.0, 1.0, 0.9822916666666667, 33.31873687189899, 37.826730714980215, 1134, 1725.1203351497804, 1044, 2178], [0.003484320557491289, 0.0, 0.0, 0.0021551724137931034, 32.38603801546554, 37.36457767276067, 357, 562.8451032805661, 1737, 2094], [1.0, 0.8823529411764706, 0.578125, 0.7586206896551724, 31.78217130052596, 32.19373129533759, 702, 1132.9971461509986, 1241, 1943], [0.780373831775701, 0.13414634146341464, 0.0, 0.25, 31.106946715477928, 32.16801502112253, 1208, 2001.9756521357237, 1140, 2348], [0.7532467532467533, 0.3954022988505747, 0.0, 0.24552429667519182, 31.53120973916093, 33.52863407795965, 977, 1592.371470183961, 1119, 2096], [1.0, 0.9195402298850575, 0.3137254901960784, 0.7915632754342432, 29.390257551216692, 38.962371654324485, 514, 912.5658281887391, 1614, 2128], [0.6712328767123288, 0.0, 0.0, 0.33793103448275863, 33.10505175498738, 44.05124350274924, 655, 1004.5743490905553, 1509, 2164], [0.811965811965812, 0.2847222222222222, 0.0, 0.4236760124610592, 40.836153858343536, 43.2363097856482, 647, 748.6012084999653, 1621, 2268], [0.5675675675675675, 1.0, 1.0, 0.896774193548387, 37.782704098618304, 36.12892961080731, 422, 544.3783663325256, 1106, 1528], [0.0, 0.0, 0.0, 0.0, 32.031082472642545, 23.57493947844676, 417, 666.5346156508847, 1827, 2244], [0.415625, 0.0015625, 0.0, 0.08880053015241882, 27.190511176993727, 31.753195581812136, 947, 1843.4135748840586, 1377, 2324], [0.4377880184331797, 0.3097560975609756, 0.0, 0.23360353721444363, 25.887094479653808, 29.00792227170801, 1125, 2318.174791757032, 1371, 2496], [0.10945273631840796, 0.0, 0.0, 0.021568627450980392, 25.822053953736905, 20.747823754502406, 923, 1907.4431594533537, 1495, 2418], [0.0, 0.22807017543859648, 0.21621621621621623, 0.09830508474576272, 29.03738429656922, 35.01048812810301, 374, 673.6768458553909, 1543, 1917], [0.0, 0.0, 0.0, 0.0, 29.408762266388674, 30.364394112261955, 674, 1195.7296950509829, 1555, 2229], [0.0, 0.11320754716981132, 0.0, 0.0379746835443038, 29.824173398913562, 30.854721469641326, 529, 922.7830781901599, 1547, 2076], [0.0, 0.0, 0.0, 0.0, 34.76829331277746, 40.4257761046482, 989, 1424.6661565825448, 1570, 2559], [0.0, 0.0, 0.0, 0.0, 26.48068122373725, 27.08372857092028, 429, 861.1679163204362, 2154, 2583], [0.0, 0.0, 0.0, 0.0, 28.3743241940685, 32.96089450024538, 429, 794.2694346633305, 2163, 2592], [0.0, 0.0, 0.0, 0.0, 32.55775120151913, 33.965754460475814, 336, 526.2430807644772, 2238, 2574], [0.0, 0.0, 0.0, 0.0, 29.76352133016294, 37.17253532682215, 331, 578.8127817845477, 2220, 2551], [0.0, 0.0, 0.0, 0.0, 24.839644214132814, 32.70666522904581, 295, 637.2800784006429, 2360, 2655], [0.0, 0.0, 0.0, 0.0, 17.16909033429048, 12.46240302043373, 99, 320.42916642870387, 2078, 2177], [0.213768115942029, 0.0, 0.0, 0.05432780847145488, 32.01818629830179, 28.74518764830849, 458, 732.4357895427405, 1793, 2251], [0.10204081632653061, 0.0, 0.0, 0.023980815347721823, 33.45202313916806, 33.738199650215186, 478, 723.4947744155403, 1814, 2292], [0.0, 0.0, 0.0, 0.0, 35.1806830361257, 32.93904521729755, 395, 560.3491762479517, 1897, 2292], [0.0, 0.0, 0.0, 0.0, 34.60091544983481, 34.724773113905954, 922, 1336.4694009073626, 1776, 2698], [0.0, 0.0, 0.0, 0.0, 29.11399108372803, 33.06615123869235, 810, 1454.4468776214378, 1777, 2587], [0.6797153024911032, 0.5517241379310345, 0.0, 0.53125, 33.392548739972646, 40.67550288978211, 510, 773.6745150509329, 1778, 2288], [0.926605504587156, 1.0, 1.0, 0.9413919413919414, 35.70579313264336, 42.06452522082368, 309, 481.209935018443, 1791, 2100], [0.0, 0.0, 0.0, 0.0, 36.95069070315858, 40.14769746505658, 553, 735.1713190417887, 1772, 2325], [0.0, 0.0, 0.0, 0.0, 36.98869469264466, 35.28539052635395, 555, 736.8123168239733, 1768, 2323], [0.006289308176100629, 0.0, 0.0, 0.0033003300330033004, 28.307767132343262, 45.63269627412631, 535, 993.2802257775292, 1910, 2445], [0.23618090452261306, 0.0, 0.0, 0.08117443868739206, 25.834111427706368, 40.70868026537837, 818, 1689.5465015547509, 1829, 2647], [1.0, 0.2927927927927928, 0.0, 0.4732394366197183, 25.259447556326325, 23.642978217385767, 765, 1621.3391013218134, 1769, 2534], [1.0, 1.0, 0.34328358208955223, 0.7621621621621621, 25.57566660128705, 27.24295109571051, 434, 906.8160092756875, 1770, 2204], [0.0, 0.0, 0.0, 0.0, 23.50681875785254, 39.05326713390067, 1054, 2423.2453571505566, 1952, 3006], [0.0, 0.0, 0.0, 0.0, 28.05189912156238, 35.947657223126456, 774, 1452.506721820185, 2137, 2911], [0.0, 0.0, 0.0, 0.0, 29.035402803011714, 32.66265627379019, 713, 1284.4137371714105, 2155, 2868], [1.0, 1.0, 1.0, 1.0, 33.50993614647691, 36.1518880009087, 246, 385.9949183943715, 1562, 1808], [0.9596412556053812, 0.1910828025477707, 0.0, 0.43884892086330934, 32.660221497596694, 37.31171544470978, 291, 453.972054441335, 1529, 1820], [1.0, 0.1891891891891892, 0.0, 0.4866385372714487, 36.342772105888294, 37.02856668729684, 353, 479.80014853663516, 1550, 1903], [1.0, 1.0, 1.0, 1.0, 36.51862308808159, 32.091149601669414, 703, 949.4044408218069, 1616, 2319], [0.6427457098283932, 0.022277227722772276, 0.6605504587155964, 0.447347585114806, 33.97208406821519, 38.7868855528149, 699, 1037.4000435243536, 1561, 2260], [0.25806451612903225, 0.685640362225097, 0.27897838899803534, 0.4499437570303712, 33.46808597369354, 36.78461372505302, 794, 1201.0561455243342, 1518, 2312], [0.9952830188679245, 0.9552469135802469, 1.0, 0.9824651882413615, 30.597901637708446, 31.730297155410785, 198, 334.82770202976434, 1624, 1822]]

Prd=[16.92,
19.53,
14.715,
20.97,
21.915,
4.41,
8.145,
14.22,
19.935,
18.9,
18,
2.07,
25.965,
10.98,
3.24,
14.67,
3.87,
4.095,
21.42,
17.415,
11.61,
27.9,
15.525,
15.84,
3.24,
26.235,
13.905,
13.41,
16.2,
10.305,
20.52,
11.835,
15.03,
12.51,
22.59,
17.595,
19.665,
12.96,
17.235,
14.085,
1.395,
17.01,
9.495,
3.825,
15.21,
20.07,
20.97,
11.205,
25.83,
5.805,
1.125,
2.925,
18.315,
13.41,
26.325,
16.11,
18.405,
15.975,
16.29,
12.42,
17.01,
9.81,
11.115,
12.465,
7.335,
21.96,
7.02,
20.745,
7.2,
9.36,
14.94,
12.6,
7.2,
19.8,
21.195,
22.995,
9,
19.935,
19.98]

Frd=[0,
0,
1,
1,
0,
0,
0,
1,
0,
1,
1,
0,
0,
0,
0,
0,
1,
1,
0,
0,
0,
0,
1,
1,
0,
0,
1,
0,
0,
1,
1,
1,
1,
1,
0,
0,
0,
0,
0,
1,
0,
0,
1,
1,
1,
0,
1,
1,
1,
0,
1,
0,
1,
1,
0,
0,
1,
1,
0,
0,
1,
0,
0,
0,
1,
0,
1,
0,
1,
1,
1,
1,
1,
0,
0,
0,
0,
0,
0]

print('nb coulées =',len(Data))
Fb=[100*e[0]for e in Data]
Fm=[100*e[1]for e in Data]
Fh=[100*e[2]for e in Data]
F=[100*e[3]for e in Data]
Pente=[e[4]for e in Data]
Penteh=[e[5]for e in Data]
Deniv=[e[6]for e in Data]
Longueur=[e[7]for e in Data]
Altmin=[e[8]for e in Data]
Altmax=[e[9]for e in Data]
Altmoy=[(e[9]+e[8])/2 for e in Data]

def Graph3D(X,Y,Z): 
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    fig.add_axes(ax) 
    ax.scatter(X, Y, Z)
    ax.set_xlabel('X1', fontsize = 11)
    ax.set_ylabel('X2', fontsize = 11)
    ax.set_zlabel('y', fontsize = 11)
    plt.show()


#Graph3D(Pente,Altmoy,F)
#Graph3D(Fh,Altmax,Pente)

def Graph(X,Y): 
    plt.scatter(X,Y)
    plt.xlabel("Altitude de départ de l'avalanche (m)")
    plt.ylabel("Pourcentage de surface de l'avalanche boisée")
    plt.axvline(x=2400,color='red')
    plt.text(2450,70,s='Altitude limite de la forêt \n                2400m', color='red')
    plt.show()

#Graph(Altmax,F)

#Graph(Altmin,F)

Graph(Altmax,Longueur)

#Graph(F,Longueur)
#Graph(Fh,Pente)
#Graph(Altmax,Pente)

#-------------cacractéristiques physiques des coulées--------------------------------------------------------------------------------------------

def pente():
    Pf=[]
    for k in range(len(Data)):
        if Fh[k]==1:
            Pf.append(Pente[k])
    plt.hist((Pente,Prd), bins=[k for k in range(0,50,3)], edgecolor='black')
    plt.xlabel('pente')
    plt.ylabel('nb')
    handles = [plt.Rectangle((0,0),1,1,color=c,ec="k")for c in ['blue','orange']]
    labels= ["coulées","Pentes tirées aux hasard"]
    plt.axvline(np.average(Pente), color='blue')
    plt.axvline(np.average(Prd), color='orange')
    plt.legend(handles,labels)
    plt.show()

#pente()

def alt():
    plt.hist((Altmax,Altmoy,Altmin), bins=[k for k in range(1000,4000,200)], edgecolor='black')
    plt.xlabel('Altitude (m)')
    plt.ylabel("nombre d'avalanches")
    handles = [plt.Rectangle((0,0),1,1,color=c,ec="k")for c in ['blue','orange','green']]
    labels= ["Altitude de départ de l'avalanche","Altitude moyenne de l'avalanche","Altitude d'arrivée de l'avalanche"]
    plt.axvline(x=2400, color='red')
    plt.legend(handles,labels)
    plt.text(x=2450,y=21,s="Altitude limite de la forêt", color='red')
    plt.show()

#alt()

def longueur():
    plt.hist(Longueur, bins=[k for k in range(0,4000,250)], edgecolor='black')
    plt.xlabel('Longueur')
    plt.ylabel('nb de coulées')
    plt.axvline(np.average(Longueur))
    plt.show()

#longueur()

def foret():
    fch=[]
    for k in range (len(Data)):
        if Fh[k]!=100:
            fch.append(0)
        else:
            fch.append(1)
    moyfch=np.average(fch)
    moyfrd=np.average(Frd)
    errfch=1.96*np.std(fch)/np.sqrt(len(fch))
    errfrd=1.96*np.std(Frd)/np.sqrt(len(Frd))
    
    plt.bar(x=[1,3], height=[100*moyfrd,100*moyfch], yerr=[100*errfrd,100*errfch], color=["grey","orange"])
    plt.xticks(color='none')
    handles = [plt.Rectangle((0,0),1,1,color=c,ec="k")for c in ['orange','grey']]
    labels= ["Zones de départ des avalanches","Zones tirées aux hasard"]
    plt.legend(handles,labels)

    plt.ylabel('pourcentage de la surface boisée')
    plt.show()

#foret()


# --------------------------------------------------------------------------------------------------------

def compatroncon():
    f1=[e[2]*100 for e in Data]
    f2=[e[1]*100 for e in Data]
    f3=[e[0]*100 for e in Data]
    plt.hist((f1,f2,f3), bins=[k for k in range(0,120,20)], edgecolor='black',) #density=True)
    handles = [plt.Rectangle((0,0),1,1,color=c,ec="k")for c in ['blue','orange','green']]
    labels= ["troncon haut","troncon moyen","troncon bas"]
    plt.axvline(x=np.average(f1), color='blue', label='moy troncon haut')
    plt.axvline(x=np.average(f2), color='orange', label='moy troncon moy')
    plt.axvline(x=np.average(f3), color='green', label='moy troncon bas')
    plt.xlabel("proportion de forêt", fontsize=16)  
    plt.ylabel("nb de coulées", fontsize=16)
    plt.legend(handles, labels)

    plt.show()

#compatroncon()

def compatronconalt(altmin,altmax): #comparaison a alt fixée entre altmin et altmax
    F1,F2,F3 = [],[],[]
    for k in range (len(Data)):
        if altmin<Altmax[k]<altmax:
            F1.append(Fh[k]*100)
        elif altmin<Altmin[k]<altmax:
            F3.append(Fb[k]*100)
    #print(F1,F3)
    plt.hist((F1,F3), bins=[k for k in range(0,110,10)], edgecolor='black',) #density=True)
    handles = [plt.Rectangle((0,0),1,1,color=c,ec="k")for c in ['blue','orange']]
    labels= ["troncon haut","troncon bas"]
    plt.axvline(x=np.average(F1), color='blue', label='moy troncon haut')
    plt.axvline(x=np.average(F3), color='orange', label='moy troncon moy')
    plt.xlabel("proportion de forêt à altitude fixée à 1700m", fontsize=16)  
    plt.ylabel("nb de coulées", fontsize=16)
    plt.legend(handles, labels)

    plt.show()

#compatronconalt(1800,2000)

def compapente(altmin,altmax): #pente en fonction de prop de foret a alt fixée 
    f,p = [],[]
    for k in range (len(Data)):
        if altmin<Altmoy[k]<altmax:
            f.append(Fh[k]*100)
            p.append(Pente[k])
    Graph(f,p)

#compapente(1500,1750)
#compapente(1750,2000)

#__________________________________________________________________________________________________________








def moypentelongueur(): #compare les moyenne de pente et de longueur entre les coulées sans foret et les coulées 100pourcent foret
    pf,pnf,lf,lnf,prd,prdf = [],[],[],[],[],[]
    for k in range (len(Data)):
        if Fh[k]==0 and 0<Altmax[k]<2400: 
            pnf.append(Pente[k])
            lnf.append(Longueur[k])
        elif Fh[k]==100 and 0<Altmax[k]<2400:
            pf.append(Pente[k])
            lf.append(Longueur[k])
    for i in range (len(Frd)):
        if Frd[i]==1:
            prdf.append(Prd[i])
        else:
            prd.append(Prd[i])

    moypf=np.average(pf)
    moypnf=np.average(pnf)
    moylf=np.average(lf)
    moylnf=np.average(lnf)
    moyprd=np.average(prd)
    moyprdf=np.average(prdf)
    stdpf=np.std(pf)
    stdpnf=np.std(pnf)
    stdlf=np.std(lf)
    stdlnf=np.std(lnf)
    stdprd=np.std(prd)
    stdprdf=np.std(prd)
    
    plt.bar([5,10],[moypnf-25,moypf-25], width=2, bottom=25, yerr=[1.96*stdpnf/np.sqrt(len(pnf)),1.96*stdpf/np.sqrt(len(pf))], color=["orange", (0.8,0.8,0)])
    handles = [plt.Rectangle((0,0),1,1,color=c,ec="k")for c in ["orange", (0.8,0.8,0)]]
    labels= ["Avalanches déclenchées en zone non boisée", "Avalanches déclenchées dans un boisement continu"]
    
    plt.xticks(color="none")
    plt.ylabel("longueur de l'avalanche (m)")
    plt.legend(handles,labels)


    #plt.bar([5,6.5],[moylnf,moylf], width=1, bottom=0, yerr=[1.98*stdlnf/np.sqrt(len(lnf)),1.98*stdlf/np.sqrt(len(lf))], color=["orange", (0.8,0.8,0)])
    
    plt.show()

#moypentelongueur()


c=0
for e in Altmax:
    if e <=2400:
        c+=1
print (c/127)
