from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    description = models.CharField(max_length=512, blank=True)
    profile_img = models.ImageField(upload_to='profile_images/', blank=True)
    group = models.ManyToManyField('Group')

    def __repr__(self):
        return f'Person({self.first_name})'

    def __str__(self):
        return f'Person({self.first_name})'


class Address(models.Model):
    city = models.CharField(max_length=32)
    street = models.CharField(max_length=32)
    building_no = models.IntegerField()
    apt_no = models.IntegerField()
    label = models.CharField(max_length=32, blank=False)

    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='person_id_address')

    def __repr__(self):
        return f'Address({self.city} {self.street})'

    def __str__(self):
        return f'Address({self.city} {self.street})'


class Telephone(models.Model):
    tel_no = models.IntegerField()
    label = models.CharField(max_length=32, blank=False)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='person_id_tel')

    def __repr__(self):
        return f'Telephone({self.tel_no})'

    def __str__(self):
        return f'Telephone({self.tel_no})'


class Email(models.Model):
    email = models.CharField(max_length=32)
    label = models.CharField(max_length=32, blank=False)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='person_id_email')

    def __repr__(self):
        return f'Email({self.email})'

    def __str__(self):
        return f'Email({self.email})'


class Group(models.Model):
    name = models.CharField(max_length=32)

    def __repr__(self):
        return f'{self.name}'

    def __str__(self):
        return f'{self.name}'

