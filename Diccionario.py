diccio={"Alemania":"Berlin","Francia":"Paris", "England":"Londres", "España":"Madrid"}

print(diccio["Francia"])
print("    ")
print(diccio["Alemania"])
print("    ")
print(diccio)
print("    ")
diccio["Italia"]="Lisboa"
print(diccio)
print("    ")
diccio["Italia"]="Roma"
print(diccio)
print("    ")
del diccio["England"]
print(diccio)