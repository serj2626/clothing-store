<script lang="ts" setup>
import { api } from "~/api";
const { $api } = useNuxtApp();

interface IFooterDataResponse {
  site_name: string;
  copyright: string;
  links: ILinkGroup[];
}

export interface ILinkGroup {
  name: string;
  items: ILinkItem[];
}

export interface ILinkItem {
  name: string;
  url: string;
}
const { data: footerData } = useAsyncData<IFooterDataResponse>(
  "footer-info",
  () => $api(api.contacts.footer)
);
</script>
<template>
  <footer class="footer-component">
    <div class="container">
      <FooterContent v-if="footerData?.links" :links="footerData.links" />
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
    color: var(--color-section-title);
    opacity: 0.9;
    text-align: center;
    padding-bottom: 10px;
  }
}
</style>
