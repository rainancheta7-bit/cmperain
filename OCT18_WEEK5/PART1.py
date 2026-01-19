#6th demo

#STRING
import math
#NUMERIC TYPE
#INTEGER -10, 0, 2324
#FLOAT 25, 2323
#COMPLEX 25 + 47j #i ampere, j impendance,
intA = 25
intB = 15
intC = 5
#ARITHMETIC OPERATION
intSum = intB + intC
print(intSum)
intDiff = intA- intB
print(intDiff)
intProd = intA * intB
print(intProd)
intQu = intA/intB
print(intQu)
intResult = intA + intB
print(intResult)
#PEMDAS

result = intResult / intQu
print(result)

intAngle = 90
result = round(math.cos(math.radians(intAngle)), 1)
print(result)
result = round(math.sin(math.radians(intAngle)), 1)
print(result)
intAngle = 45
result = round(math.tan(math.radians(intAngle)), 1)
print(result)

intX = 5
faceResult = math.factorial(intX)
print(faceResult)

myComA = 25+5j
myComB = 10-10j
comProd = myComA*myComB
print(comProd)



intA = 5
intB = 6
isResult = intA == intB
print(isResult)
isResult =intA <= intB
print(isResult)
isResult = intA >= intB
print(isResult)
isResult = intA !=intB
print(isResult)
isResult  = intA > intB
print(isResult)
isResult = intA < intB
print(isResult)