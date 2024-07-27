if (localStorage.getItem("dark-mode") === undefined)
    localStorage.setItem("dark-mode", "false");

function setTheme() {
    let isDarkMode = localStorage.getItem("dark-mode");
    if (isDarkMode === undefined)
        return;

    if (isDarkMode === "true")
        document.body.classList.add("dark");
}

function changeTheme() {
    let isDarkMode = localStorage.getItem("dark-mode");
    
    document.body.classList.toggle("dark");
    localStorage.setItem("dark-mode", (isDarkMode === "false") ? "true" : "false");
}
