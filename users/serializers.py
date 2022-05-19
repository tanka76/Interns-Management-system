from rest_framework import serializers
from .models import Attendance, CustomUser,Task,Intern
class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(style={'input_type':'password'})
    class Meta:
        fields = ['email', 'password']




class InternSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intern
        fields = '__all__'

class TaskSerializer(serializers.Serializer):
    class Meta:
        model=Task
        fields = ['task_name', 'description','start_date','deadline','completed']

    def create(self, validated_data):
        task_name=self.context['task_name']
        task_obj = Task.objects.get(task_name=task_name)
        task_obj.completed=True
        task_obj.save()
        return task_obj

class AttendanceSerializer(serializers.Serializer):
    class Meta:
        model=Attendance
        fields = ['present']

    def create(self, validated_data):
        user=self.context.get("user")
        attedance_obj = CustomUser.objects.get(pk=user.id)
        attedance_obj=Attendance.objects.create(user=user)
        attedance_obj.present=True
        attedance_obj.save()
        return attedance_obj



        
