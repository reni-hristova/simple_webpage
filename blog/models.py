from django.db      import models
from django.conf    import settings
from django.utils   import timezone

ENTRY_TYPES = (
    ('education', 'Education'),
    ('experience', 'Experience'),
    ('achievement', 'Achievement'),
)

class Post(models.Model):
    author          = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title           = models.CharField(max_length = 200)
    text            = models.TextField()
    created_date    = models.DateField(default = timezone.now)
    published_date  = models.DateField(blank = True, null = True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Entry(models.Model):
    type            = models.CharField(max_length = 20, choices=ENTRY_TYPES, default = "experience")
    title           = models.CharField(max_length = 200)
    organisation    = models.CharField(max_length = 200)
    description     = models.TextField()
    start_date      = models.DateTimeField(blank = True, null = True)
    end_date        = models.DateTimeField(blank = True, null = True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title + "at " + self.organisation

class EducationEntry(models.Model):
    degreeTitle     = models.CharField(max_length = 200)
    organisation    = models.CharField(max_length = 200)
    description     = models.TextField()
    start_date      = models.DateTimeField(blank = True, null = True)
    end_date        = models.DateTimeField(blank = True, null = True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.degreeTitle + "at " + self.organisation

class PersonalProfile(models.Model):
    description  = models.TextField()
    last_updated = models.DateField(default = timezone.now)

    def publish(self):
        self.last_updated = timezone.now()
        self.save()

    def __str__(self):
        return self.description
