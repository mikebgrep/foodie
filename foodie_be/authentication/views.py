from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from .serializers import UserSerializer
from ..foodie.HeaderAuthentication import HeaderAuthentication


class SignUpView(CreateAPIView):
    authentication_classes = [HeaderAuthentication]
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )



