from PIL import Image

img = Image.open("UIC_spr22.bmp")


w, h = img.size

msg = ""

for y in range(0,h,80):
  for x in range(0, w, 80):
    r,g,b = img.getpixel( (x,y) )

    msg += chr(b-100)

print (msg)

exit()


msg = "Congratulations on making it through CS111 during a challenging semester!\nI respect your hard work and perseverance. -- Prof. Hayes"

counter = 0



for y in range(0,h,80):
  for x in range(0, w, 80):
    r,g,b = img.getpixel( (x,y) )


    if (counter < len(msg)):
    
      ltr = msg[counter]
  
      img.putpixel ( (x,y), (r, g, 100 + ord(ltr)))
  
      counter += 1

img.save("UIC_spr22.bmp")



# Part 1


# the puzzle-gold file is a PNG file, which is RGBA mode, meaning the color values are 4-tuples, not 3. So you'll unpack the pixel color to FOUR variables, not three
# r,g,b,a = 
# and you'll put colors as 4-tuples
# But the red, green and blue values are the only ones you need to change to unscramble the image.  