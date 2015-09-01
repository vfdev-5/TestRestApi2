
from django.db import models


class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    comment = models.TextField()
    owner = models.ForeignKey('auth.User', related_name='comments')

    def __unicode__(self):
        return '{id=%d, comment: %s, owner: %s}' % (self.id, self.comment, self.owner)
