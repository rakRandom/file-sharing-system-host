const hostCode = document.getElementById("host-code");
const hostPassword = document.getElementById("host-password");

document
.getElementById("submit-button")
.addEventListener("click", async e => {
    e.preventDefault();

    let res = await fetch(`/connect?c=${hostCode.value}&p=${hostPassword.value}`).then(res => res.json());

    switch (res.error) {
        case 0:
            window.location.href = "/download";
            break;
        case 1:
            alert("Host not found");
            break;
        case 2:
            alert("Host code or password is incorrect");
            break;
        default:
            break;
    }
});
