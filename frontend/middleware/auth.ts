export default defineNuxtRouteMiddleware(async (to) => {
  const authStore = useAuthStore()
  
  // Если пользователь не аутентифицирован, перенаправляем на страницу входа
  if (!authStore.isAuthenticated) {
    return navigateTo('/login')
  }
  
  // Пытаемся получить данные пользователя
  try {
    await authStore.fetchUser()
  } catch (error) {
    // Если запрос не удался, разлогиниваем пользователя
    authStore.logout()
    return navigateTo('/login')
  }
})