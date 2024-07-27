const input = document.getElementById("file-path");
const button = document.getElementById("submit-button");

button.addEventListener("click", e => {
    e.preventDefault();

    button.innerText = "Downloading File...";
    downloadFile(input.value);
    button.innerText = "Download File";
});

async function downloadFile(path) {
    let link = document.createElement("a");
    link.style.display = "hidden";
    link.href = "/download/" + path;
    link.download = "";

    document.body.appendChild(link);
    link.click();
    link.remove();
}
