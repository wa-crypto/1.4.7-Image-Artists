from PIL import Image, ImageDraw, ImageFilter
"""
im = Image.open('family_1.png')
im.convert('RGBA')
im.putalpha(255)
angle = 20
out = im.rotate(angle, expand=True, fillcolor= None)
out.save('OriginalImages/family_1.png')


im1 = Image.open('OriginalImages/result1.jpg')
im2 = Image.open('OriginalImages/family_1.png')

back_im = im1.copy()
back_im.paste(im2, (500, 10),im2)
back_im.save('OriginalImages/result2.png', quality=95)
"""
"""
im1 = Image.open('OriginalImages/result2.png')
im2 = Image.open('familysil.png')

back_im = im1.copy()
back_im.paste(im2, (0, 390),im2)
back_im.save('OriginalImages/result3.png', quality=95)
"""
