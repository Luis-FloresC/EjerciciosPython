x = {1,2,3,4,5}
print(type(x))

x.add(0)
print(x)

y = {"id":1,"nombre":"Luis","apellido":"Flores","carrera":"Ingeniero"}
y["direccion"] = "Danli"
y.update({"direccion":"cuyali"})
print(y.get("nombre"));
print(y.values())
print(y.keys())
print(y)