<script lang="ts" setup>
import { api } from "~/api";
const { $api } = useNuxtApp();

interface IFooterDataResponse {
  site_name: string;
  copyright: string;
}
const { data: footerData } = useAsyncData<IFooterDataResponse>(
  "footer-info",
  () => $api(api.contacts.footer)
);
</script>
<template>
  <footer class="footer-component">
    <div class="container">
      <FooterContent />
      <p class="footer-component__copyright">
        {{ footerData?.copyright }}
      </p>
    </div>
  </footer>
</template>
<style lang="scss">
.footer-component {
  &__copyright {
    font-weight: 200;
    color: $black;
    opacity: 0.8;
    text-align: center;
    padding-bottom: 10px;
  }
}
</style>
