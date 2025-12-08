export default defineNuxtRouteMiddleware((to, from) => {
  const history = useState<{ name: string; fullPath: string }[]>(
    "routeHistory",
    () => []
  );

  if (!from.fullPath) return;

  history.value.push({
    name: to.name as string,
    fullPath: to.fullPath
  });
});
