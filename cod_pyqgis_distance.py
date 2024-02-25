from math import sqrt

faz_tal_lista = [("24886", "1"), ("17543", "1"), ("17543", "2"), ("31145", "1"), ("32961", "1")]
faz_tal_listLayer = []
tal_geomtry_list = []
distance_tal = None

faz_tal_listLayer.clear()
tal_geomtry_list.clear()

layer = QgsProject.instance()
get_camada = layer.mapLayersByName('topo_fazendas')[0]

for item in get_camada.getFeatures():
    faz = str(int(item['fazenda']))
    tal = str(item['talhao'])
    
    faz_tal = (faz, tal)
    
    if faz_tal not in faz_tal_listLayer:
        faz_tal_listLayer.append(faz_tal)

for faz, tal in faz_tal_lista:
    if (faz, tal) in faz_tal_listLayer:
        for feature in get_camada.getFeatures():
            if str(int(feature['fazenda'])) == faz and str(feature['talhao']) == tal:
                geometry_tal = feature.geometry()
                tal_geomtry_list .append(geometry_tal)

def get_coordinates_center(geometry):
    centro_geom = geometry.centroid().asPoint()
    x, y = centro_geom.x(), centro_geom.y()
    return x, y

for geometry1 in tal_geomtry_list:
    x1, y1 = get_coordinates_center(geometry1)
    for geometry2 in tal_geomtry_list:
        if geometry1 == geometry2:
            continue
        
        x2, y2 = get_coordinates_center(geometry2)
        
        distance = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        
        distnce_km = round(distance, 2) / 1000
        
        if distnce_km <= 10:
            distance_tal = True
            continue
        else:
            distance_tal = False
            break
    



