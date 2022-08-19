from PIL import Image



# Part 1


# the puzzle-gold file is a PNG file, which is RGBA mode, meaning the color values are 4-tuples, not 3. So you'll unpack the pixel color to FOUR variables, not three
# r,g,b,a = 
# and you'll put colors as 4-tuples
# But the red, green and blue values are the only ones you need to change to unscramble the image.  

img = Image.open("puzzle-gold.png")

w, h = img.size


for x in range(w):
  for y in range(h):
    r,g,b,a = img.getpixel( (x,y) )

    # recover the red values
    recovered_red = r*10

    # set blue and green to 0 to eliminate noise
    img.putpixel ( (x,y), (recovered_red, 0, 0, a))


img.save("lab14.png")







img = Image.open("UIC.bmp")


w, h = img.size

msg = ""

for y in range(0,h,80):
  for x in range(0, w, 80):
    r,g,b = img.getpixel( (x,y) )

    msg += chr(b-100)

print (msg)

