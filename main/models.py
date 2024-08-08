from django.db import models
from django.utils.html import mark_safe


class Profile(models.Model):

    photo = models.ImageField(upload_to='media/profile_photos')
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField()
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=4, decimal_places=2, null=True)

    def __str__(self) -> str:
        return self.name
    
    def img_preview(self):
        return mark_safe(f'<img src="{self.photo}">')
    
    class Meta:
        db_table = 'UserProfiles'
        ordering = ['surname']
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profilesss'

class Player(models.Model):

    class BestPositionTextChoices(models.TextChoices):
        ST = "ST"
        RB = "RB"
        RW = "RW"
        CDM = "CDM"

    name = models.CharField(max_length=100)
    img_link = models.URLField(null=True)
    mail = models.EmailField(null=True)
    flag_img_link = models.URLField(null=True)
    Best_position = models.CharField(null=True, max_length=50, choices=BestPositionTextChoices.choices)
    # Best_position = models.TextChoices(names=('А','B'), values=('A','B'))


    # photo = models.ImageField(upload_to='media/profile_photos')

    def __str__(self) -> str:
        return self.name

    def img_preview(self):
        return mark_safe(f'<img src="{self.img_link}">')

    img_preview.short_description = 'Player\'s Image'
    # img_preview.allow_tags = True

    def flag_preview(self):
        return mark_safe(f'<img src="{self.flag_img_link}">')

