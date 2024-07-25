if (localStorage.getItem("dark-mode") === undefined)
    localStorage.setItem("dark-mode", "true");

function setTheme() {
    let isDarkMode = localStorage.getItem("dark-mode");
    if (isDarkMode === undefined)
        return;

    if (isDarkMode === "false")
        document.body.classList.remove("dark");
}

function changeTheme() {
    let isDarkMode = localStorage.getItem("dark-mode");
    
    document.body.classList.toggle("dark");
    localStorage.setItem("dark-mode", (isDarkMode === "false") ? "true" : "false");
}
