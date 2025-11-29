# Ouverture du fichier
# a mode:
# le fichier n'existe pas, créera le fichier
# le fichier existe, sera écrits à la fin
f = open('python.txt', 'a')
f.write("hello world2")
f.flush()
f.close()