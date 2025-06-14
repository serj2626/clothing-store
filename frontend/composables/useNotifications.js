// composables/useNotifications.js
export const useNotifications = () => {
  const notifications = ref([])
  const unreadCount = ref(0)
  
  const fetchNotifications = async () => {
    const { data } = await useFetch('/api/notifications/')
    notifications.value = data.value
    unreadCount.value = data.value.filter(n => !n.is_read).length
  }
  
  const markAsRead = async (id) => {
    await useFetch(`/api/notifications/${id}/mark_as_read/`, {
      method: 'PATCH'
    })
    await fetchNotifications()
  }
  
  // Опционально: WebSocket или polling для реального времени
  const setupRealTime = () => {
    setInterval(fetchNotifications, 60000) // Проверка каждую минуту
  }
  
  return {
    notifications,
    unreadCount,
    fetchNotifications,
    markAsRead,
    setupRealTime
  }
}