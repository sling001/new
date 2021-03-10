from rest_framework import viewsets
from .models import ListModel, DispatchListModel
from . import serializers
from utils.page import MyPageNumberPagination
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from .filter import Filter, DispatchFilter
from rest_framework.exceptions import APIException
from .serializers import FileRenderSerializer
from django.http import StreamingHttpResponse
from .files import FileRenderCN, FileRenderEN
from rest_framework.settings import api_settings

class APIViewSet(viewsets.ModelViewSet):
    """
        retrieve:
            Response a data list（get）

        list:
            Response a data list（all）

        create:
            Create a data line（post）

        delete:
            Delete a data line（delete)

        partial_update:
            Partial_update a data（patch：partial_update）

        update:
            Update a data（put：update）
    """
    queryset = ListModel.objects.all()
    serializer_class = serializers.DriverGetSerializer
    pagination_class = MyPageNumberPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter, ]
    ordering_fields = ['id', "create_time", "update_time", ]
    filter_class = Filter

    def get_project(self):
        try:
            id = self.kwargs.get('pk')
            return id
        except:
            return None

    def get_queryset(self):
        id = self.get_project()
        if self.request.user:
            if id is None:
                return self.queryset.filter(openid=self.request.auth.openid, is_delete=False)
            else:
                return self.queryset.filter(openid=self.request.auth.openid, id=id, is_delete=False)
        else:
            return self.queryset.none()

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.DriverGetSerializer
        elif self.action == 'retrieve':
            return serializers.DriverGetSerializer
        elif self.action == 'create':
            return serializers.DriverPostSerializer
        elif self.action == 'update':
            return serializers.DriverUpdateSerializer
        elif self.action == 'partial_update':
            return serializers.DriverPartialUpdateSerializer
        elif self.action == 'destroy':
            return serializers.DriverGetSerializer
        else:
            return self.http_method_not_allowed(request=self.request)

    def create(self, request, *args, **kwargs):
        data = request.data
        if self.queryset.filter(openid=self.request.auth.openid, driver_name=data['driver_name'], is_delete=False).exists():
            raise APIException({"detail": "Data Exists"})
        else:
            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=200, headers=headers)

    def update(self, request, pk):
        qs = self.get_object()
        if qs.openid != self.request.auth.openid:
            raise APIException({"detail": "Cannot Update Data Which Not Yours"})
        else:
            data = request.data
            serializer = self.get_serializer(qs, data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=200, headers=headers)

    def partial_update(self, request, pk):
        qs = self.get_object()
        if qs.openid != self.request.auth.openid:
            raise APIException({"detail": "Cannot Partial Update Data Which Not Yours"})
        else:
            data = self.request.data
            serializer = self.get_serializer(qs, data=data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=200, headers=headers)

    def destroy(self, request, pk):
        qs = self.get_object()
        if qs.openid != self.request.auth.openid:
            raise APIException({"detail": "Cannot Delete Data Which Not Yours"})
        else:
            qs.is_delete = True
            qs.save()
            serializer = self.get_serializer(qs, many=False)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=200, headers=headers)

class DispatchListViewSet(viewsets.ModelViewSet):
    """
        retrieve:
            Response a data list（get）

        list:
            Response a data list（all）
    """
    queryset = DispatchListModel.objects.all()
    serializer_class = serializers.DispatchListGetSerializer
    pagination_class = MyPageNumberPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter, ]
    ordering_fields = ['id', "create_time", "update_time", ]
    filter_class = DispatchFilter

    def get_project(self):
        try:
            id = self.kwargs.get('pk')
            return id
        except:
            return None

    def get_queryset(self):
        id = self.get_project()
        if self.request.user:
            if id is None:
                return self.queryset.filter(openid=self.request.auth.openid)
            else:
                return self.queryset.filter(openid=self.request.auth.openid, id=id)
        else:
            return self.queryset.none()

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.DispatchListGetSerializer
        elif self.action == 'retrieve':
            return serializers.DispatchListGetSerializer
        else:
            return self.http_method_not_allowed(request=self.request)

class FileDownloadView(viewsets.ModelViewSet):
    queryset = ListModel.objects.all()
    serializer_class = serializers.FileRenderSerializer
    renderer_classes = (FileRenderCN, ) + tuple(api_settings.DEFAULT_RENDERER_CLASSES)
    filter_backends = [DjangoFilterBackend, OrderingFilter, ]
    ordering_fields = ['id', "create_time", "update_time", ]
    filter_class = Filter

    def get_project(self):
        try:
            id = self.kwargs.get('pk')
            return id
        except:
            return None

    def get_queryset(self):
        id = self.get_project()
        if self.request.user:
            if id is None:
                return self.queryset.filter(openid=self.request.auth.openid, is_delete=False)
            else:
                return self.queryset.filter(openid=self.request.auth.openid, id=id, is_delete=False)
        else:
            return self.queryset.none()

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.FileRenderSerializer
        else:
            return self.http_method_not_allowed(request=self.request)

    def list(self, request, *args, **kwargs):
        from datetime import datetime
        dt = datetime.now()
        data = (
            FileRenderSerializer(instance).data
            for instance in self.filter_queryset(self.get_queryset())
        )
        if self.request.GET.get('lang', '') == 'zh-hans':
            renderer = FileRenderCN().render(data)
        else:
            renderer = FileRenderEN().render(data)
        response = StreamingHttpResponse(
            renderer,
            content_type="text/csv"
        )
        response['Content-Disposition'] = "attachment; filename='driverlist_{}.csv'".format(str(dt.strftime('%Y%m%d%H%M%S%f')))
        return response
