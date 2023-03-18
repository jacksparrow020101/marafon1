from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class Users(AbstractUser):
    user_types = (
        ('1', 'Administrator'),
        ('2', 'Habar Menejer'),
        ('3', 'Media Menejer'),
        ('4', 'Howa Maglumaty Menejer'),
        ('5', 'Metbugat Menejer'),
    )
    user_type = models.CharField(max_length=10, default=1, null=True)


class Esasy_Surat(models.Model):
    image = models.ImageField("Surat", upload_to='Esasy_Surat', null=True)
    name = models.CharField("Ady", max_length=500, null=True, blank=True)
    title = models.CharField("Mazmyny", max_length=500, null=True)

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        try:
            self.image.delete()
        except:
            pass
        super().delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        if self.id != None:
            file = str(self.image)
            name = file.split('/', 1)
            if name[0] != 'Esasy_Surat':
                model = Esasy_Surat.objects.get(id=self.id)
                model.image.delete(save=False)
            else:
                pass
        else:
            pass
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('Administrator_Esasy_Surat')


class Habar(models.Model):
    Habarlar = (
        ('1', 'Syýasy habarlar'),
        ('2', 'Tehnologiýa habarlar'),
        ('3', 'Sport habarlar'),
        ('4', 'Harby habarlar'),
    )
    name = models.CharField("Ady", max_length=500, null=True)
    image = models.ImageField("Surat", upload_to='Habar', null=True)
    descriptions = models.TextField("Tekst", null=True)
    read = models.BigIntegerField(default=0)
    habar_types = models.CharField(max_length=10, null=True, choices=Habarlar)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)

    def delete(self, *args, **kwargs):
        try:
            self.image.delete()
        except:
            pass
        super().delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        if self.id != None:
            file = str(self.image)
            name = file.split('/', 1)
            if name[0] != 'Habar':
                model = Habar.objects.get(id=self.id)
                model.image.delete(save=False)
            else:
                pass
        else:
            pass
        super().save(*args, **kwargs)


class Surat(models.Model):
    image = models.ImageField("Surat", upload_to='Surat')
    show = models.BigIntegerField(default=0)
    name = models.CharField("Ady", max_length=100, null=True)

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        if self.id != None:
            file = str(self.image)
            name = file.split('/', 1)
            if name[0] != 'Surat':
                model = Surat.objects.get(id=self.id)
                model.image.delete(save=False)
            else:
                pass
        else:
            pass
        super().save(*args, **kwargs)


class Wideo(models.Model):
    video = models.FileField("Wideo",upload_to='Wideo')
    show = models.BigIntegerField(default=0)
    name = models.CharField("Ady",max_length=100, null=True)

    def __str__(self):
        return self.name + ": " + str(self.video)

    def delete(self, *args, **kwargs):
        self.video.delete()
        super().delete(*args, **kwargs)


class Metbugat_at(models.Model):
    name = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.name


class Metbugat(models.Model):
    metbugat = (
        ('1', 'Gazetler'),
        ('2', 'Žurnallar')
    )
    image = models.ImageField("Surat", upload_to='Metbugat_Surat', null=True)
    pdf = models.FileField("PDF", upload_to='Metbugat_PDF', null=True)
    read = models.BigIntegerField(default=0)
    download = models.BigIntegerField(default=0)
    metbugat_type = models.CharField(max_length=10, choices=metbugat, null=True)
    ady = models.ForeignKey(Metbugat_at, on_delete=models.CASCADE)
    date = models.DateField("Sene", null=True)

    def __str__(self):
        return str(self.date)

    def delete(self, *args, **kwargs):
        try:
            self.image.delete()
        except:
            pass
        try:
            self.pdf.delete()
        except:
            pass
        super().delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        if self.id != None:
            file = str(self.image)
            name = file.split('/', 1)
            file2 = str(self.pdf)
            name2 = file2.split('/', 1)
            if name[0] != 'Metbugat_Surat':
                model = Metbugat.objects.get(id=self.id)
                model.image.delete(save=False)
            else:
                pass
            if name2[0] != 'Metbugat_PDF':
                model = Metbugat.objects.get(id=self.id)
                model.pdf.delete(save=False)
            else:
                pass
        else:
            pass
        super().save(*args, **kwargs)


class Weather(models.Model):
    week = (
        ('1', 'Du'),
        ('2', 'Si'),
        ('3', 'Ça'),
        ('4', 'Pn'),
        ('5', 'An'),
        ('6', 'Şn'),
        ('7', 'Ýk'),
    )
    weather_week = models.CharField(max_length=10, choices=week, null=True)
    weather_type = models.CharField(max_length=10, null=True)
    weather_tempratura = models.IntegerField(null=True)
