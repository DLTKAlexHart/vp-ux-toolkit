/* ==========================================================================
   vp-nav.js — optional helpers that render the floating nav and utility rail
   from plain arrays. Needs css/vp-hicons.css (Harmony icon font).
   Everything is plain functions on window; no build step, no imports.

   vpIcon(name, small?)                 -> '<i class="vp-hicon vp-hicon--NAME">'
   vpNav.render(target, items, opts?)   -> floating nav; target = selector|element
       items: [{ title, icon }, { divider: true }, …]   icon = vp-hicon name
       opts:  { selected: "Dashboards", onSelect(item, button) }
   vpUtilityRail.render(target, opts?)  -> floating utility rail
       opts:  { notifications: true, onDela(button) }

   The markup these produce is documented in docs/COMPONENTS.md; copy that
   instead if you don't want a script.
   ========================================================================== */

window.vpIcon = (name, small) =>
  `<i class="vp-hicon${small ? " vp-hicon--sm" : ""} vp-hicon--${name}"></i>`;

(function () {
  const el = (t) => (typeof t === "string" ? document.querySelector(t) : t);
  const esc = (s) => String(s).replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));

  window.vpNav = {
    render(target, items, opts = {}) {
      const host = el(target);
      host.innerHTML =
        `<nav class="vp-nav vp-nav--floating">` +
        items.map((i) => i.divider
          ? `<div class="vp-nav__divider"></div>`
          : `<button class="vp-nav__item${i.title === opts.selected ? " is-selected" : ""}" title="${esc(i.title)}" aria-label="${esc(i.title)}">${vpIcon(i.icon)}</button>`
        ).join("") + `</nav>`;
      const real = items.filter((i) => !i.divider);
      host.querySelectorAll(".vp-nav__item").forEach((b, n) =>
        b.addEventListener("click", () => {
          host.querySelectorAll(".vp-nav__item").forEach((x) => x.classList.toggle("is-selected", x === b));
          if (opts.onSelect) opts.onSelect(real[n], b);
        }));
      return host;
    },
  };

  window.vpUtilityRail = {
    render(target, opts = {}) {
      const host = el(target);
      const dela = [1, 2, 3, 4].map((n) => `<span class="vp-hicon vp-hicon--dela-${n}"></span>`).join("");
      host.innerHTML =
        `<aside class="vp-utility-rail vp-utility-rail--floating">` +
        `<button class="vp-utility-rail__item vp-utility-rail__item--dela" title="Ask Dela" aria-label="Ask Dela"><i class="vp-hicon vp-dela">${dela}</i></button>` +
        `<button class="vp-utility-rail__item" title="Insights" aria-label="Insights">${vpIcon("sparkles")}</button>` +
        `<button class="vp-utility-rail__item" title="Notifications" aria-label="Notifications">${vpIcon("bell")}${opts.notifications === false ? "" : `<span class="vp-badge-dot"></span>`}</button>` +
        `<button class="vp-utility-rail__item" title="Help" aria-label="Help">${vpIcon("help")}</button>` +
        `</aside>`;
      if (opts.onDela) host.querySelector(".vp-utility-rail__item--dela").addEventListener("click", (e) => opts.onDela(e.currentTarget));
      return host;
    },
  };
})();
