import uuid
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
# Create your models here.

class Books(models.Model):

    id = models.UUIDField(
        primary_key=True,
        # db_index=True,
        default=uuid.uuid4,
        editable=False,
    )
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    cover = models.ImageField(upload_to='covers/',blank=True)

    class Meta:
        # class-based model indexes were added so can include in the Meta section instead.
        indexes = [
            models.Index(fields=["id"],name="id_idnex"),
        ]
        permissions = [
        ("special_status", "Can read all books"),
        ]


    def __str__(self) -> str:
        return self.title
    
    # def get_absolute_url(self):
    #     return reverse("books_detail",kwargs={"pk":self.pk})
    def get_absolute_url(self): # new
        return reverse("book_detail", kwargs={"pk":self.pk})
        # return reverse("book_detail", args=[str(self.id)])

class Reviews(models.Model):

    book = models.ForeignKey(
        Books,
        on_delete=models.CASCADE, 
        related_name='reviews',
    )

    review = models.CharField(max_length=255)
    
    auther = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    
    def __str__(self) -> str:
        return self.review