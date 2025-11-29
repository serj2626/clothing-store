from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import LikeToggleSerializer
from .services import toggle_like


class LikeToggleAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = LikeToggleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        obj = serializer.validated_data["content_object"]
        liked = toggle_like(request.user, obj)

        return Response(
            {
                "liked": liked,
                "likes_count": obj.likes.count(),
            },
            status=status.HTTP_200_OK,
        )
