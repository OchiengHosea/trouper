from django.db import models

from base.utils import get_uuid

class BaseModelIdOnly(models.Model):
    id = models.UUIDField(primary_key=True, default=get_uuid, editable=False)

    class Meta:
        abstract = True
        
class BaseModel(BaseModelIdOnly):
    created_on = models.DateTimeField(auto_now_add=True, editable=False)
    modified_on = models.DateTimeField(auto_now=True, editable=False)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        abstract = True