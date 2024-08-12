from rest_framework import serializers
from .models import Singer, Song

class SingerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Singer
        fields = '__all__'

class SongSerializer(serializers.ModelSerializer):
    singer = SingerSerializer()

    class Meta:
        model = Song
        fields = ['title', 'singer']

    def update(self,instance,validated_data):
        singer_data = validated_data.pop('singer')
        singer = Singer.objects.filter(id = instance.singer.id)
        singer.update(name=singer_data.get('name',instance.singer.name),gender=singer_data.get('gender',instance.singer.gender))
        
        instance.title = validated_data.get('title',instance.title)
        instance.save()

        return instance