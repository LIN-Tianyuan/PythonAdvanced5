# Importer le module json
import json

# Préparer les données python au format json
data = [{"name": "Kevin", "age": 16}, {"name": "Laurent", "age": 20}]
print(len(data))
print(type(data))

# Convertir les données python en données json
data = json.dumps(data)
print(data)
print(type(data))

# Convertir les données json en données python
data = json.loads(data)
print(data)
print(type(data))





