from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from searchapp.models import Search, SearchResult
from searchapp.serializers import SearchSerializer, SearchResultSerializer


@api_view(['GET', 'POST'])
def search_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        searches = SearchResult.objects.all()
        serializer = SearchResultSerializer(searches, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        serializer = SearchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
