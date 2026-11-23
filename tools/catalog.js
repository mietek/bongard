const filterLinks = [...document.querySelectorAll(".filters a[data-show]")];
const problems = document.querySelectorAll("section.problem");
const allProblems = filterLinks.find(link => link.dataset.show === "all");

function showSelectedProblems() {
  const requested = new URLSearchParams(location.search).get("show");
  const selected = filterLinks.find(link => link.dataset.show === requested) ?? allProblems;
  const view = selected.dataset.show;

  for (const link of filterLinks) {
    link.classList.toggle("active", link === selected);
  }
  for (const problem of problems) {
    const status = problem.dataset.flagged === "true" ? "flagged" : "unflagged";
    const difficulty = problem.dataset.difficulty;
    const matchesRating = difficulty ? difficulty === selected.dataset.difficulty : view === "unrated";
    problem.hidden = view !== "all" && view !== status && !matchesRating;
    if (problem.hidden) {
      problem.querySelectorAll(".source-reveal[style]").forEach(finishDisclosure);
    }
  }
}

for (const link of filterLinks) {
  link.addEventListener("click", event => {
    if (event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) {
      return;
    }
    if (link.href !== location.href) {
      try {
        history.pushState(null, "", link.href);
      } catch (error) {
        if (error.name === "SecurityError") return; // Follow the link on restricted file URLs.
        throw error;
      }
    }
    event.preventDefault();
    showSelectedProblems();
  });
}

window.addEventListener("popstate", showSelectedProblems);
showSelectedProblems();

const reducedMotion = matchMedia("(prefers-reduced-motion: reduce)");

function finishDisclosure(reveal) {
  const details = reveal.parentElement;
  if (details.classList.contains("closing")) {
    details.open = false;
    details.classList.remove("closing");
  }
  reveal.style.height = "";
}

document.addEventListener("click", event => {
  const summary = event.target.closest(".source-row summary");
  if (!summary || reducedMotion.matches) return;
  event.preventDefault();

  const details = summary.parentElement;
  const reveal = summary.nextElementSibling;
  const expand = !details.open || details.classList.contains("closing");
  const height = details.open ? reveal.getBoundingClientRect().height : 0;
  reveal.style.height = height + "px";
  if (!details.open) {
    details.classList.add("closing");
    details.open = true;
  }
  // Capture the current height and opacity before transitioning to the new state.
  reveal.getBoundingClientRect();
  details.classList.toggle("closing", !expand);
  const target = expand ? reveal.firstElementChild.getBoundingClientRect().height : 0;
  reveal.style.height = target + "px";
  if (height === target) finishDisclosure(reveal);
});

document.addEventListener("transitionend", event => {
  if (event.target.matches(".source-reveal") && event.propertyName === "height") {
    finishDisclosure(event.target);
  }
});

reducedMotion.addEventListener("change", () => {
  if (reducedMotion.matches) {
    document.querySelectorAll(".source-reveal[style]").forEach(finishDisclosure);
  }
});
