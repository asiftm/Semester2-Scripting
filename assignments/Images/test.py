from PIL import ImageColor, Image, ImageChops, ImageDraw,ImageFont
import os
# import images
# print(ImageColor.getcolor('red','RGBA'))

# one = Image.open('1.jpg')
# print(one)
# one.show()

# size = one.size
# print(size)
# height,width = one.size
# print(height)
# print(width)
# print(one.filename)
# print(one.format)
# print(one.format_description)
# one.save('2.png')
# two = Image.open('2.png')
# print(two.filename)
# print(two.format)
# print(two.format_description)

# one = one.crop((2100,200,2800,1000))
# one.show()


# img = Image.new('RGBA', (100, 200), 'purple')
# img.save('purple.png')
# img = Image.new('RGBA', (20, 20))
# img.save('transparent.png')
# img = Image.new('RGBA', (200, 200), (0,255,0,100))
# img.save('green.png')
# img = Image.new('RGBA', (200, 200), (255,0,0,100))
# img.save('red.png')


# crop = one.crop((2100, 200, 2800, 1000))
# copyimg = one.copy()
# copyimg.paste(crop, (0,0))
# copyimg.paste(crop, (2000,1500))
# copyimg.paste(crop, (1000,1000))
# copyimg.show()


# width, height = one.size
#
# halfsize = one.resize((int(width / 2), int(height / 2)))
# halfsize.save('halfsize.jpg')
#
# halfsize.rotate(90).save('rotated90.png')
# halfsize.rotate(180).save('rotated180.png')
# halfsize.rotate(270).save('rotated270.png')
#
# halfsize.transpose(Image.FLIP_LEFT_RIGHT).save('horizontal.png')
# halfsize.transpose(Image.FLIP_TOP_BOTTOM).save('vertical.png')


# for x in range(0, one.width):
#     for y in range(0, one.height):
#         r, g, b = one.getpixel((x, y))
#         print(r,g,b)
        # inverted = (255 - r, 255 - g, 255 - b)
        # one.putpixel((x, y), inverted)
#
# one.save('inverted.png')



# img = ImageChops.invert(one)
# img.show()


# img = Image.new('RGBA', (200, 200), 'white') # new image 200 by 200 pixels
# draw = ImageDraw.Draw(img)
# draw.line([(2, 2), (198, 2), (198, 198), (2,198) , (2,2)], fill='blue')
# draw.rectangle((10, 10, 20, 20), fill='blue')
# draw.ellipse((120, 30, 160, 60), fill='red')
# draw.polygon(((57, 87), (79, 62), (94, 85), (120, 90), (103, 113)), fill='brown')
# for i in range(100, 200, 20):
#     draw.line([(i, 0), (200, i-20)], fill='green')
# img.save('drawing.png')


# im = Image.new('RGBA', (200, 200), 'white')
# draw = ImageDraw.Draw(im)
#
# draw.text((85, 95), 'Hello', fill='purple')
# # fontsFolder = 'FONT_FOLDER'  # e.g. ‘/Library/Fonts'
# # arialFont = ImageFont.truetype(os.path.join(fontsFolder, 'arial.ttf'), 32)
# draw.text((100, 150), 'Hello', fill='gray')
# im.save('text.png')




