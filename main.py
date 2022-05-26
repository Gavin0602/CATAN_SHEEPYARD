from DrawMap import *
from Map import *


map_size = 5
map_type = 0
length = 30

m = Map(map_size, map_type)

print(len(m.edges))
print(m.get_total_edges())
print(m.edges)
# draw_map(map_size, length)
