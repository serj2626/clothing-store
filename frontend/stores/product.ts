import { defineStore } from 'pinia'

export const useProductStore = defineStore('product', () => {
  const comments = ref([])
  const likesCount = ref(0)
  const isLiked = ref(false)
  const { $api } = useNuxtApp()

  const fetchComments = async (productId: number) => {
    try {
      const { data } = await $api(`/products/${productId}/comments/`)
      comments.value = data.comments
      likesCount.value = data.likes_count
      isLiked.value = data.is_liked
    } catch (error) {
      console.error('Error fetching comments:', error)
    }
  }

  const addComment = async (commentData: {
    productId: number
    text: string
    rating: number
  }) => {
    // try {
    //   const { data } = await $api.post(`/products/${commentData.productId}/comments/`, {
    //     text: commentData.text,
    //     rating: commentData.rating
    //   })
    //   comments.value.unshift(data.comment)
    // } catch (error) {
    //   throw error
    // }
  }

  const toggleLike = async (productId: number) => {
    try {
      const { data } = await $api.post(`/products/${productId}/toggle-like/`)
      likesCount.value = data.likes_count
      isLiked.value = data.is_liked
    } catch (error) {
      console.error('Error toggling like:', error)
    }
  }

  return {
    comments,
    likesCount,
    isLiked,
    fetchComments,
    addComment,
    toggleLike
  }
})





// # views.py
// from rest_framework import viewsets, permissions
// from rest_framework.decorators import action
// from rest_framework.response import Response
// from .models import Product, Comment, ProductLike
// from .serializers import CommentSerializer

// class ProductViewSet(viewsets.ModelViewSet):
//     # ... ваши существующие методы
    
//     @action(detail=True, methods=['get'])
//     def comments(self, request, pk=None):
//         product = self.get_object()
//         comments = product.comments.all().order_by('-created_at')
//         serializer = CommentSerializer(comments, many=True)
//         return Response({
//             'comments': serializer.data,
//             'likes_count': product.likes.count(),
//             'is_liked': product.likes.filter(user=request.user).exists() if request.user.is_authenticated else False
//         })
    
//     @action(detail=True, methods=['post'])
//     def toggle_like(self, request, pk=None):
//         product = self.get_object()
//         like, created = ProductLike.objects.get_or_create(
//             product=product,
//             user=request.user
//         )
//         if not created:
//             like.delete()
//         return Response({
//             'likes_count': product.likes.count(),
//             'is_liked': not created
//         })

// class CommentViewSet(viewsets.ModelViewSet):
//     serializer_class = CommentSerializer
//     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
//     def get_queryset(self):
//         return Comment.objects.filter(product_id=self.kwargs['product_pk'])
    
//     def perform_create(self, serializer):
//         serializer.save(
//             user=self.request.user,
//             product_id=self.kwargs['product_pk']
//         )