from django.db import models

# Create your models here.

# we want to have a Book table inside our DB


class Book(models.Model):

    # fields aka attributes of the table:
    # eqv. title VARCHAR(255) NOT NULL
    title = models.CharField(blank=False, max_length=255)

    # eqv. ISBN VARCHAR(255) NOT NULL
    ISBN = models.CharField(blank=False, max_length=255)

    # eqv. desc TEXT NOT NULL
    desc = models.TextField(blank=False)

    # toString function - allows us to state the string representation of a class in the django DB (presentation)
    def __str__(self):
        return self.title


class Publisher(models.Model):

    name = models.CharField(blank=False, max_length=100)
    email = models.CharField(blank=False, max_length=100)
    website = models.CharField(blank=False, max_length=100)

    def __str__(self):
        return self.name


class Author(models.Model):

    first_name = models.CharField(blank=False, max_length=100)
    last_name = models.CharField(blank=False, max_length=100)
    birthdate = models.DateField(blank=False)

    def __str__(self):
        return self.first_name + " " + self.last_name
