const btnNav = document.querySelector(".btn-mobile-nav");
const headerEl = document.querySelector(".header");

btnNav.addEventListener("click", function () {
  headerEl.classList.toggle("nav-open");
});

const allLinks = document.querySelectorAll("a:link");

allLinks.forEach(function (link) {
  link.addEventListener("click", function (e) {
    const href = link.getAttribute("href");

    // SCROLL TO TOP
    if (href === "#")
      window.scrollTo({
        top: 0,
        behavior: "smooth",
      });

    // SCROLL TO OTHER LINKS
    if (href !== "#" && href.startsWith("#")) {
      const sectionEl = document.querySelector(href);
      sectionEl.scrollIntoView({ behavior: "smooth" });
    }

    if (link.classList.contains("main-nav-link")) {
      headerEl.classList.toggle("nav-open");
    }
  });
});

// STICKY NAV
const sectionHeroEl = document.querySelector(".section-hero");

const obs = new IntersectionObserver(
  function (ent) {
    const firstEntry = ent[0];
    if (firstEntry.isIntersecting === false) {
      document.querySelector("body").classList.add("sticky");
    }
    if (firstEntry.isIntersecting) {
      document.querySelector("body").classList.remove("sticky");
    }
  },
  {
    // in the viewport
    root: null,
    threshold: 0,
    rootMargin: "-80px",
  }
);
obs.observe(sectionHeroEl);
