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
th, td { padding: .65rem clamp(.25rem, 1vw, .85rem); text-align: left; vertical-align: top; overflow-wrap: anywhere; }
th { font-weight: 650; border-bottom: 1px solid #a5adb4; }
tbody tr + tr td { border-top: 1px solid #d9dee2; }
img { display: block; width: 100%; height: auto; }
a { color: #215b88; text-underline-offset: .15em; }
td p { margin: 0; }
@media (max-width: 38rem) { body { font-size: .9rem; } }

td object[type="image/svg+xml"], .sheet-map { display:block; width:100%; height:auto; aspect-ratio:515/326; }
$if(catalog)$
.record { overflow-x: auto; }
.record tbody th { border-bottom: 0; }
.record tbody tr + tr th { border-top: 1px solid #d9dee2; }
@media (max-width: 42rem) {
  .record table { min-width: 36rem; }
  .record tr > :first-child { position: sticky; left: 0; z-index: 1; background: white; }
}
$endif$
$if(zoom)$
.derived-sheet { position: relative; }
.derived-sheet > img { width: 100%; height: auto; }
.derived-sheet > .sheet-map { position: absolute; inset: 0; }
.sheet-map a { cursor: pointer; }
.sheet-map a:hover rect, .sheet-map a:focus-visible rect { stroke: currentColor; stroke-width: 2; }
.individual { display: none; scroll-margin: 1rem; }
.individual:target { display: block; }
table:has(+ .details > .individual:target) { display: none; }
.individual h3 { margin: 0 0 .6rem; }
.individual img { width: min(65vw, 20rem); height: auto; border: 1px solid #9da4a9; }
.individual p { margin: .65rem 0 0; }
$endif$</style>
</head>
<body>
<main>
$body$
</main>
</body>
</html>
