from django.db import models

MATCHER_CHOICE = (
    ('MATCHER1','Matcher1'),
    ('MATCHER2','Matcher2'),
)

class Search(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length = 100, blank=True, default='')
    matcher = models.CharField(max_length=10, choices=MATCHER_CHOICE)

    def save(self, *args, **kwargs):
        if self.matcher == 'MATCHER1' or self.matcher == 'MATCHER2':
            print('Valid matcher type, saving: ' + self.name)
            SearchResult.objects.get_or_create(name=self.name,matcher=self.matcher)
            super(Search,self).save(*args,**kwargs)
        else:
            print("Invalid matcher type, not saving: " + self.name)    
        
    
    
class SearchResult(models.Model):
    name = models.CharField(max_length = 100, blank=True, default='')
    matcher = models.CharField(max_length=10, choices=MATCHER_CHOICE)
    status = models.CharField(max_length = 10, default='CREATED')
    percent_complete = models.FloatField(default=0.0)
