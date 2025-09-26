const button = document.querySelector("#button_gen");
const passwordInp = document.querySelector("#password");

button.addEventListener("click", () => {
    fetch('/api', {method: "POST", header: {"content-type": "application/json"}})
    .then((response)=> response.json())
    .then((data) => {
        passwordInp.value = data.pass
    })
});