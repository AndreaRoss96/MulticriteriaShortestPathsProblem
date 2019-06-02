import math

alt = 0 # For semplicity the geodetic height is approximated to 0.

def wgsToEcef(lat, lon):
    """
    Convert latitude an longitude (WorldGeodeticSystem) 
    to EarthCenteredEarthFixed coordinates.
    For semplicity the geodetic height is approximated to 0

    this version is little more performaning than using pyProj.trasform
    --> to prove it check https://gis.stackexchange.com/questions/230160/converting-wgs84-to-ecef-in-python
    """
    rad_lat = lat * (math.pi / 180.0)
    rad_lon = lon * (math.pi / 180.0)

    a = 6378137.0           # Equatorial radius (WGS-84)
    finv = 298.257223563    # Inversa flattening (WGS-84)
    f = 1 / finv
    e2 = 1 - (1 - f) * (1 - f)
    v = a / math.sqrt(1 - e2 * math.sin(rad_lat) * math.sin(rad_lat))

    x = (v + alt) * math.cos(rad_lat) * math.cos(rad_lon)
    y = (v + alt) * math.cos(rad_lat) * math.sin(rad_lon)
    # the z value is not interest to us
    # z = (v * (1 - e2) + alt) * math.sin(rad_lat)

    return x, y

def initSingleNode(graph, source):
    """
    Initialising all the the nodes for the dijkstra algorithm

    graph : the set of all nodes that must be reset

    source : the starting node

    @return
        graph initilized
    """
    for v in graph:
        v.resetValue(False)  # reset the value of predecessor, visited and minWeight of all nodes
    source.minWeight = 0
    source.visited = True
    return graph