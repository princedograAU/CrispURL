from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK
from rest_framework import permissions
from rest_framework.views import APIView

from commons.utils.base62 import generate_random_url
from url_shorter.serializers import URLInputSerializer, URLResponseSerializer
from url_shorter.models import UrlInputFields, UrlShorter
from url_shorter.throttling import LimitUserRequests


class URLView(APIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = URLResponseSerializer
    throttle_classes = (LimitUserRequests,)

    def post(self, request):
        serializer = URLInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        request_params: UrlInputFields = serializer.save()
        return Response(URLResponseSerializer(generate_random_url(request_params)).data, status=HTTP_201_CREATED)

    def get(self, *args, **kwargs):
        if param := self.request.query_params.get('identifier'):
            url_obj = get_object_or_404(UrlShorter, short_url_alias=param)
            url_obj.hits += 1
            url_obj.save()
            return Response(URLResponseSerializer(url_obj).data, status=HTTP_200_OK)
        return Response(URLResponseSerializer(UrlShorter.objects.all(), many=True).data, status=HTTP_200_OK)