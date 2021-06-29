# Create your views here.
#IMPORT models

#IMPORT LIBRARIRES/FUNCTIONS
from django.shortcuts import render , HttpResponse
from django.http import JsonResponse
import json
#IMPORT DJANGO PASSWORD HASH GENERATOR AND COMPARE
from django.contrib.auth.hashers import make_password, check_password
from .models import Servicios,Pet,Owner

#check_password(noHashPassword,HashedPassword) this funcion validate if the password match to the hash

#def vista(request):
#    return render(request,'clase.html')

def vista(request):
    
    #https://docs.djangoproject.com/en/3.0/ref/templates/language/#templates
    return render(request, 'clase.html', {'title': "Bumblebee" , "otra": "asdassdsdsdd" })



    if request.method == 'GET':

        responseData = {}
        responseData['success'] = 'true'
        responseData['data'] = list(Types.objects.all().values())
        return JsonResponse(responseData, status=200)

    else:

        responseData = {}
        responseData['success'] = 'false'
        responseData['mesage'] = 'Wrong Method'
        return JsonResponse(responseData, status=400)

def servicios(request):
    
    if request.method == 'GET':

        responseData = {}
        responseData['success'] = 'Consulta correcta de los servicios'
        responseData['data'] = list(Servicios.objects.all().values())
        return JsonResponse(responseData, status=200)

    else:

        responseData = {}
        responseData['success'] = 'Consulta no satisfactoria'
        responseData['mesage'] = 'Wrong Method'
        return JsonResponse(responseData, status=400)

def update(request, petid):

    if request.method == 'POST':
        try: 
            one_entry = Pet.objects.get(id_pet=petid)
        except:
            responseData ={}
            responseData['status_message'] = 'The id its not valid'
            responseData['status_code'] = 'False'
            
            return JsonResponse(responseData, status=400)
        try:
            json_object = json.loads(request.body)
            contador = 0
            try:
                value = json_object["name"]
                Pet.objects.filter(id_pet=petid).update(name=value)
                contador = contador +1
            except KeyError:
                responseData={}

            try:
                value = json_object["breed"]
                Pet.objects.filter(id_pet=petid).update(breed=value)
                contador = contador +1
            except KeyError:
                responseData={}

            try:
                value = json_object["age"]
                Pet.objects.filter(id_pet=petid).update(age=value)
                contador = contador +1
            except KeyError:
                responseData={}

            try:
                value = json_object["owner_id"]
                Pet.objects.filter(id_pet=petid).update(owner_id=value)
                contador = contador +1
            except KeyError:
                responseData={}

            try:
                value = json_object["body_color"]
                Pet.objects.filter(id_pet=petid).update(body_color=value)
                contador = contador +1
            except KeyError:
                responseData={}

            try:
                value = json_object["height"]
                Pet.objects.filter(id_pet=petid).update(height=value)
                contador = contador +1
            except KeyError:
                responseData={}

            try:
                value = json_object["weight"]
                Pet.objects.filter(id_pet=petid).update(weight=value)
                contador = contador +1
            except KeyError:
                responseData={}

            try:
                value = json_object["pet_type"]
                Pet.objects.filter(id_pet=petid).update(pet_type=value)
                contador = contador +1
            except KeyError:
                responseData={}

            if contador == 0:
                responseData = {}
                responseData['status_message'] = 'No updated data'
                responseData['status_code'] = 'True'
                return JsonResponse(responseData, status=204)
            else:
                responseData = {}
                responseData['status_message'] = 'Updated pet'
                responseData['status_code'] = 'True'
                return JsonResponse(responseData, status=200)

        except ValueError as e:
            responseData = {}
            responseData['success'] = 'false'
            responseData['data'] = 'Invalid Json'
            responseData['data'] = json.loads(request.body)
            responseData['message2'] = str(e)
            return JsonResponse(responseData, status=400)

    else:
        responseData ={}
        responseData['status_message'] = 'Wrong method'
        responseData['status_code'] = 'False'
        return JsonResponse(responseData, status=404)

def pet(request):
    
    if request.method == 'GET':

        responseData = {}
        responseData['success'] = 'Consulta correcta de los datos de la mascota'
        responseData['data'] = list(Pet.objects.all().values())
        return JsonResponse(responseData, status=200)

    else:

        responseData = {}
        responseData['success'] = 'Consulta no satisfactoria'
        responseData['mesage'] = 'Wrong Method'
        return JsonResponse(responseData, status=400)

def owner(request):
    
    if request.method == 'GET':

        responseData = {}
        responseData['success'] = 'Consulta satisfactoria de los datos del dueño'
        responseData['data'] = list(Owner.objects.all().values())
        return JsonResponse(responseData, status=200)

    else:

        responseData = {}
        responseData['success'] = 'Consulta no satisfactoria'
        responseData['mesage'] = 'Wrong Method'
        return JsonResponse(responseData, status=400)

def petAdd(request):

    if request.method == 'POST':

        try:
            json_object = json.loads(request.body)
            newPet = Pet(name=json_object['name'], breed=json_object['breed'], age=json_object['age'], owner_id= json_object['owner_id'], 
            body_color= json_object['body_color'], height=json_object['height'], weight= json_object['weight'],pet_type= json_object['pet_type'])
            # INSERT INTO pet VALUES (1, "Mocha", "Yorkie", 1, 1, "cafe", 3.2, 42, "perro");
            #name varchar(45) 
            #breed varchar(45) 
            #age int(11) 
            #owner_id int(11) UN 
            #body_color varchar(45) 
            #height float 
            #weight float 
            #pet_type varchar(45)
            newPet.save()
            responseData = {}
            responseData['success'] = 'true'
            responseData['message'] = 'Pet inserted'
            return JsonResponse(responseData, status=200)
        except ValueError as e:
            responseData = {}
            responseData['success'] = 'false'
            responseData['message'] = 'Invalid Json'
            responseData['data'] = json.loads(request.body)
            responseData['message2'] = str(e)
            return JsonResponse(responseData, status=400)

    else:

        responseData = {}
        responseData['success'] = 'false'
        responseData['mesage'] = 'Wrong Method'
        return JsonResponse(responseData, status=400)

def petDelete(request):

    if request.method == 'DELETE':

        try:
            json_object = json.loads(request.body)
            try:
                one_entry = Pet.objects.get(id_pet=json_object["pet_id"])
            except:
                responseData = {}
                responseData['success'] = 'false'
                responseData['message'] = 'The pet_id its not valid'
                return JsonResponse(responseData, status=400)
            Pet.objects.filter(id_pet=json_object["pet_id"]).delete()
            responseData = {}
            responseData['success'] = 'true'
            responseData['message'] = 'The pet has been deleted'
            return JsonResponse(responseData, status=200)
        except ValueError as e:
            responseData = {}
            responseData['success'] = 'false'
            responseData['data'] = 'Invalid Json'
            return JsonResponse(responseData, status=400)
    else:

        responseData = {}
        responseData['success'] = 'false'
        responseData['mesage'] = 'Wrong Method'
        return JsonResponse(responseData, status=400)

def petGet(request,petid):

    if request.method == 'GET':

        try:
            one_entry = Pet.objects.get(id_pet=petid)    
        except:
            responseData = {}
            responseData['success'] = 'false'
            responseData['message'] = 'The pet_id its not valid'
            return JsonResponse(responseData, status=400)
        responseData = {}
        responseData['success'] = 'true'
        responseData['data'] = {}
        responseData['data']['name'] = one_entry.name
        responseData['data']['breed'] = one_entry.breed
        responseData['data']['age'] = one_entry.age
        responseData['data']['owner_id'] = one_entry.owner_id
        responseData['data']['body_color'] = one_entry.body_color
        responseData['data']['height'] = one_entry.height
        responseData['data']['weight'] = one_entry.weight
        responseData['data']['pet_type'] = one_entry.pet_type
        return JsonResponse(responseData, status=200)
        
    else:

        responseData = {}
        responseData['success'] = 'false'
        responseData['mesage'] = 'Wrong Method'
        return JsonResponse(responseData, status=400)







# def searchDish(request, dishId):
#     if request.method == 'GET':
#         try: 
#             one_entry = Dish.objects.get(dish_id=dishId)
#         except:
#             responseData ={}
#             responseData['status_message'] = 'The id its not valid'
#             responseData['status_code'] = 'False'
#             return JsonResponse(responseData, status=400)

#         responseData = {}
        
#         data = list(Dish.objects.filter(dish_id=dishId).values())
#         responseData['data']= data[0]  
#         responseData['status_message'] = 'Conectado'
#         responseData['status_code'] = 'True'
#         return JsonResponse(responseData, status=200)
    
#     else:
#         responseData ={}
#         responseData['status_message'] = 'Wrong method'
#         responseData['status_code'] = 'False'
#         return JsonResponse(responseData, status=404)