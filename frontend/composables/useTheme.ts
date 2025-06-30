export const useTheme = () => {
  const theme = useState<"light" | "dark">("theme", () => "light");

  const toggleTheme = () => {
    theme.value = theme.value === "light" ? "dark" : "light";
    document.documentElement.setAttribute("data-theme", theme.value);
  };

  const setTheme = (value: "light" | "dark") => {
    theme.value = value;
    document.documentElement.setAttribute("data-theme", value);
  };

  onMounted(() => {
    document.documentElement.setAttribute("data-theme", theme.value);
  });

  return { theme, toggleTheme, setTheme };
};
