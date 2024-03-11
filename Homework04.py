#Tuple
immutable_var = 1, 1.0, 'string', True
print(type (immutable_var))
print(immutable_var)
 #Тuple(Кортеж) является неизменяемым типом данных, чтобы присвоить в нем новые значения,
 #нужно вставить в него List(Список), и тогда можно список изменить внутри кортежа
  #ПРИМЕР:
immutable_var01 = [1, 2.0, 'string', True], 5
immutable_var01 [0][2] = 5.6
print (immutable_var01)
#List
Mutable_var = [1,2,5, True, 'string']
Mutable_var.remove(2)
Mutable_var.append(6.0)
Mutable_var.extend(['apple'])
print(type(Mutable_var))
print(Mutable_var)
