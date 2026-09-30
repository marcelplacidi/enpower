/* Runs before first paint: apply the stored theme, light by default. */
(function () {
  var theme = "light";
  try {
    var stored = localStorage.getItem("enpower-theme");
    if (stored === "dark" || stored === "light") theme = stored;
  } catch (e) {}
  var root = document.documentElement;
  root.setAttribute("data-theme", theme);
  root.classList.add("js");
})();
