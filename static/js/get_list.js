async function getList() {
    let res = await fetch(`/list_files`).then(res => res.json()).then(json => json.response);
    
    if (!(Array.isArray(res) && res.length)) {
        alert("The directory is empty.")
        return;
    }

    const resultsList = document.getElementById("results");
    resultsList.innerHTML = "";

    res.forEach(name => {
        const listItem = document.createElement('li');
        const link = document.createElement('a');

        link.href = `/download?name=${name}`
        link.textContent = name;

        listItem.appendChild(link);
        resultsList.appendChild(listItem);
    });
}
