from django.db import models

# Create your models here.
class UserCreditCard(models.Model):
    username = models.CharField(max_length=225)
    email = models.EmailField(unique=True)
    encrypted_credit_card = models.TextField()  # Updated field

    def __str__(self):
        return f"UserCreditCard(username={self.username}, email={self.email}, encrypted_credit_card= {self.encrypted_credit_card})"



    

# models.py
