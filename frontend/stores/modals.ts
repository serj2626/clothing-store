export type ModalItem =
  | "register"
  | "feedback"
  | "login"

  
  | "reviewDetail"
  | "reviewForm"
  | "success"
  | "resetPassword"
  | "changePassword";

export const useModalsStore = defineStore("modals-store", () => {
  const activeModals = ref<Map<ModalItem, any>>(new Map());

  function checkKey(event: KeyboardEvent) {
    if (event.key === "Escape") {
      closeAllModals();
    }
  }

  const openModal = (modal: ModalItem, props?: any) => {
    if (document) {
      document.documentElement.style.overflowY = "hidden";
      document.addEventListener("keydown", checkKey, { once: true });
    }
    activeModals.value.set(modal, props);
  };

  const closeModal = (modal: ModalItem) => {
    activeModals.value.delete(modal);
    if (!activeModals.value.size && document) {
      document.documentElement.style.overflowY = "auto";
    }
  };

  const closeAllModals = () => {
    const headerCatalogMenu = document.getElementById("header-catalog-menu");

    if (menuIsOpen) {
      headerCatalogMenu?.classList.add("header-catalog-menu_close");
      activeModals.value.clear();
      document && (document.documentElement.style.overflowY = "auto");
    }
  };

  const isAnyModalOpen = computed(
    () => activeModals.value && !!activeModals.value.size
  );

  const menuIsOpen = computed(() => activeModals.value.has("register"));

  return {
    activeModals,
    openModal,
    closeModal,
    closeAllModals,
    isAnyModalOpen,
    menuIsOpen,
  };
});
