export default defineNuxtPlugin(({ $auth }) => {
  console.log('Auth initialized:', $auth?.strategy?.name);
});