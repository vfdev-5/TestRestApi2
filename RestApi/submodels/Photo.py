from django.db import models


class Photo(models.Model):
    owner = models.ForeignKey('auth.User', related_name='images')
    image = models.ImageField(max_length=254)

    def __unicode__(self):
        return '{id=%d, image: %s, owner: %s}' % (self.id, self.image, self.owner)

