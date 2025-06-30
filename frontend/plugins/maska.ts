import { defineNuxtPlugin } from '#imports'
import { vMaska } from 'maska/vue'

export default defineNuxtPlugin(nuxtApp => {
  nuxtApp.vueApp.directive('maska', vMaska)
})