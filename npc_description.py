import random
from faker import Faker
fake = Faker()
Faker.seed(random.randint(1,10))
gender = ['male', 'female', 'non-binary']
general_age = ['young', 'old', 'middle-aged' ]
face_age = ['weathered', 'baby-faced', 'young', 'clean', 'scared']
mouth_status = ['smiling', 'frowning', 'scowling', 'laughing', 'furrowing']
stature = ['slender', 'muscled', 'chubby', 'healthy', 'fat']
skin_color = ['white', 'dark', 'black', 'tan']
hair_color = ['yellow, white, black', 'dark brown', 'brown']
hair_style = ['wavy', 'dreadlocks', 'straight', 'puffy']
clothes_style = ['expensive', 'wooded', 'modest', 'extravagant', 'lazy']
attitude = ['positive', 'off putting', 'angry', 'giddy', 'obnoxious']
class_status = ['low born', 'high born']

their_gender = random.choice(gender)
if their_gender == 'male':
    name = fake.name_male()
elif their_gender == 'female':
    name = fake.name_female()
else:
    name = fake.name_nonbinary()

print(f"This character is **{their_gender}** and looks generally **{random.choice(general_age)}**.")
print(f"Their face looks **{random.choice(face_age)}** and are **{random.choice(mouth_status)}**, in your general direction.")
print(f"They have a **{random.choice(stature)} build**, with **{random.choice(skin_color)} skin** and **{random.choice(hair_color)} {random.choice(hair_style)} hair**.")
print(f"They are dressed in a **{random.choice(clothes_style)} style** which compliments their general **{random.choice(attitude)}** attitude.")
print(f"They seem to be **{random.choice(class_status)}**, but looks can be deceiving.")
print(f'They walk up to you and introduce themselves as **{name}**. ')