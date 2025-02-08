temperatura = []

for n in range(0, 5):
  t = int(input("Registre la temperatura:"))
  temperatura.append(t)
print(temperatura)

promedio = sum(temperatura)/ len(temperatura)
print(f"el promedio de todas las temperaturas es :{promedio:.2f}")

if t < 20:
  print("Se necesita arreglo la temperatura promedio es baja")

elif 20 <= t <= 30:
  print("El aire esta en excelentes condiciones")
else:
  print ("se necesita un arreglo la temperatura promedio es baja")
