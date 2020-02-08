from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import ListView, View
from .models import CrudUser


class CrudView(ListView):
    model = CrudUser
    template_name = 'crud_ajax/crud.html'
    context_object_name = 'users'


class CreateCrudUser(View):
    def get(self, request):
        name = request.GET.get('name', None)
        address = request.GET.get('address', None)
        age = request.GET.get('age', None)

        obj = CrudUser.objects.create(
            name=name,
            address=address,
            age=age,
        )
        user = {
            'id': obj.id,
            'name': obj.name,
            'address': obj.address,
            'age': obj.age

        }
        data = {
            'user': user
        }

        return JsonResponse(data)


class UpdateCrudUser(View):

    def get(self, request):
        id1 = request.GET.get('id', None)
        name = request.GET.get('name', None)
        address = request.GET.get('address', None)
        age = request.GET.get('age', None)

        obj = CrudUser.objects.get(id=id1)
        obj.name = name
        obj.address = address
        obj.age = age
        obj.save()

        user = {
            'id': obj.id,
            'name': obj.name,
            'address': obj.address,
            'age': obj.age,
        }

        data = {
            'user': user
        }
        return JsonResponse(data)


class DeleteCrudUser(View):
    def  get(self, request):
        id1 = request.GET.get('id', None)
        CrudUser.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)