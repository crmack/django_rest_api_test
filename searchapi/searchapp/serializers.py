from rest_framework import serializers
from searchapp.models import Search, SearchResult, MATCHER_CHOICE

class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Search
        fields = ('name','matcher')
        
class SearchResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = SearchResult
        fields = ('name','matcher','status','percent_complete')
