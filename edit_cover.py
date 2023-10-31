from PIL import Image, ImageFont, ImageDraw

def edit_cover_video(title_text, sub_text, third_text):

    my_image =  Image.open("banco_imagens/baseCapa.png")
    image_editable = ImageDraw.Draw(my_image)

    font_size_title = 100
    font_title = ImageFont.truetype("/usr/share/fonts/truetype/ubuntu/Ubuntu-M.ttf", font_size_title)
    image_editable.text((600,160), title_text, (255, 255, 255), font=font_title)

    font_size_sub = 120
    font_sub = ImageFont.truetype("/usr/share/fonts/truetype/ubuntu/Ubuntu-M.ttf", font_size_sub)
    image_editable.text((600,250), sub_text, (255, 255, 255), font=font_sub)

    font_size_sub = 120
    font_sub = ImageFont.truetype("/usr/share/fonts/truetype/ubuntu/Ubuntu-M.ttf", font_size_sub)
    image_editable.text((600,300), third_text, (255, 255, 255), font=font_sub)

    my_image.save("banco_imagens/capaEditada.png")
