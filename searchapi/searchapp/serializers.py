from rest_framework import serializers
from searchapp.models import Search, SearchResult, MATCHER_CHOICE

class SearchSerializer(serializers.Serializer):
    class Meta:
        model = Search
        fields = ('name','matcher')
        
class SearchResultSerializer(serializers.Serializer):
    class Meta:
        model = SearchResult
        fields = ('name','matcher','status','percent_complete')
