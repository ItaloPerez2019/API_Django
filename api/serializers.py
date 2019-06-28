from rest_framework import serializers
from api.models import Expense

class ExpensesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ('description', 'amount', 'types', 'date')
