class Calculator:

    def __init__(self, value):
        self.value = value

    def add(self):
        result = self.value[0]
        for x in self.value[1::]:
            result += x
        return result

    def sub(self):
        result = self.value[0]
        for x in self.value[1::]:
            result -= x
        return result

    def mult(self):
        result = self.value[0]
        for x in self.value[1::]:
            if x > 0:
                result *= x 
        return result   

    def div(self):
        result = self.value[0]
        for x in self.value[1::]:
            if x > 0:
                result /= x 
        return result
