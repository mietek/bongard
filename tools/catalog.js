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
