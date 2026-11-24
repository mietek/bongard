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
.source-row { padding: 0; }
.source-row details { --duration: 200ms; }
.source-row summary { display: flex; align-items: center; width: max-content; gap: .35rem; padding: .65rem var(--cell-inset); cursor: pointer; list-style: none; }
.source-row summary::-webkit-details-marker { display: none; }
.triangle { display: inline-block; line-height: 1; transform: rotate(-90deg); transition: transform var(--duration) ease-in-out; }
.source-row details[open]:not(.closing) .triangle { transform: rotate(0deg); }
.source-reveal { overflow: hidden; transition: height var(--duration) ease-in-out, opacity var(--duration) ease-in-out; }
.source-row .closing .source-reveal { opacity: 0; }
.source-columns { display: grid; grid-template-columns: var(--image-width) minmax(0, 1fr); }
.panel-comparison { display: block; position: relative; }
@media screen and (any-hover: hover) {
  .panel-comparison > span {
    position: absolute;
    left: calc(var(--x) * 100% / 515);
    top: calc(var(--y) * 100% / 326);
    width: calc(100% * 100 / 515);
    height: calc(100% * 100 / 326);
    overflow: hidden;
  }
  .panel-comparison > span:hover::after {
    content: "";
    position: absolute;
    /* Each panel is 100 units square, so 1% of it is one sheet unit. */
    left: calc(-1% * var(--x));
    top: calc(-1% * var(--y));
    width: 515%;
    height: 326%;
    background: var(--derived-sheet) 0 0 / 100% 100% no-repeat;
    pointer-events: none;
  }
}
@media (prefers-reduced-motion: reduce) {
  .source-row .triangle, .source-reveal { transition: none; }
}
</style>
</head>
<body>
<main>
$body$
</main>
</body>
</html>
