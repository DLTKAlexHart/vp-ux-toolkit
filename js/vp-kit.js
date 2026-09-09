/* ==========================================================================
   vp-kit.js — tiny, dependency-free interactivity for mockups
   Everything is declarative via data attributes; no build step, no imports.

   Tabs:        <button class="vp-tab" data-vp-tab="panelId">
                panels get id="panelId"; siblings toggled automatically.
   Dialogs:     <button data-vp-open="dialogId"> / <button data-vp-close>
                dialog markup: <div class="vp-overlay" hidden></div>
                               <div class="vp-dialog" id="dialogId" hidden>
   Flyout:      <button data-vp-flyout="flyoutId"> toggles .is-open
   Theme:       <button data-vp-theme-toggle> flips html[data-theme="dark"]
   ========================================================================== */

document.addEventListener("click", (e) => {
  // --- tabs ---
  const tab = e.target.closest("[data-vp-tab]");
  if (tab) {
    const group = tab.closest(".vp-tabs");
    if (!group) return;
    group.querySelectorAll(".vp-tab").forEach((t) => t.classList.remove("is-selected"));
    tab.classList.add("is-selected");
    // toggle panels that belong to this tab group, if declared
    const panelId = tab.getAttribute("data-vp-tab");
    if (panelId) {
      group.querySelectorAll("[data-vp-tab]").forEach((t) => {
        const p = document.getElementById(t.getAttribute("data-vp-tab"));
        if (p) p.hidden = t !== tab;
      });
    }
    return;
  }

  // --- open dialog ---
  const opener = e.target.closest("[data-vp-open]");
  if (opener) {
    const dlg = document.getElementById(opener.getAttribute("data-vp-open"));
    if (dlg) {
      dlg.hidden = false;
      const overlay = document.querySelector(".vp-overlay");
      if (overlay) overlay.hidden = false;
    }
    return;
  }

  // --- close dialog ---
  const closer = e.target.closest("[data-vp-close]");
  if (closer) {
    const dlg = closer.closest(".vp-dialog");
    if (dlg) dlg.hidden = true;
    const overlay = document.querySelector(".vp-overlay");
    if (overlay) overlay.hidden = true;
    return;
  }

  // --- nav flyout ---
  const fly = e.target.closest("[data-vp-flyout]");
  if (fly) {
    const el = document.getElementById(fly.getAttribute("data-vp-flyout"));
    if (el) el.classList.toggle("is-open");
    return;
  }

  // --- theme toggle ---
  if (e.target.closest("[data-vp-theme-toggle]")) {
    const html = document.documentElement;
    html.dataset.theme = html.dataset.theme === "dark" ? "" : "dark";
    return;
  }

  // clicking the overlay closes any open dialog
  if (e.target.classList && e.target.classList.contains("vp-overlay")) {
    document.querySelectorAll(".vp-dialog").forEach((d) => (d.hidden = true));
    e.target.hidden = true;
  }
});

// Escape closes dialogs and flyouts
document.addEventListener("keydown", (e) => {
  if (e.key === "Escape") {
    document.querySelectorAll(".vp-dialog").forEach((d) => (d.hidden = true));
    const overlay = document.querySelector(".vp-overlay");
    if (overlay) overlay.hidden = true;
    document.querySelectorAll(".vp-nav-flyout.is-open").forEach((f) => f.classList.remove("is-open"));
  }
});
