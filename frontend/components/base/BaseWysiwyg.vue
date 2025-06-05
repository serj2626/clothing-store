<script setup>
defineProps({
  html: {
    type: String,
    default: "",
  },
});
</script>
<template>
  <div v-if="html" class="wysiwyg-component" v-html="html" />
</template>
<style lang="scss" scoped>
.wysiwyg-component {
  color: #2e2e2e;
  font-size: 14px;
  margin-block: 40px;
  @include mediaTablet {
    font-size: 16px;
  }
  :deep(h1) {
    font-weight: 700;
  }
  :deep(h2) {
    font-weight: 700;
  }
  :deep(h3) {
    font-weight: 700;
  }
  :deep(h4) {
    font-weight: 700;
  }
  :deep(h5) {
    font-weight: 700;
  }
  :deep(ul) {
    list-style: disc;
  }
  :deep(li) {
    list-style: disc;
  }
  &:deep(img) {
    margin: 30px 0;
    border-radius: 15px;
  }

  ol {
    counter-reset: num 0;

    li {
      counter-increment: num 1;
      &::before {
        content: counter(num) ". ";
      }

      ol {
        counter-reset: num2 0;

        li {
          counter-increment: num2 1;
          &::before {
            content: counter(num) "." counter(num2) ". ";
          }

          ul {
            li {
              list-style-type: "— ";
              list-style-position: inside;
              &::before {
                content: none;
              }
            }
          }
        }
      }
    }
  }
}
</style>
