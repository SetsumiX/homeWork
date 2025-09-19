document.addEventListener("DOMContentLoaded", function(){
    const buttonChange1 = document.querySelector(".btn1");
    const buttonChange2 = document.querySelector(".btn2");
    const buttonChange3 = document.querySelector(".btn3");
    const buttonChange4 = document.querySelector(".btn4");
    const messageChange = document.getElementById("messageChange");
    const textP1 = document.querySelector(".frstP")
    const textP2 = document.querySelector(".scndP")
    const textP3 = document.querySelector(".thrdP")
    const textP4 = document.querySelector(".fourP")
    const miku = document.querySelector(".mku")

    let count = 0

    buttonChange1.addEventListener("click", (e)=> {
        console.log("Colour for 1 was changed")
        messageChange.innerHTML = `<span style=color:lightblue;>Цвет первого блока был изменён</span>`;
        textP1.style.backgroundColor = `grey`

        count+=1
        if (count == 4){
            messageChange.innerHTML = `<p style=color:red;>Поздравляем вы нажали 4 раза на кнопочки, или закрасили все блоки в серый</p>`
            miku.style.display = `flex`
        }
    })
    buttonChange2.addEventListener("click", (e)=> {
        console.log("Colour for 2 was changed")
        messageChange.innerHTML = `<span style=color:lightblue;>Цвет второго блока был изменён</span>`;
        textP2.style.backgroundColor = `grey`

        count+=1
        if (count == 4){
            messageChange.innerHTML = `<p style=color:red;>Поздравляем вы нажали 4 раза на кнопочки, или закрасили все блоки в серый</p>`
            miku.style.display = `flex`
        }
    })
    buttonChange3.addEventListener("click", (e)=> {
        console.log("Colour for 3 was changed")
        messageChange.innerHTML = `<span style=color:lightblue;>Цвет третьего блока был изменён</span>`;
        textP3.style.backgroundColor = `grey`

        count+=1
        if (count == 4){
            messageChange.innerHTML = `<p style=color:red;>Поздравляем вы нажали 4 раза на кнопочки, или закрасили все блоки в серый</p>`
            miku.style.display = `flex`
        }
    })
    buttonChange4.addEventListener("click", (e)=> {
        console.log("Colour for 4 was changed")
        messageChange.innerHTML = `<span style=color:lightblue;>Цвет четвёртого блока был изменён</span>`;
        textP4.style.backgroundColor = `grey`

        count+=1
        if (count == 4){
            messageChange.innerHTML = `<p style=color:red;>Поздравляем вы нажали 4 раза на кнопочки, или закрасили все блоки в серый</p>`
            miku.style.display = `flex`
        }
    })
})