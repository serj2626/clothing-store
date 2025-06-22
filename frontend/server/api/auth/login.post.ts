// server/api/auth/login.post.ts
import { defineEventHandler, readBody, setCookie } from 'h3'
export default defineEventHandler(async (event) => {
  const { username, password } = await readBody(event)

  // Отправляем данные на Django backend
  const { data } = await $fetch('https://your-django-api.com/api/token/', {
    username,
    password,
  })

  // ✅ Устанавливаем токены в HttpOnly куки:
  setCookie(event, 'access_token', data.access, {
    httpOnly: true,
    secure: process.env.NODE_ENV === 'production',
    path: '/',
    maxAge: 60 * 15, // 15 минут
    sameSite: 'lax',
  })

  setCookie(event, 'refresh_token', data.refresh, {
    httpOnly: true,
    secure: process.env.NODE_ENV === 'production',
    path: '/',
    maxAge: 60 * 60 * 24 * 7, // 7 дней
    sameSite: 'lax',
  })

  return { success: true }
})
