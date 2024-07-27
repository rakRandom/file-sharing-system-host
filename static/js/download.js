const input = document.getElementById("file-path");
const button = document.getElementById("submit-button");

button.addEventListener("click", e => {
    e.preventDefault();

    button.innerText = "Downloading File...";
    downloadFile(input.value);
    button.innerText = "Download File";
});

async function downloadFile(name) {
    const credentials = await fetch("/get_host").then(res => res.json()).then(json => json.response);
    console.log(credentials);
    if (!(Array.isArray(credentials) && credentials.length)) {
        alert("Error: fail to get host credentials")
        return;
    }

    let link = document.createElement("a");
    link.style.display = "hidden";
    link.href = `http://${credentials[0]}/download/${name}?p=${credentials[1]}`;
    link.download = "";

    document.body.appendChild(link);
    link.click();
    link.remove();
}