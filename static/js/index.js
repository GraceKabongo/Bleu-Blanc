const categorieDropdown = document.getElementById("categorie-dropdown");
const humberger = document.getElementById("humberger");
let startTimer = false;
let time = 0;

// Categorie Dropdown Event
categorieDropdown.addEventListener("click", () => {
  const subMenuBcategorie = document.querySelector(".sub-menu-categorie");
  subMenuBcategorie.classList.toggle("show");

  if (subMenuBcategorie.classList.contains("show")) {
    categorieDropdown.lastChild.style.transform = "rotate(0)";
  } else {
    categorieDropdown.lastChild.style.transform = "rotate(180deg)";
  }
});

// Humberger Event
humberger.addEventListener("click", () => {
  const linkMenu = document.querySelector(".link").firstElementChild;
  humberger.classList.toggle("open");
  linkMenu.classList.toggle("show");
});

const removeStyles = (el) => {
  el.removeAttribute("style");

  if (el.childNodes.length > 0) {
    for (let child in el.childNodes) {
      if (el.childNodes[child].nodeType == 1)
        removeStyles(el.childNodes[child]);
    }
  }
};

menu = categorieDropdown.parentElement.parentElement;

if (window.location.pathname === "/")
  menu.querySelector("li:nth-child(1)").classList.add("active");
else if (
  window.location.pathname.includes("/article") &&
  !window.location.pathname.includes("article/search/")
)
  menu.querySelector("li:nth-child(2)").classList.add("active");
else if (window.location.pathname.includes("/about"))
  menu.querySelector("li:nth-child(3)").classList.add("active");

removeStyles(document.body);
