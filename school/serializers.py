from school.models import USER_TYPE, UserType, Student, Parents, Teacher, Marks
from rest_framework import serializers
from django.contrib.auth.models import User


#serializer class for student

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'password',)
    
    
        


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('name', 'class_field', 'section','marks')
        

#serializer class for parents
class ParentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parents
        fields = ('name_parents', 'student', 'email', 'usertype')

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('name_teacher','class_field_teacher', 'section', 'email', 'usertype')


class MarksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marks
        fields = ('subject1', 'subject2')
