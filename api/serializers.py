from rest_framework import serializers
from .models import *

class TaskSerializer(serializers.ModelSerializer):
	class Meta:
		model = Task
		fields = ['title', 'completed', 'created', 'updated', 'id']
		read_only_fields = ['created', 'updated', 'id']