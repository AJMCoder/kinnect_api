from rest_framework import generics, permissions
from kinnect_api.permissions import IsOwnerOrReadOnly
from .models import Rating
from .serializers import RatingSerializer

class RatingList(generics.ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class RatingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        return Rating.objects.filter(owner=self.request.user)