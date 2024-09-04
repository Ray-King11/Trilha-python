curso = "Curso de Python"
nome_curso = curso
saldo = 1000
limite = 1000

print(curso is nome_curso)
print(curso is not nome_curso)
print(saldo is limite)
print(saldo is not limite)


a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)  # True, pois b é o mesmo objeto que a
print(a is c)  # False, pois c é um objeto diferente, apesar de ter o mesmo conteúdo
print(a is not c)  # True, pois c não é o mesmo objeto que a

