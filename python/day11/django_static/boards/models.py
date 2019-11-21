from django.db import models
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import ResizeToFill, Thumbnail

# Create your models here.
# Board를 새로 생성할때 save() 가 호출되고 나서 pk가 생성
def board_img_path(instance, filename):
    return f'boards/user_{instance.user.pk}번글/{filename}'


class Board(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    
    # #ResizeToFill Ver.1
    # image = ProcessedImageField(
    #     upload_to = "boards/images_rtf" ,
    #     processors= [ResizeToFill(600, 500)],
    #     format = "JPEG",
    #     options = {
    #         'quality':85

    #     }
    # )
    
    # #Thumbnail Ver.1 (원본 x, 썸네일 o)
    # image = ProcessedImageField(
    #     upload_to = "boards/thumbnail" ,
    #     processors= [ResizeToFill(100, 100)],
    #     format = "JPEG",
    #     options = {
    #         'quality':90

    #     }
    # )


    #Thumbnail 원본은 저장하고 썸네일은 캐쉬형태로 Ver.2
    #원본 저장 o  thumbnail은 캐시형태로 ~
    image = models.ImageField(blank=True, upload_to=board_img_path)
    image_thumbnail = ImageSpecField(
        source = 'image',
        processors = [Thumbnail(250,250)],
        format= "JPEG",
        options = {
             'quality':90

        }

    )

    
    
    # image = models.ImageField(blank=True)
    # image_thumb = ImageSpecField(
    #     source = 'image',
    #     processors = [Thumbnail(200, 300)],
    #     format = "JPEG",
    #     options = {
    #         'quality':90
    #     }
    # )
