import random
building = ['village', 'city', 'township', 'shire', 'suburb', 'roadhouse']
size = ['small', 'medium', 'large']
style = ['gothic', 'europian', 'romanesque', 'baroque', 'colonial']
roads = ['dirt', 'paved', 'cobbled']
roads_status = ['good', 'shoddy', 'crumbling']

the_size = random.choice(size)
the_style = random.choice(style)
the_building = random.choice(building)
the_roads = random.choice(roads)
the_roads_status = random.choice(roads_status)
if the_building == 'roadhouse' or the_building == 'township' or the_building == 'village':
    the_size = 'small'
    the_roads = 'dirt'

print(f"As you walk up to a **{the_building}**, you notice a **{the_size}** number of **{the_style}** buildings.")
print(f"There are **{the_roads_status} {the_roads}** roads connecting the different buildings.")