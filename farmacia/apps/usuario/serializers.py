from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import Usuario


# 🔹 Serializer del modelo Usuario
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'


# 🔹 Serializer personalizado para generar el token JWT
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Serializer personalizado que agrega información adicional del usuario
    dentro del token JWT y en la respuesta del login.
    """
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # 🔸 Campos personalizados que aparecerán dentro del token
        token['username'] = user.username
        token['email'] = user.email
        token['telefono'] = user.telefono
        token['rol'] = user.rol.name if user.rol else None

        return token

    def validate(self, attrs):
        data = super().validate(attrs)

        # 🔹 Estructura organizada para el frontend
        data['user'] = {
            'username': self.user.username,
            'email': self.user.email,
            'telefono': self.user.telefono,
            'rol': self.user.rol.name if self.user.rol else None,
        }

        return data