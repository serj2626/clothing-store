import type { IProduct, IProductVariant } from '~/types'

// stores/favorites.ts
import { defineStore } from 'pinia'

export const useFavoritesStore = defineStore('favorites', () => {
  const favorites = ref<Array<{
    id: number
    product: IProduct
    variant: IProductVariant | null
    created_at: string
  }>>([])
  
  const isLoading = ref(false)
  const error = ref(null)

  // Получение списка избранных товаров
  const fetchFavorites = async () => {
    try {
      isLoading.value = true
      const { data } = await useFetch('/api/favorites/my/')
      favorites.value = data.value || []
    } catch (err) {
      error.value = err
    } finally {
      isLoading.value = false
    }
  }

  // Переключение избранного
  const toggleFavorite = async (productId: number, variantId?: number) => {
    try {
      const { data } = await useFetch(`/api/favorites/toggle/${productId}/`, {
        method: 'POST',
        body: { variant_id: variantId }
      })
      await fetchFavorites() // Обновляем список
      return data.value
    } catch (err) {
      console.error('Error toggling favorite:', err)
      throw err
    }
  }

  // Проверка, есть ли товар в избранном
  const isFavorite = (productId: number, variantId?: number) => {
    if (variantId) {
      return favorites.value.some(
        fav => fav.product.id === productId && fav.variant?.id === variantId
      )
    }
    return favorites.value.some(fav => fav.product.id === productId)
  }

  return {
    favorites,
    isLoading,
    error,
    fetchFavorites,
    toggleFavorite,
    isFavorite
  }
})