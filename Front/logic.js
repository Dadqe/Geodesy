class Points {
    Deg = null;
    Min = null;
    Sec = null;
    HorDist = null;
}
var aPoints = [];
function CreateTable() {
    let input = document.getElementById("input");

    let container = document.getElementById("container");
    let tbody = document.getElementById("tbody_container");
    tbody.innerHTML = "";
    let header_container = document.getElementById("header_container");
    header_container.style.display = "none";
    //container.innerHTML = "";
    if (input.value != "0" && input.value != 0) {
        for (let i = 0; i < input.value; i++) {
            // let newInput = document.createElement("input");
            // newInput.id = "newinput" + i;
            // newInput.classList.add("for_new_input");
            // newInput.value = "0";
            // container.appendChild(newInput);
            header_container.style.display = "table";
            AddRow();

        }
        // let q = tbody.childElementCount;
        // let del = document.getElementById("Distan" + q);

        // del.remove();
        // let newButton = document.createElement("button");
        // newButton.innerText = "Кнопочка";
        // newButton.addEventListener("click", function () {
        //     let inputs = Array.from(document.querySelectorAll(".for_new_input"));
        //     if (inputs) {
        //         inputs.map((item) => console.log(item.id + ": " + item.value)
        //         )
        //     }
        // });
        // container.appendChild(newButton);
    }


    //console.log(input.value);
}
function change() {
    let input = document.getElementById("input");
    let label = document.getElementById("label");
    label.innerHTML = input.value;
}
function addtest(text, i) {
    let div = document.getElementById("test_con");
    let p = document.createElement("p");
    p.innerHTML = text;
    p.style.transition = "1s"
    p.style.opacity = 0;
    setTimeout(() => { p.style.opacity = 1 }, i * 100)
    div.appendChild(p);
}

function click123() {
    let loader = document.getElementById("loader");
    loader.style.display = "flex";
    fetch('https://dummyjson.com/products')
        .then(res => res.json())
        .then(item => {
            document.getElementById("test_con").innerHTML = "";
            for (let i = 0; i < item.products.length; i++) {
                addtest(item.products[i].title, i);
            }

            loader.style.display = "none";
        }
        );
}

function click321() {
    // let response = await fetch('https://localhost:44370/api/values', {
    //     cache: "no-cache",
    //     //mode: "no-cors",
    //     method: 'GET',
    //     headers: {
    //         'Content-Type': 'application/json'
    //     }
    // });
    // let result = await response.json();
    // console.log(result)

    fetch('http://127.0.0.1:8000/')
        .then(res => res.json())
        .then(item => {
            console.log(item)
        }
        );
    /*class test1234 {
        par1 = null;
        par2 = null;
        par3 = null;
    }
    let test123 = new test1234();
    test123.par1="123";
    test123.par2="2345";
    console.log(test123);

    fetch('https://localhost:44370/api/values', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            test123
        })

    })
        .then(res => res.json())
        .then(item => {
            console.log(item)
        }
        );*/


}

function CreateHeader() {
    let container = document.getElementById("header_container");
    let table = document.createElement("table");
    /*Заголовки*/
    let thead = document.createElement("thead");
    let trthead1 = document.createElement("tr");
    let thtr11 = document.createElement("th");
    thtr11.innerHTML = "Номер";
    let thtr12 = document.createElement("th");
    thtr12.innerHTML = "Градус";
    let thtr13 = document.createElement("th");
    thtr13.innerHTML = "Минута";
    let thtr14 = document.createElement("th");
    thtr14.innerHTML = "Секунда";
    let thtr15 = document.createElement("th");
    thtr15.innerHTML = "Градус";
    let thtr16 = document.createElement("th");
    thtr16.innerHTML = "Минута";
    let thtr17 = document.createElement("th");
    thtr17.innerHTML = "Секунда";
    let thtr18 = document.createElement("th");
    thtr18.innerHTML = "Расстояние";
    trthead1.appendChild(thtr11);
    trthead1.appendChild(thtr12);
    trthead1.appendChild(thtr13);
    trthead1.appendChild(thtr14);
    trthead1.appendChild(thtr15);
    trthead1.appendChild(thtr16);
    trthead1.appendChild(thtr17);
    trthead1.appendChild(thtr18);
    thead.appendChild(trthead1);

    let trthead2 = document.createElement("tr");
    let thtr21 = document.createElement("th");
    thtr21.innerHTML = "";
    let thtr22 = document.createElement("th");
    thtr22.innerHTML = "Измеренные углы";
    thtr22.colSpan = 3;
    let thtr23 = document.createElement("th");
    thtr23.innerHTML = "Исправленные углы";
    thtr23.colSpan = 3;
    let thtr24 = document.createElement("th");
    thtr24.innerHTML = "";

    trthead2.appendChild(thtr21);
    trthead2.appendChild(thtr22);
    trthead2.appendChild(thtr23);
    trthead2.appendChild(thtr24);
    thead.appendChild(trthead2);
    table.appendChild(thead);
    container.appendChild(table);
    /*Заголовки*/
    let tbody = document.createElement("tbody");
}

function AddRow() {
    let tbody = document.getElementById("tbody_container");
    let index = tbody.childElementCount + 1;
    //console.log(index);
    let tr = document.createElement("tr");
    tr.id = "row" + index;
    let td1 = document.createElement("td");
    let label = document.createElement("label");
    label.id = "l" + index;
    label.innerHTML = index;
    td1.appendChild(label);
    let td2 = document.createElement("td");
    let inputDeg = document.createElement("input");
    inputDeg.id = "Deg" + index;
    inputDeg.value = 0;
    td2.appendChild(inputDeg);
    let td3 = document.createElement("td");
    let inputMin = document.createElement("input");
    inputMin.id = "Min" + index;
    inputMin.value = 0;
    td3.appendChild(inputMin);
    let td4 = document.createElement("td");
    let inputSec = document.createElement("input");
    inputSec.id = "Sec" + index;
    inputSec.value = 0;
    td4.appendChild(inputSec);
    let td5 = document.createElement("td");
    let inputDegRead = document.createElement("input");
    inputDegRead.id = "DegRead" + index;
    inputDegRead.disabled = true;
    td5.appendChild(inputDegRead);
    let td6 = document.createElement("td");
    let inputMinRead = document.createElement("input");
    inputMinRead.id = "MinRead" + index;
    inputMinRead.disabled = true;
    td6.appendChild(inputMinRead);
    let td7 = document.createElement("td");
    let inputSecRead = document.createElement("input");
    inputSecRead.id = "SecRead" + index;
    inputSecRead.disabled = true;
    td7.appendChild(inputSecRead);
    let td8 = document.createElement("td");
    let inputDistan = document.createElement("input");
    inputDistan.id = "Distan" + index;
    inputDistan.value = 0;
    inputDistan.classList.add("distant_input");
    td8.appendChild(inputDistan);
    tr.appendChild(td1);
    tr.appendChild(td2);
    tr.appendChild(td3);
    tr.appendChild(td4);
    tr.appendChild(td5);
    tr.appendChild(td6);
    tr.appendChild(td7);
    tr.appendChild(td8);
    tbody.appendChild(tr);
}

function MoreRow() {
    let input = document.getElementById("input");

    let newval = Number(input.value);
    input.value = newval + 1;
    let label = document.getElementById("label");
    label.innerHTML = input.value;
    AddRow()
}



function submit() {
    let tbody = document.getElementById("tbody_container");
    let cntRows = tbody.childElementCount;
    aPoints = [];
    for (let i = 1; i < cntRows + 1; i++) {
        let record = new Points();
        let Deg = document.getElementById("Deg" + i);
        let Min = document.getElementById("Min" + i);
        let Sec = document.getElementById("Sec" + i);
        let HorDist = document.getElementById("Distan" + i);
        record.Deg = Deg.value;
        record.Min = Min.value;
        record.Sec = Sec.value;
        record.HorDist = HorDist.value;
        // if (i < cntRows) {


        // }
        aPoints.push(record);
    }
    console.log(aPoints);

    let loader = document.getElementById("loader");
    loader.style.display = "flex";

    let otherValues = document.getElementById("other_values");

    fetch('http://127.0.0.1:8000/Test2', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', 'accept': '*/*' },
        body: JSON.stringify({
            aPoints
        })

    })
        .then(res => res.json())
        .then(item => {
            console.log(item)
        }
        )
        .catch((ex) => {
            if (ex.message == "Failed to fetch") {
                console.warn("Ошибка запроса");
            } else {
                console.error(ex)
            }
        })
        .finally(() => {
            loader.style.display = "none";
            console.info("finally");
            otherValues.style.display = "block";
        });

}
