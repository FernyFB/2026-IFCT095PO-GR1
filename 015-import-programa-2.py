# Es el mismo programa que 012-listas-playground, pero con el import

from import_libreria_comun import describe

cantidad = 55
cantidad2 = 11
pre_mensaje_para_usuario = "El valor es "
post_mensaje_para_usuario = "jiroclios"

describe(cantidad)
describe(cantidad2)
describe(pre_mensaje_para_usuario)
describe(post_mensaje_para_usuario)

print("=" * 40)
print()

combinamos_la_informacion_numerica = cantidad + cantidad2
print(combinamos_la_informacion_numerica)

combinamos_la_informacion_texual = pre_mensaje_para_usuario + post_mensaje_para_usuario
print(combinamos_la_informacion_texual)

combinamos_distintos_tipos = pre_mensaje_para_usuario + cantidad
print(combinamos_distintos_tipos)
