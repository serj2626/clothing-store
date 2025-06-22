// server/api/auth/refresh.post.ts
import { getCookie, setCookie } from "h3";

export default defineEventHandler(async (event) => {
  const refreshToken = getCookie(event, "refresh_token");
  if (!refreshToken) {
    throw createError({ statusCode: 401, statusMessage: "No refresh token" });
  }

  try {
    const { data } = await $fetch(
      "https://your-django-api.com/api/token/refresh/",
      {
        refresh: refreshToken,
      }
    );

    // Обновляем access токен
    setCookie(event, "access_token", data.access, {
      httpOnly: true,
      secure: process.env.NODE_ENV === "production",
      path: "/",
      maxAge: 60 * 15,
      sameSite: "lax",
    });

    return { success: true };
  } catch (e) {
    throw createError({
      statusCode: 401,
      statusMessage: "Token refresh failed",
    });
  }
});
