from django.shortcuts import render

# Create your views here.


# from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Expense
from api.serializers import ExpensesSerializer
from django.contrib.auth import authenticate
from rest_framework import permissions
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView



# Create your views here.
@api_view(['GET', 'POST'])
def GetExpenses(request):
    """
    List all tasks, or create a new task.
    """
    if request.method == 'GET':
        expenses = Expense.objects.all()
        serializer = ExpensesSerializer(expenses, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ExpensesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def GetExpense(request, pk):
    """
    Get, udpate, or delete a specific task
    """
    try:
        expense = Expense.objects.get(pk=pk)
    except Expense.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ExpensesSerializer(expense)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ExpensesSerializer(expense, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serilizer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        expense.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



   
class LoginView(APIView):
    permission_classes = [permissions.AllowAny, ]

    def post(self, request, *args, **kwargs):
        print(request)
        data = request.data
        print(data)
        user = authenticate(username=data.get('username'), password=data.get('password'))

        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=200)
        return Response(status=400)