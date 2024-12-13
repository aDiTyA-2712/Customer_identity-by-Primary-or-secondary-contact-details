from django.db import models
from django.utils import timezone

# Create your models here.
class PrimCont(models.Model):
    PRIMARY='primary'
    SECONDARY='secondary'
    link_precedence_choice=[
        (PRIMARY,'Primary'),
        (SECONDARY,'Secondary'),
    ]
    id=models.AutoField(primary_key=True)
    emails=models.CharField(null=True,blank=True)
    phones=models.CharField(null=True,blank=True)
    linked_id=models.IntegerField(null=True,blank=True)
    link_precedence=models.CharField(choices=link_precedence_choice,default=PRIMARY)
    createdAt = models.DateTimeField(auto_now_add=True,blank=True)
    updatedAt = models.DateTimeField(auto_now=True,blank=True)
    deletedAt= models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return f'{self.emails or self.phones} ({self.link_precedence})'

 

