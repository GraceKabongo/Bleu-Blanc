const menuCategory = document.getElementById("sub-menu-categorie");
const capitalize = (s) => {
  if (typeof s !== "string") return "";
  return s.charAt(0).toUpperCase() + s.slice(1);
};

fetch("/all-category")
  .then((response) => response.json())
  .then((data) => {
    data["category"].forEach((category) => {
      const li = document.createElement("li");
      const a = document.createElement("a");

      category = capitalize(category);

      a.setAttribute("href", `/article/category/${category}`);
      a.innerText = category;
      li.appendChild(a);

      menuCategory.appendChild(li);
    });
  });
