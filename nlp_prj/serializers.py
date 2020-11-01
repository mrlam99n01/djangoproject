from rest_framework import serializers
from .models import Article
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

    def __str__(self):
        return self.data
    def create(self, validated_data):
        return Article.objects.create(**validated_data)
