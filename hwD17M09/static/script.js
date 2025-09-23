const button = document.querySelector("#button_gen");
const passwordInp = document.querySelector("#password");

button.addEventListener("click", () => {
    fetch('/', {method: "POST", header: {"content-applications": "application/json"}})
    .then((response)=> response.json())
    .then((data) => {
        passwordInp.value = data.pass
    })
});


//document.addEventListener("DOMContentLoaded", function() {
//    const button = document.querySelector("#button_gen");
//    const password = document.querySelector("#password");
//
//
//
//    button.addEventListener("click", (e) => {
//        let newPassword = generate()
//        console.log(`Пароль сгенерирован: ${newPassword}`);
//        password.value = `${newPassword}`;
//    });
//});