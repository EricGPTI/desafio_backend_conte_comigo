from api.serializer import CalculationSerializer
from api.models import Calculation
from rest_framework import viewsets, status
from rest_framework.response import Response
from api.libs.calculator import Calculator


class CalculationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows calculations to be viewed or edited.
    """
    queryset = Calculation.objects.all()
    serializer_class = CalculationSerializer

    def create(self, request):
        value = request.data.get('value')
        operation = request.data.get('operation')

        calculator = Calculator(value)
        
        if operation == '+':
            total = calculator.add()
        elif operation == '-':
            total = calculator.sub()
        elif operation == '*':
            total = calculator.mult()
        elif operation == '/':
            total = calculator.div()
        else:
            raise "OperatorError: Operator value must be one of '+', '-', '*', '/'"
        request.data['total'] = total

        serializer = CalculationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def list(self, request):
    #     calculations = Calculation.objects.all()
    #     serializer = CalculationSerializer(calculations, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)
