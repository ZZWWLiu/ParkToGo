# recommend 3 parks to user

introduction = 'Arches National Park\n\
This site features more than 2,000 natural sandstone arches, including the Delicate Arch. In a desert climate millions of years of erosion have led to these structures, and the arid ground has life-sustaining soil crust and potholes, natural water-collecting basins. Other geologic formations are stone columns, spires, fins, and towers.\
\n \
Glacier National Park\n\
Part of Waterton Glacier International Peace Park, this park has 26 remaining glaciers and 130 named lakes under the tall Rocky Mountain peaks. There are historic hotels and a landmark road in this region of rapidly receding glaciers. These mountains, formed by anoverthrust, have the world\'s best sedimentary fossils from the Proterozoic era.\\n \
Hawaii Volcanoes National Park\n\
This park on the Big Island protects the Kilauea and Mauna Loa volcanoes, two of the world\'s most active. Diverse ecosystems of the park range from those at sea level to 13,000 feet (4,000 m).\
\n\
Great Smoky Mountains National Park\n\
The Great Smoky Mountains, part of the Appalachian Mountains, have a wide range of elevations, making them home to over 400 vertebrate species, 100 tree species, and 5000 plant species. Hiking is the park\'s main attraction, with over 800 miles (1,300 km) of trails, including 70 miles (110 km) of the Appalachian Trail. Other activities are fishing, horseback riding, and visiting some of nearly 80 historic structures.\
\n\
Yellowstone National Park\n\
Situated on the Yellowstone Caldera, the first national park in the world has vast geothermal areas such as hot springs and geysers, the best-known being Old Faithful and Grand Prismatic Spring. The yellow-hued Grand Canyon of the Yellowstone River has numerouswaterfalls, and four mountain ranges run through the park. There are almost 60 mammal species, including the gray wolf, grizzly bear,lynx, bison, and elk.'

print introduction

print 'please rate those five Parks : (enter 1~5)'
rate1 = raw_input('Arches National Park : ')
rate2 = raw_input('Glacier National Park : ')
rate3 = raw_input('Great Smoky Mountains National Park : ')
rate4 = raw_input('Great Smoky Mountains National Park : ')
rate5 = raw_input('Yellowstone National Park : ')

rateList = [rate1, rate2, rate3, rate4, rate5]

num = rateList.index(max(rateList))

print num