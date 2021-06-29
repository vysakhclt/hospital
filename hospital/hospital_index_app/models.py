from django.db import models


# Create your models here.

class Doctors(models.Model):
    name = models.CharField(max_length=150, unique=True)
    qualification = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='doctor')
    detail = models.TextField()

    # def get_url(self):
    #     return reverse(':ProdCatdetails', args=[self.category.slug, self.slug])

    class Meta:
        ordering = ('name',)
        verbose_name = 'doctor'
        verbose_name_plural = 'doctors'

    def __str__(self):
        return '{}'.format(self.name)


class Blog(models.Model):
    name = models.CharField(max_length=250)
    text = models.TextField()
    image = models.ImageField(upload_to='blog')



    class Meta:
        ordering = ('name',)
        verbose_name = 'blog'
        verbose_name_plural = 'blogs'

    def __str__(self):
        return '{}'.format(self.name)


class Booking(models.Model):
    patient_name = models.CharField(max_length=30)
    age = models.IntegerField()
    phone = models.TextField()
    time_slot = models.DateTimeField()
    department = models.TextField()
    doctor = models.TextField()

    class Meta:
        ordering = ('patient_name',)
        verbose_name = 'Booking'
        verbose_name_plural = 'Bookings'

    def __str__(self):
        return '{}'.format(self.patient_name)