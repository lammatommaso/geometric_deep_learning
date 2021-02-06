from PIL import Image, ImageDraw

simplex = Image.new("L", (128,128), 255)
draw = ImageDraw.Draw(simplex)
draw.line([1,1,3,2,1,3])
simplex.save("simplex.png")


