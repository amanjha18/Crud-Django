from django.shortcuts import render
from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UserDetails

class Create(APIView):
    def post(self, request, user_id):
        try:
            capture_name = request.data['capture-name']
            address = request.data['address']
            owner_info = request.data['owner-info']
            employee_size = request.data['employee-size']
            data = UserDetails.objects.create(capture_name=capture_name, user_id=user_id, address=address, owner_info=owner_info, employee_size=employee_size )
            data.save()
            print(data)
            return Response({"status": True, "message": "data created successfully"})
        except:
            return Response({"status": False, "message": "user_id not found"})


class GetAll(APIView):
    def get(self, request):
        try:
            data = UserDetails.objects.all()
            response_list = []
            for i in data:
                dic = {
                    "capture_name": i.capture_name,
                    "address": i.address,
                    "owner_info": i.owner_info,
                    "employee_size": i.employee_size
                }
                response_list.append(dic)
            return Response({"status": True, "data": response_list})
        except:
            return Response({"status": False},status=status.HTTP_404_NOT_FOUND)


class Update(APIView):
    def put(self, request, id ):
        capture_name = request.data['capture-name']
        address = request.data['address']
        owner_info = request.data['owner-info']
        employee_size = request.data['employee-size']
        data = UserDetails.objects.filter(pk=id).update(capture_name=capture_name, address=address,
                                          owner_info=owner_info, employee_size=employee_size)

        return Response({"status": True, "message":"data updated succesfully"})

class Delete(APIView):
    def delete(self, request, id):
        data = UserDetails.objects.get(id=id)
        data.delete()
        return Response({"status": True, "message":"data deleted successfully"})


