const socket = io();

document.getElementById('scan-button').addEventListener('click', () => {
    socket.emit('find_hosts');
});

socket.on('find_hosts', (results) => {
    const resultsList = document.getElementById('results');
    resultsList.innerHTML = '';

    if (results.length == 0) {
        alert("No host found");
        return;
    }
    
    results.forEach(result => {
        const listItem = document.createElement('li');
        const link = document.createElement('a');

        link.href = `/?h=${result}`
        link.textContent = result;

        listItem.appendChild(link);
        resultsList.appendChild(listItem);
    });

    document.getElementById("results-div").classList.remove("hidden");
});
