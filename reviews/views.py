from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission
from django.http import JsonResponse
from reviews.models import Review
from reviews.serializer import ReviewSerializer
from movies.models import Movie


class ReviewCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Review
    serializer_class = ReviewSerializer

    def delete(self, request, pk, *args, **kwargs):
        try:
            reviews = Review.objects.all()
            review_movie = [review.movie for review in reviews if review.id==pk]
            super().delete(request, *args, **kwargs)

            return JsonResponse(
                {'message': f'a review do filme {review_movie[0]} foi excluido com sucesso'}
            )
        except Exception as error:
            return JsonResponse(
                {'message': f'foi encontrado um erro: {error.args}'}
            )