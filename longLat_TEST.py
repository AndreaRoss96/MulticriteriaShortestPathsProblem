from pyproj import Proj, transform
import time
import pyproj


# Test 1 - 0.05498711 s
start=time.time()
inProj = Proj(init='epsg:3857')
outProj = Proj(init='epsg:4326')
x1,y1 = -11705274.6374,4826473.6922
x2,y2 = transform(inProj,outProj,x1,y1)
end=time.time()
print(y2,x2)
print('%.7f' % (end-start))
print("*" * 80)

# Test 2 - 0.0022807 s --- factor 11,9
start=time.time()
x,y = -11705274.6374,4826473.6922
#performs a cartographic transformations between geographic (lan/log) and projection (x/y)
p = pyproj.Proj("+proj=merc +lon_0=0 +k=1 +x_0=0 +y_0=0 +a=6378137 +b=6378137 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs")
lon, lat = p(x, y, inverse=True)
end=time.time()
print(lat, lon)
print('%.7f' % (end-start)) 
print("*" * 80)

"""
After several tests, is possible to see that in everey one
the second method results tiny faster.
"""