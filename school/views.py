from django.shortcuts import render_to_response, redirect
from rest_framework import generics, status
from school.models import Marks, Student, UserType, Parents, Teacher;
from django.contrib.auth.models import User, Group
from school.serializers import MarksSerializer, StudentSerializer,UserSerializer, ParentsSerializer, TeacherSerializer
from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse



# Create your views here.

#create new user
@login_required
def reg_user(request):
    user = request.user
    
    if user.groups.filter(pk = 1).exists() and request.method=='POST':
        username = request.POST.get('username');
        user = User.objects.create(username=username)
        password = request.POST.get('password')
        user.set_password(password)
        user_groups = Group.objects.get(pk=request.POST.get('group'))
        user.groups.add(user_groups)
        
        user.save();
        
        #return redirect('school/userlist/')
        return HttpResponse("DONE BUDDY")
    else: 
        return HttpResponse("NOT ALLOWED BUDDY")
    
    return render_to_response('registration.html', {});

class MarksView(generics.CreateAPIView):
    queryset = Marks.objects.all()
    serializer_class = MarksSerializer
    
