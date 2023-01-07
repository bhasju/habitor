from rest_framework import serializers
from dailies.models import task, subtask



class subtaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = subtask
        fields = ["title",  "description", "points"]

class taskSerializer(serializers.ModelSerializer):
    subtask = subtaskSerializer(source="subtask_set", many=True)
    class Meta:
        model = task
        fields = ["title",  "description", "points", "subtask"]