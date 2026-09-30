/* Section rail: highlight the section in view, and the mobile menu. */
(function () {
  var rail = document.getElementById("rail");
  var menu = rail && rail.querySelector(".rail__menu");
  var links = Array.prototype.slice.call(document.querySelectorAll(".rail__links a"));

  function closeMenu() {
    if (!rail) return;
    rail.classList.remove("is-open");
    if (menu) menu.setAttribute("aria-expanded", "false");
  }
  if (menu) {
    menu.addEventListener("click", function () {
      var open = rail.classList.toggle("is-open");
      menu.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }
  links.forEach(function (a) { a.addEventListener("click", closeMenu); });
  document.addEventListener("keydown", function (e) { if (e.key === "Escape") closeMenu(); });

  if (!("IntersectionObserver" in window)) return;
  var byId = {};
  links.forEach(function (a) { byId[a.getAttribute("href").slice(1)] = a; });
  var visible = {};
  function update() {
    var best = null;
    links.forEach(function (a) {
      var id = a.getAttribute("href").slice(1);
      if (visible[id] && !best) best = id;
    });
    links.forEach(function (a) {
      if (a.getAttribute("href").slice(1) === best) a.setAttribute("aria-current", "true");
      else a.removeAttribute("aria-current");
    });
  }
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (en) { visible[en.target.id] = en.isIntersecting; });
    update();
  }, { rootMargin: "-35% 0px -55% 0px", threshold: 0 });
  Object.keys(byId).forEach(function (id) {
    var el = document.getElementById(id);
    if (el) io.observe(el);
  });
})();
