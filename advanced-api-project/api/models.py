from django.db import models

# Create your models here.
class Author(models.Model):
    """
    Represents a book author.

    This model stores basic author information.
    An Author can be associated with multiple Book instances
    through a one-to-many relationship.
    """
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Book(models.Model):
    """
    Represents a book written by an author.

    Each Book is linked to exactly one Author via a ForeignKey,
    creating a one-to-many relationship (Author → Books).
    """

    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    publication_year = models.DateField()
    def __str__(self):
       return f"{self.title} ({self.publication_year})"