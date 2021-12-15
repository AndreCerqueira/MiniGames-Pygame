from PIL import Image
  
# Import an image from directory:
player_image = Image.open("player.png")
hat_image = Image.open("hat2.png")

# Extracting pixel maps:
pixel_map_player = player_image.load()
pixel_map_hat = hat_image.load()
  
# Extracting the width and height 
# of the image:
width, height = player_image.size
  
# taking half of the width:
for i in range(width):
    for j in range(height):
        
        # getting the RGB player pixel value.
        r1, g1, b1, p1 = player_image.getpixel((i, j))
          
        # getting the RGB hat pixel value.
        try:
            if hat_image.getpixel((i, j)) != (0, 0, 0, 0):
                r2, g2, b2, p2 = hat_image.getpixel((i, j))
                pixel_map_player[i, j] = r2, g2, b2, p2
        except:
            pass

        # setting the pixel value.
        
  
# Saving the final output
# as "grayscale.png":
player_image.save("player2.png", format="png")
  
# use input_image.show() to see the image on the
# output screen.