# Fonts

Templates load **Lexend** from Google Fonts (the product's UI font); offline,
the product fallback stack (tahoma, calibri, trebuchet ms) applies.

Optional: to use the product's **Harmony icon font** (instead of the kit's SVG
sprite), copy `Harmony.woff2` from the product repo (`fonts/` next to the
product stylesheets) into this folder and add to a page or css file:

    @font-face {
      font-family: "Harmony";
      src: url("../fonts/Harmony.woff2") format("woff2");
      font-display: block;
    }

The glyph map (`--harmony-icon-*` codepoint tokens) is already included in
`css/vp-tokens.css`, so e.g.:

    .my-icon::before { font-family: var(--font-family); content: var(--harmony-icon-calculator); }
