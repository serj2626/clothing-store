import mediumZoom from "medium-zoom";

export default defineNuxtPlugin(() => {
  return {
    provide: {
      zoom: mediumZoom(),
    },
  };
});