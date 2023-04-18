from rest_framework import serializers

from tracker.models import StatusChoice, TypeChoice, Task, Project


class ProjectSerializer(serializers.Serializer):
    start_date = serializers.DateTimeField(read_only=True)
    finish_date = serializers.DateTimeField(read_only=True)
    name = serializers.CharField(max_length=200, required=True, allow_blank=True)
    description = serializers.CharField(max_length=1000, min_length=5, required=True, allow_blank=True)


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ('id', 'summary', 'description', 'status', 'type', 'created_at', 'updated_at', 'project')
        read_only_fields = ('updated_at', 'updated_at')

    def create(self, validated_data):
        return Task.objects.create(**validated_data)

    def update(self, instance: Task, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance
