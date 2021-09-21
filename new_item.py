import random
size = ['small', 'medium', 'large']
item = ['book', 'journal', 'painting', 'goblet']
color_thing = ['etching', 'paint', 'wrapping', 'stamp']
color = ['black', 'red', 'green', 'blue', 'yellow', 'purple', 'white']
location = ['top', 'side', 'bottom' ]

the_size = random.choice(size)
the_item = random.choice(item)
the_color_thing = random.choice(color_thing)
the_color = random.choice(color)
the_location = random.choice(location)

print(f"You come across a **{the_size} **{the_item}**.") 
print(f"You notice a **{the_size} {the_color}** on **{the_color_thing}** on the **{the_location}** of the **{the_item}**.") 
print(f"You're curious on what that means, and why it's there.")
