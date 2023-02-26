from rest_framework.response import Response
from rest_framework.decorators import api_view
from myapp.models import Item
from .serializers import ItemSerializers

@api_view(['GET'])
def getData(request):
    # person={'name':'Dennis','age':28}
    items= Item.objects.all()
    serializer = ItemSerializers(items, many=True)
    return Response(serializer.data)

@api_view(["POST"])
def addItem(request):
    serializer=ItemSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(["DELETE"])
def deleteItem(self,pk):
    items= Item.objects.all()
    serializer=self.get_object(pk)
    serializer.delete()
    return Response(items)