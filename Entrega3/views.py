from django.http import HttpResponse
# from django.template import Template, Context, loader


# from datetime import datetime

# def saludo(request):
#     return HttpResponse('Hola Django - Coder')

# def segunda(request):
#     return HttpResponse('Esto<br><br> es eze')

# def dia_actual(request):
#     fecha = datetime.now()
#     texto = f'Hoy es {fecha.strftime("%d/%m/%Y")}'
#     return HttpResponse(texto)

# def mi_nombre_es(request, nombre):
#     texto = f'Mi nombre es: {nombre}'
#     return HttpResponse(texto)

# def test_template(request):
#     nombre = 'Nicolas'
#     apellido = 'Garzilli'
#     fecha = datetime.now()
#     lista_de_notas = [2,4,6,6,3,8]
#     diccionario1 = {'nombre': nombre, 'apellido': apellido, 'fecha': fecha, 'notas': lista_de_notas}

#     plantilla = loader.get_template('template1.html')

#     documento = plantilla.render(diccionario1)
#     return HttpResponse(documento)
