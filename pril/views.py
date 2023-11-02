import time

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from pril.models import Pass, Item
from pril.serializers import PassSerializer, ItemSerializer


@api_view(http_method_names=["post", "get"])
@permission_classes([IsAuthenticated])
def import_data(request):
    if request.method == 'GET':
        pass_model = Pass.objects.first()
        return Response(
            data={
                "user": request.user.id,
                "file_name": request.query_params.get("file_name"),
                "result by serializer": PassSerializer(pass_model).data
            }, status=status.HTTP_201_CREATED
        )

    name_format = request.query_params.get("file_name", "name.csv")
    list(name_format)
    name_file, data_format = name_format.rsplit(".")
    pass_model, _ = Pass.objects.get_or_create(name=name_file)

    return Response(data=f'{name_file}, {data_format}, {request.user.id}', status=status.HTTP_201_CREATED)


class PassViewSet(ModelViewSet):
    queryset = Pass.objects.all()
    serializer_class = PassSerializer

    def perform_create(self, serializer):
        temp = self.request.GET.get("file_name")
        serializer.save(name=temp)


class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def perform_create(self, serializer):
        temp, _ = Pass.objects.get_or_create(name=self.request.user.id)
        title_str = self.request.GET.get("file_name")
        serializer.save(pass_fk=temp.id, title=title_str)
