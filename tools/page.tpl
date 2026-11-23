<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>$title$</title>
<style>
:root { color-scheme: light; color: #1f2429; background: white; font-family: system-ui, -apple-system, sans-serif; }
* { box-sizing: border-box; }
body { max-width: 86rem; margin: 0 auto; padding: 1.25rem clamp(.75rem, 3vw, 2.75rem) 2.5rem; line-height: 1.55; }
h1 { font-size: clamp(1.75rem, 3vw, 2.4rem); margin: .25rem 0 1.3rem; }
h2 { font-size: clamp(1.25rem, 2.3vw, 1.65rem); margin: 1.4rem 0 .7rem; }
h1, h2 { line-height: 1.2; }
hr { border: 0; border-top: 1px solid #636c75; margin: 1.7rem 0 1.1rem; }
table { width: 100%; border-collapse: collapse; table-layout: fixed; }
col:first-child { width: var(--image-width); }
td, .source-columns > div { padding: .65rem var(--cell-inset); text-align: left; vertical-align: top; overflow-wrap: anywhere; }
tbody tr + tr td { border-top: 1px solid #d9dee2; }
img { display: block; width: 100%; height: auto; }
a { color: #215b88; text-underline-offset: .15em; }
td p { margin: 0; }
@media (max-width: 38rem) { body { font-size: .9rem; } }

.filters ul { display: flex; flex-wrap: wrap; gap: .3rem .55rem; list-style: none; padding: 0; margin: 0; }
.filters li { white-space: nowrap; }
.filters li:not(:last-child)::after { content: "·"; margin-left: .55rem; }
.filters a { text-decoration: none; }
.filters a:hover, .filters a:focus-visible, .filters a.active { text-decoration: underline; }
.filters a.active { color: inherit; font-weight: 700; }
.record { overflow-x: auto; --image-width: 67%; --cell-inset: clamp(.25rem, 1vw, .85rem); }
.record * + p { margin-top: .5rem; }
.foundalis { padding: 0; }
.foundalis details { position: relative; min-height: 2.8rem; }
.foundalis summary { position: absolute; top: .65rem; left: var(--cell-inset); display: grid; place-items: center; width: 1.5rem; height: 1.5rem; cursor: pointer; list-style: none; }
.foundalis summary::-webkit-details-marker { display: none; }
.foundalis summary span { display: block; line-height: 1; transform: rotate(-90deg); transition: transform 160ms ease-in-out; }
.foundalis details[open] > summary span { transform: rotate(0deg); }
.source-columns { display: grid; grid-template-columns: var(--image-width) minmax(0, 1fr); }
.source-columns > :first-child { padding-left: calc(var(--cell-inset) + 1.75rem); }
@media (prefers-reduced-motion: reduce) {
  .foundalis summary span { transition: none; }
}
</style>
</head>
<body>
<main>
$body$
</main>
</body>
</html>
