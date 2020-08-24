from rest_framework import serializers

#analogo ao body parser
class HelloSerializer(serializers.Serializer):
    """serializers a name field for testing our APIView. """

    name = serializers.CharField(max_length=10)
