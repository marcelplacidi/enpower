/* Click a figure to see it larger in a native dialog; Esc or the close button closes it. */
(function () {
  var dlg = document.getElementById("lightbox");
  if (!dlg || typeof dlg.showModal !== "function") return;
  var img = dlg.querySelector(".lightbox__img");
  var cap = dlg.querySelector(".lightbox__caption");
  document.addEventListener("click", function (e) {
    var btn = e.target.closest(".fig__zoom");
    if (!btn) return;
    var src = btn.querySelector("img");
    var fc = btn.parentNode.querySelector("figcaption");
    img.src = src.currentSrc || src.src;
    img.alt = src.alt;
    cap.textContent = fc ? fc.textContent : "";
    dlg.showModal();
  });
  dlg.addEventListener("click", function (e) { if (e.target === dlg) dlg.close(); });
  dlg.addEventListener("close", function () { img.removeAttribute("src"); });
})();
