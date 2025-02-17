from django.db import models

from django.db import models
from django.contrib.auth.models import User

class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ('income', 'Income'),
        ('expense', 'Expense'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.title} - {self.amount}"

class Budget(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    monthly_budget = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    savings_goal = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    current_savings = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.user.username}'s Budget"

