from django.db      import models
from django.conf    import settings
from django.utils   import timezone

class Etry(models.Model):
    positionTitle   = models.CharField(max_length = 200)
    text            = models.TextField()
    start_date      = models.DateTimeField(default = timezone.now)
    end_date        = models.DateTimeField(blank = True, null = True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.positionTitle

class Section(models.Model):
    title   = models.CharField(max_length = 200)
    content = models.TextField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.title
