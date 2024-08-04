async function getList() {
    let list = await fetch(`/list_files`).then(res => res.json()).then(json => json.response);
    
    if (!(Array.isArray(list) && list.length)) {
        alert("The directory is empty.")
        return;
    }

    return list;
}
