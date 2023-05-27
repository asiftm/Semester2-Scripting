from PIL import ImageColor, ImageDraw, Image

img = Image.new('RGBA', (200, 200), 'white')

img.save('pdf.pdf')