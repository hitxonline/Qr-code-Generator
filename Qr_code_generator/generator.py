from PIL import Image,ImageFont,ImageDraw
from api.models import Codes
import qrcode
import urllib.request
from api.models import Codes, Code


def merging(id):

    # Open the two images

    urllib.request.urlretrieve(
        'https://eweb.pythonanywhere.com/media/wallpapers/background.jpg',
        "background.jpg"
    )
    image1 = Image.open('background.jpg')
    image2 = Image.open(r"qr_codes/qr_code"+str(id)+".jpg")


    # Resize image2 to match the size of image1
    newsize = (300, 300)
    image2 = image2.resize(newsize)


    # Create a new image with the same size as image1
    result = Image.new("RGB",image1.size)

    # Paste image1 onto the new image,

    result.paste(image1, (0, 0))
    # Paste image2 onto the new image, on top of image1
    result.paste(image2, (145,440), image2)

    # Save the resulting Image
    result.save('media/image'+str(id)+'.jpg')


def Code_generating(link,id):

    # qr code generating with using a link
    
    img = qrcode.make(link)
    qr = Code.objects.update(id=id, qrcode=img)


def Texting(id, holder_status, link_from):
    
    img = Image.open(r"media/image"+str(id)+".jpg")

    # Set font size and type

    font_type = ImageFont.truetype('arial.ttf',70)
    draw = ImageDraw.Draw(img)

    # Create a white color text to the Image

    draw.text(xy=(270,190),text=holder_status, stroke_width=3, fill=('#ffffff'),font=font_type)


    # Create another white color text to the Image

    draw.text(xy=(132,300),text=link_from, stroke_width=3, fill=('#ffffff'),font=font_type)

    # Save the final result image

    img.save('media/image'+str(id)+'.jpg')

    