from django.test import TestCase
from rest_framework.test import APITestCase
import json
from searchapp.models import Search
from .views import search_list


class SearchesTests(APITestCase):
    
    def setUp(self):
        # Add two valid searches and one invalid
        Search.objects.create(name="Test Search",matcher="MATCHER1")
        Search.objects.create(name="Test Search 2",matcher="MATCHER2")
        Search.objects.create(name="Invalid test search",matcher="MATCHER3")
                
    def test_search_results(self):
        # Test that the setup searches are there and correct
        response = self.client.get('/searches/')
        jsonresp = json.loads(response.content)
        self.assertEqual(len(jsonresp),2)
        self.assertEqual(jsonresp[0]['name'],"Test Search")
        self.assertEqual(jsonresp[0]['matcher'],"MATCHER1")
        self.assertEqual(jsonresp[1]['name'],"Test Search 2")
        self.assertEqual(jsonresp[1]['matcher'],"MATCHER2")
        # Make sure the invalid search wasn't added
        for search in jsonresp:
            self.assertNotEqual(search['name'],"Invalid test search")

    def test_submit_search(self):
        # Test that we can submit a new search item
        self.client.post('/searches/', {'name': 'third test search', 'matcher': 'MATCHER2'}, format='json')
        response = self.client.get('/searches/')
        jsonresp = json.loads(response.content)
        self.assertEqual(len(jsonresp),3)
        self.assertEqual(jsonresp[2]['name'],"third test search")
        self.assertEqual(jsonresp[2]['matcher'],"MATCHER2")
