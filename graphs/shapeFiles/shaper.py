from shapely.geometry import shape
import fiona
geoms =[shape(feature['geometry']) for feature in fiona.open("bologna.shp")]
import itertools
# create a Graph
import networkx as nx
G = nx.Graph()
for line in geoms[0]:
   for seg_start, seg_end in itertools.izip(list(line.coords),list(line.coords)[1:]):
    G.add_edge(seg_start, seg_end) 