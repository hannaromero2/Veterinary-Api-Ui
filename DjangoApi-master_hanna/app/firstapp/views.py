# Create your views here.
#IMPORT models

#IMPORT LIBRARIRES/FUNCTIONS
from django.shortcuts import render , HttpResponse,redirect
from django.http import JsonResponse
import json
import requests
#IMPORT DJANGO PASSWORD HASH GENERATOR AND COMPARE
from django.contrib.auth.hashers import make_password, check_password
from .models import Dogs,Types

#check_password(noHashPassword,HashedPassword) this funcion validate if the password match to the hash

#def vista(request):
#    return render(request,'clase.html')

def vista(request):

    query = "batman"
    apiKey = "c809e516f37fa7407b060cc0dd57bce4"

    #API URL
    url = 'https://api.themoviedb.org/3/search/movie?query=' + query + '&api_key=' + apiKey;

    response = requests.get(url)
    result = response.json()
    cuantos = len(result['results']);

    #post_data = {'remote_api_file_field': self.file}
    #requests.post(REMOTE_API_URL, data=post_data)

    #url = 'https://www.googleapis.com/urlshortener/v1/url'
    #data = {'longUrl': 'http://www.google.com/'}
    #headers = {'Content-Type': 'application/json'}

    #response = requests.post(url, data=json.dumps(data), headers=headers)

    return render(request, 'clase.html', {'cuantos': cuantos , "movies": result })
    #return JsonResponse(result)


def vetApi(request):

    r = requests.get('http://host.docker.internal:8000/pet')

    result = r.json()
    return render(request, "vetapi.html", {"mascotas": result })
 
def Editar(request, mascotasId):
    Url = "http://host.docker.internal:8000/pet/search/" + str(mascotasId)
    
    response = requests.get(Url)

    result = response.json()
    # return JsonResponse(result)
    return render(request, 'editar.html',  {"mascotas": result['data'],"id_mascota": mascotasId , "Accion": "Editar" })

def Update(request,petid):
    
    data = request.POST

    Url="http://host.docker.internal:8000/pet/update/"+ str(petid)

    response = requests.post(Url, json=data)
    result = response.json()
    
    return redirect('/')

def Agregar(request):
    
    # return JsonResponse(result)
    return render(request, 'agregar.html',  {"Accion": "Agregar" })

def Add(request):
    Url= "http://host.docker.internal:8000/pet/add"
    datos= request.POST
    response= requests.post(Url,json=datos)
    result=response.json()
    #return JsonResponse(result)
    return redirect("/")


def delete (request, petid):
    Url = "http://host.docker.internal:8000/pet/delete"
    Json_Delete={
        "pet_id" : str(petid)
    }
    #return  JsonResponse(Json_Delete)
    response = requests.delete(Url, json= Json_Delete)

    result = response.json()
    #return JsonResponse(result)
    return redirect('/')