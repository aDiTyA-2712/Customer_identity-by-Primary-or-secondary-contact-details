from .models import PrimCont
from rest_framework import serializers

class PrimConSerializer(serializers.ModelSerializer):
    class Meta:
        model=PrimCont
        #fields=['id','emails','phones','linked_id','link_precedence','createdAt','updatedAt','deletedAt']
        fields='__all__'


