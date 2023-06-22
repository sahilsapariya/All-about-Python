# All the logic should be written here

from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *
import re

class UserSerializer(serializers.ModelSerializer):

    class Meta: 
        model = User
        fields = ['username', 'password']
    
    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user


class StudentSerializer(serializers.ModelSerializer):
    # In class Meta two entity are compulsory
    # model and fields
    class Meta:
        model = Student
        # fields = ['name', 'age']
        # exclude = ['id']
        fields = '__all__'
        # extra_kwargs = {
        #     'age': {'required': False}
        # }

    # If we want to add validation then it's logic should be implemented here 
    def validate(self, data):
        if 'age' in data and data['age'] < 18:
            raise serializers.ValidationError({'error': 'age cannot be less than 18'})
        if 'name' in data and re.search(r'\d', data['name']):
            raise serializers.ValidationError({'error': 'name must not contain any digits'})
        return data
    

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name']


class BookSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Book
        fields = '__all__'

    