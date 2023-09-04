'''from qgis.core import *
from qgis.gui import *
from qgis.analysis import *

from qgis.PyQt.QtCore import *
from qgis.PyQt.QtGui import *

path_to_file = '/Volumes/Escritorio_Externo/Users/raulguzman/Documents/info/Tesis_maestria/RAUL TESIS DATOS/DATOS FINALES/calles/calles_cuauhtemoc.shp'
vectorLayer = QgsVectorLayer(path_to_file, 'lines')
builder = QgsGraphBuilder(vectorLayer.sourceCrs())
director = QgsVectorLayerDirector(vectorLayer, -1, '', '', '', QgsVectorLayerDirector.DirectionBoth)

startPoint = QgsPointXY(485456, 2152283)
endPoint = QgsPointXY(482357,2145150)

tiedPoints = director.makeGraph(builder, [startPoint, endPoint])
tStart, tStop = tiedPoints

graph = builder.graph()
idxStart = graph.findVertex(tStart)

tree = QgsGraphAnalyzer.shortestTree(graph, idxStart, 0)

idxStart = tree.findVertex(tStart)
idxEnd = tree.findVertex(tStop)

if idxEnd == -1:
    raise Exception('No route!')

# Add last point
route = [tree.vertex(idxEnd).point()]

# Iterate the graph
while idxEnd != idxStart:
    edgeIds = tree.vertex(idxEnd).incomingEdges()
    if len(edgeIds) == 0:
        break
    edge = tree.edge(edgeIds[0])
    route.insert(0, tree.vertex(edge.fromVertex()).point())
    idxEnd = edge.fromVertex()

# Display
rb = QgsRubberBand(iface.mapCanvas())
rb.setColor(Qt.green)

# This may require coordinate transformation if project's CRS
# is different than layer's CRS
for p in route:
    rb.addPoint(p)
    
 '''   
    
from qgis.core import *
from qgis.gui import *
from qgis.analysis import *
from qgis.utils import iface

from qgis.PyQt.QtCore import *
from qgis.PyQt.QtGui import *

import geopandas as gp


path_to_file = '/Volumes/Escritorio_Externo/Users/raulguzman/Documents/info/Tesis_maestria/RAUL TESIS DATOS/DATOS FINALES/calles/callesCDMXEPSG:4326.shp' 
#path_to_file = '/Volumes/Escritorio_Externo/Users/raulguzman/Documents/info/Tesis_maestria/RAUL TESIS DATOS/DATOS FINALES/calles/calles_cuauhtemoc.shp'
vectorLayer = QgsVectorLayer(path_to_file, 'lines')
builder = QgsGraphBuilder(vectorLayer.sourceCrs())
director = QgsVectorLayerDirector(vectorLayer, 6, '', '', '', QgsVectorLayerDirector.DirectionBoth)



startPoint = QgsPointXY(477280.19007599086, 2148611.622814366)
endPoint = QgsPointXY(479697.41136285156, 2154725.503541218)

tiedPoints = director.makeGraph(builder, [startPoint, endPoint])
tStart, tStop = tiedPoints

graph = builder.graph()
idxStart = graph.findVertex(tStart)

tree = QgsGraphAnalyzer.shortestTree(graph, idxStart, 0)

idxStart = tree.findVertex(tStart)
idxEnd = tree.findVertex(tStop)

if idxEnd == -1:
    raise Exception('No route!')

# Add last point
route = [tree.vertex(idxEnd).point()]

# Iterate the graph
while idxEnd != idxStart:
    edgeIds = tree.vertex(idxEnd).incomingEdges()
    if len(edgeIds) == 0:
        break
    edge = tree.edge(edgeIds[0])
    route.insert(0, tree.vertex(edge.fromVertex()).point())
    idxEnd = edge.fromVertex()

# Display
rb = QgsRubberBand(iface.mapCanvas())
rb.setColor(Qt.green)


# This may require coordinate transformation if project's CRS
# is different than layer's CRS
for p in route:
    rb.addPoint(p)
