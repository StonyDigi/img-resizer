from PIL import Image
import os

# Az eredeti és a célmappa útvonala
input_folder = "input_images"
output_folder = "output_images"

# Létrehozzuk a célmappát, ha nem létezik
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Végigmegyünk az összes képen az input mappában
for filename in os.listdir(input_folder):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        # Kép megnyitása
        img = Image.open(os.path.join(input_folder, filename))
        # Átméretezés
        img = img.resize((1920, 1080), Image.LANCZOS)
        # Kép elmentése a célmappába
        img.save(os.path.join(output_folder, filename))

print("Átméretezés kész!")
