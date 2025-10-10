const rubInput = document.querySelector("#rubInp");
const btnConversion = document.querySelector("#conver");

const chbxUSD = document.querySelector("#chbxUsd");
const chbxEU = document.querySelector("#chbxEu");
const chbxUAH = document.querySelector("#chbxUah");
const chbxJPY = document.querySelector("#chbxJpy");
const chbxCHY = document.querySelector("#chbxCny");

const resBox = document.querySelector("#resultRow");

const currencyList = ["USD", "EU", "UAH", "JPY", "CNY"]
const chbxList = [chbxUSD, chbxEU, chbxUAH, chbxJPY, chbxCHY]

btnConversion.addEventListener("click", async ()=>{
    const value = rubInput.value
    let convertList = []

    for (let index = 0; index < chbxList.length; index++) {
        if (chbxList[index].checked) {
            const responce = await fetch("/convert", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({valRub:value, convIn: currencyList[index]})
        });
        convertList.push(await responce.json())
        console.log(convertList, 1-1)
        };
    };
    _addResult(convertList)
});

function _addResult(resultList) {
    resBox.innerHTML = "";

    for (let index = 0; index < resultList.length; index++) {
        let res = resultList[index];
        const elem = document.createElement("div");
        elem.className = "resultElement";
        elem.innerHTML = `
            <p>Операция №${index+1}</p>
            <p>${res.valRub} RUB.</p>
            <p>${res.result.toFixed(2)} ${res.convIn}.</p>
        `;
        resBox.appendChild(elem);
    }
}