type Theme = "light" | "dark";

export const useTheme = () => {
  const theme = useState<Theme>("theme", () => "light");

  const applyTheme = (value: Theme) => {
    document.documentElement.setAttribute("data-theme", value);
    localStorage.setItem("theme", value);
  };

  const toggleTheme = () => {
    theme.value = theme.value === "light" ? "dark" : "light";
    applyTheme(theme.value);
  };

  const setTheme = (value: Theme) => {
    theme.value = value;
    applyTheme(value);
  };

  onMounted(() => {
    const saved = localStorage.getItem("theme") as Theme | null;
    if (saved === "light" || saved === "dark") {
      setTheme(saved);
    } else {
      // Автовыбор по системной теме
      const prefersDark = window.matchMedia(
        "(prefers-color-scheme: dark)"
      ).matches;
      setTheme(prefersDark ? "dark" : "light");
    }
  });

  return { theme, toggleTheme, setTheme };
};
