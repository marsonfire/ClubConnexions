from django.db import models

# Class for holding the description on the home page
class Description(models.Model):
    descriptionText = models.CharField(max_length = 400)

    def str(self):
        return self.descriptionText


