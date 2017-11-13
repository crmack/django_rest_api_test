from django.test import TestCase
from searchapp.models import Search

class SearchTestCase(TestCase):
    
    def setUp(self):
        Search.objects.create(name="Test Search",matcher="MATCHER1")
        Search.objects.create(name="Invalid test search",matcher="MATCHER3")
                
    def test_search(self):
        # Should see one valid, one invalid search creation
        search1 = Search.objects.get(name="Test Search")
        
        
