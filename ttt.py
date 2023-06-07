import random
from PIL import Image
import turtle_shell
img = Image.new("L", (25, 25))

for i in range(25):
    for j in range(25):
        img.putpixel((i, j), random.randint(0, 10))

t=turtle_shell.Make_turtmat(25,25)
print(t[2,5],t[5,5],t[2,6])
# img.show()
# img.save("little_pic.png")
print(0%4,11%4,7%4)