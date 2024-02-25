from qgis.core import QgsProject, QgsFeatureRequest

name_layer = 'topo_fazendas'
layer = QgsProject.instance().mapLayersByName(name_layer)[0]

if layer and isinstance(layer, QgsVectorLayer):
    geometry_features = [feature.geometry() for feature in layer.getFeatures()]
    extension = geometry_features[0].boundingBox()
    
    for geometry in geometry_features[1:]:
        extension.combineExtentWith(geometry.boundingBox())
    
    iface.mapCanvas().setExtent(extension)
    iface.mapCanvas().refresh()