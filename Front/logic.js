class Points {
    Deg = null;
    Min = null;
    Sec = null;
    HorDist = null;
}
class BearingAngle {
    Deg = null;
    Min = null;
    Sec = null;
}
class Coords {
    X = null;
    Y = null;
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
        //AddBearingAngleRow();
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

function AddBearingAngleRow() {
    let tbody = document.getElementById("tbody_container");
    let tr = document.createElement("tr");
    tr.id = "row_BearingAngle";
    let td1 = document.createElement("td");
    let label = document.createElement("label");
    label.id = "l";
    label.innerHTML = "dir";
    td1.appendChild(label);
    let td2 = document.createElement("td");
    let inputDeg = document.createElement("input");
    inputDeg.id = "Deg";
    inputDeg.value = 0;
    //td2.appendChild(inputDeg);
    let td3 = document.createElement("td");
    let inputMin = document.createElement("input");
    inputMin.id = "Min";
    inputMin.value = 0;
    //td3.appendChild(inputMin);
    let td4 = document.createElement("td");
    let inputSec = document.createElement("input");
    inputSec.id = "Sec";
    inputSec.value = 0;
    //td4.appendChild(inputSec);
    let td5 = document.createElement("td");
    let inputDegRead = document.createElement("input");
    inputDegRead.id = "DegRead";
    inputDegRead.disabled = true;
    td5.appendChild(inputDegRead);
    let td6 = document.createElement("td");
    let inputMinRead = document.createElement("input");
    inputMinRead.id = "MinRead";
    inputMinRead.disabled = true;
    td6.appendChild(inputMinRead);
    let td7 = document.createElement("td");
    let inputSecRead = document.createElement("input");
    inputSecRead.id = "SecRead";
    inputSecRead.disabled = true;
    td7.appendChild(inputSecRead);
    let td8 = document.createElement("td");
    let inputDistan = document.createElement("input");
    inputDistan.id = "Distan";
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
    let inputDegReadDir = document.createElement("input");
    inputDegReadDir.id = "DegDirRead" + index;
    inputDegReadDir.disabled = true;
    td5.appendChild(inputDegReadDir);
    let td6 = document.createElement("td");
    let inputMinReadDir = document.createElement("input");
    inputMinReadDir.id = "MinDirRead" + index;
    inputMinReadDir.disabled = true;
    td6.appendChild(inputMinReadDir);
    let td7 = document.createElement("td");
    let inputSecReadDir = document.createElement("input");
    inputSecReadDir.id = "SecDirRead" + index;
    inputSecReadDir.disabled = true;
    td7.appendChild(inputSecReadDir);
    let td8 = document.createElement("td");
    let inputDegRead = document.createElement("input");
    inputDegRead.id = "DegRead" + index;
    inputDegRead.disabled = true;
    td8.appendChild(inputDegRead);
    let td9 = document.createElement("td");
    let inputMinRead = document.createElement("input");
    inputMinRead.id = "MinRead" + index;
    inputMinRead.disabled = true;
    td9.appendChild(inputMinRead);
    let td10 = document.createElement("td");
    let inputSecRead = document.createElement("input");
    inputSecRead.id = "SecRead" + index;
    inputSecRead.disabled = true;
    td10.appendChild(inputSecRead);
    let td11 = document.createElement("td");
    let inputDistan = document.createElement("input");
    inputDistan.id = "Distan" + index;
    inputDistan.value = 0;
    inputDistan.classList.add("distant_input");
    td11.appendChild(inputDistan);

    let td12 = document.createElement("td");
    let inputСoordinateIncrementX = document.createElement("input");
    inputСoordinateIncrementX.id = "inputСoordinateIncrementX" + index;
    inputСoordinateIncrementX.value = 0;
    inputСoordinateIncrementX.disabled = true;
    td12.appendChild(inputСoordinateIncrementX);

    let td13 = document.createElement("td");
    let inputСoordinateIncrementY = document.createElement("input");
    inputСoordinateIncrementY.id = "inputСoordinateIncrementY" + index;
    inputСoordinateIncrementY.value = 0;
    inputСoordinateIncrementY.disabled = true;
    td13.appendChild(inputСoordinateIncrementY);

    let td14 = document.createElement("td");
    let inputСoordinateIncrementCorrectX = document.createElement("input");
    inputСoordinateIncrementCorrectX.id = "inputСoordinateIncrementCorrectX" + index;
    inputСoordinateIncrementCorrectX.value = 0;
    inputСoordinateIncrementCorrectX.disabled = true;
    td14.appendChild(inputСoordinateIncrementCorrectX);

    let td15 = document.createElement("td");
    let inputСoordinateIncrementCorrectY = document.createElement("input");
    inputСoordinateIncrementCorrectY.id = "inputСoordinateIncrementCorrectY" + index;
    inputСoordinateIncrementCorrectY.value = 0;
    inputСoordinateIncrementCorrectY.disabled = true;
    td15.appendChild(inputСoordinateIncrementCorrectY);

    let td16 = document.createElement("td");
    let inputCoordX = document.createElement("input");
    inputCoordX.id = "inputCoordX" + index;
    inputCoordX.value = 0;
    inputCoordX.disabled = true;
    td16.appendChild(inputCoordX);

    let td17 = document.createElement("td");
    let inputCoordY = document.createElement("input");
    inputCoordY.id = "inputCoordY" + index;
    inputCoordY.value = 0;
    inputCoordY.disabled = true;
    td17.appendChild(inputCoordY);


    tr.appendChild(td1);
    tr.appendChild(td2);
    tr.appendChild(td3);
    tr.appendChild(td4);
    tr.appendChild(td8);
    tr.appendChild(td9);
    tr.appendChild(td10);
    tr.appendChild(td5);
    tr.appendChild(td6);
    tr.appendChild(td7);

    tr.appendChild(td11);

    tr.appendChild(td12);
    tr.appendChild(td13);
    tr.appendChild(td14);
    tr.appendChild(td15);
    tr.appendChild(td16);
    tr.appendChild(td17);
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
    let bearingAngle = new BearingAngle();
    let bearing_angle_deg = document.getElementById("bearing_angle_deg");
    let bearing_angle_min = document.getElementById("bearing_angle_min");
    let bearing_angle_sec = document.getElementById("bearing_angle_sec");
    bearingAngle.Deg = bearing_angle_deg.value;
    bearingAngle.Min = bearing_angle_min.value;
    bearingAngle.Sec = bearing_angle_sec.value;
    //aPoints.push(bearingAngle);
    console.log(aPoints);
    console.log(bearingAngle);

    let coords = [];
    let start_x = document.getElementById("start_x");
    let start_y = document.getElementById("start_y");
    let end_x = document.getElementById("end_x");
    let end_y = document.getElementById("end_y");

    let starts = new Coords();
    starts.X = start_x.value;
    starts.Y = start_y.value;
    let ends = new Coords();
    ends.X = end_x.value;
    ends.Y = end_y.value;
    coords.push(starts);
    coords.push(ends);
    console.log(coords);

    let sSide=document.getElementById("switcher_side_of_angles");
    let side_of_angles=sSide.checked ? "right" : "left";
    console.log(side_of_angles);

    let sDirection=document.getElementById("switcher_direction_of_circling");
    let direction_of_circling=sDirection.checked ? "right" : "left"
    console.log(direction_of_circling);

    let loader = document.getElementById("loader");
    loader.style.display = "flex";

    let otherValues = document.getElementById("other_values");

    fetch('http://127.0.0.1:8000/GetResult', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', 'accept': '*/*' },
        body: JSON.stringify({
            aPoints,
            bearingAngle,
            coords,
            side_of_angles,
            direction_of_circling
        })

    })
        .then(res => res.json())
        .then(item => {
            console.log(item)
            if (item) {
                if (item.angles && item.angles.length > 0) {
                    FillMainData(item.angles);
                }
                if (item.bearing_angles && item.bearing_angles.length > 0) {
                    FillBearingAngles(item.bearing_angles);
                }
                if (item.coordinate_increments && item.coordinate_increments.length > 0) {
                    FillCoordinates("coordinate_increments", item.coordinate_increments);
                }
                if (item.coordinate_increment_correct && item.coordinate_increment_correct.length > 0) {
                    FillCoordinates("coordinate_increment_correct", item.coordinate_increment_correct);
                }
                if (item.all_coords && item.all_coords.length > 0) {
                    FillCoordinates("all_coords", item.all_coords);
                }
                if (item.difference) {
                    FillOtherData("difference", item.difference);
                }
                if (item.permissible_difference) {
                    FillOtherData("permissible_difference", item.permissible_difference);
                }
                if (item.sum_correct_angles) {
                    FillOtherData("sum_correct_angles", item.sum_correct_angles);
                }
                if (item.sum_measured_angles) {
                    FillOtherData("sum_measured_angles", item.sum_measured_angles);
                }
                if (item.theoretical_sum_of_angles) {
                    FillOtherData("theoretical_sum_of_angles", item.theoretical_sum_of_angles);
                }
                if (item.perimetr) {
                    let Perimetr = document.getElementById("perimetr");
                    Perimetr.value = item.perimetr;
                }
            }
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


function FillMainData(angles) {
    if (angles && angles.length > 0) {
        for (let i = 1; i < angles.length + 1; i++) {
            let Deg = document.getElementById("DegRead" + i);
            let Min = document.getElementById("MinRead" + i);
            let Sec = document.getElementById("SecRead" + i);
            Deg.value = angles[i - 1].CorDeg;
            Min.value = angles[i - 1].CorMin;
            Sec.value = angles[i - 1].CorSec;
        }
    }
}

function FillBearingAngles(bAngles) {
    if (bAngles && bAngles.length > 0) {
        for (let i = 1; i < bAngles.length + 1; i++) {
            let Deg = document.getElementById("DegDirRead" + i);
            let Min = document.getElementById("MinDirRead" + i);
            let Sec = document.getElementById("SecDirRead" + i);
            Deg.value = bAngles[i - 1].Deg;
            Min.value = bAngles[i - 1].Min;
            Sec.value = bAngles[i - 1].Sec;
        }
    }
}

function FillOtherData(key, item) {
    let Deg = document.getElementById(key + "_deg");
    let Min = document.getElementById(key + "_min");
    let Sec = document.getElementById(key + "_sec");
    Deg.value = item.Deg;
    Min.value = item.Min;
    Sec.value = item.Sec;
}

function FillCoordinates(type, coords) {
    if (type == "coordinate_increments") {
        if (coords && coords.length > 0) {
            for (let i = 1; i < coords.length + 1; i++) {
                let X = document.getElementById("inputСoordinateIncrementX" + i);
                let Y = document.getElementById("inputСoordinateIncrementY" + i);
                X.value = coords[i - 1].incX;
                Y.value = coords[i - 1].incY;
            }
        }
    }
    if(type=="coordinate_increment_correct"){
        if (coords && coords.length > 0) {
            for (let i = 1; i < coords.length + 1; i++) {
                let X = document.getElementById("inputСoordinateIncrementCorrectX" + i);
                let Y = document.getElementById("inputСoordinateIncrementCorrectY" + i);
                X.value = coords[i - 1].incXcor;
                Y.value = coords[i - 1].incYcor;
            }
        }
    }
    if(type=="all_coords"){
        if (coords && coords.length > 0) {
            for (let i = 1; i < coords.length + 1; i++) {
                let X = document.getElementById("inputCoordX" + i);
                let Y = document.getElementById("inputCoordY" + i);
                X.value = coords[i - 1].X;
                Y.value = coords[i - 1].Y;
            }
        }
    }
}



function TestData() {
    let select_test_data = document.getElementById("select_test_data");
    fetch('http://127.0.0.1:8000/TestData/' + select_test_data.value)
        .then(res => res.json())
        .then(item => {
            let otherValues = document.getElementById("other_values");
            otherValues.style.display = "none";
            ClearData();
            if (item && item.length > 0) {
                let tbody = document.getElementById("tbody_container");
                tbody.innerHTML = "";
                let header_container = document.getElementById("header_container");
                header_container.style.display = "none";
                for (let i = 0; i < item.length; i++) {
                    header_container.style.display = "table";
                    AddRow();
                }
                FillTestDataPoints(item);
                console.log(item);
            }
            if (item && !item.length) {
                let tbody = document.getElementById("tbody_container");
                tbody.innerHTML = "";
                let header_container = document.getElementById("header_container");
                header_container.style.display = "none";
                if (item.aPoints.length) {
                    for (let i = 0; i < item.aPoints.length; i++) {
                        header_container.style.display = "table";
                        AddRow();
                    }
                    FillTestDataPoints(item.aPoints);
                    console.log(item.aPoints);
                }
                if (item.bearingAngle) {
                    FillTestDataBearingAngle(item.bearingAngle);
                    console.log(item.bearingAngle);
                }
                if (item.coords) {
                    FillTestDataCoords(item.coords);
                    console.log(item.coords);
                }
            }
            if (item == false) {
                let tbody = document.getElementById("tbody_container");
                tbody.innerHTML = "";
                let header_container = document.getElementById("header_container");
                header_container.style.display = "none";
            }
        }
        ).catch((ex) => {
            console.log(ex.message)
        });
}

function FillTestDataPoints(items) {
    if (items && items.length > 0) {
        for (let i = 1; i < items.length + 1; i++) {
            let Deg = document.getElementById("Deg" + i);
            let Min = document.getElementById("Min" + i);
            let Sec = document.getElementById("Sec" + i);
            let Distan = document.getElementById("Distan" + i);
            Deg.value = items[i - 1].Deg;
            Min.value = items[i - 1].Min;
            Sec.value = items[i - 1].Sec;
            Distan.value = items[i - 1].HorDist;
        }
    }
}
function FillTestDataBearingAngle(item) {
    if (item) {
        let Deg = document.getElementById("bearing_angle_deg");
        let Min = document.getElementById("bearing_angle_min");
        let Sec = document.getElementById("bearing_angle_sec");
        Deg.value = item.Deg;
        Min.value = item.Min;
        Sec.value = item.Sec;
    }
}
function FillTestDataCoords(item) {
    if (item) {
        let start_x = document.getElementById("start_x");
        let start_y = document.getElementById("start_y");
        let end_x = document.getElementById("end_x");
        let end_y = document.getElementById("end_y");
        start_x.value = item[0].X;
        start_y.value = item[0].Y;
        end_x.value = item[1].X;
        end_y.value = item[1].Y;
    }
}
function ClearData() {
    document.getElementById("bearing_angle_deg").value = 0;
    document.getElementById("bearing_angle_min").value = 0;
    document.getElementById("bearing_angle_sec").value = 0;
    document.getElementById("start_x").value = 0;
    document.getElementById("start_y").value = 0;
    document.getElementById("end_x").value = 0;
    document.getElementById("end_y").value = 0;
    document.getElementById("perimetr").value = 0;
}

/*переключатель*/
function ToggleSwitcher(val, sLabel) {
    let label = document.getElementById(sLabel);
    if (val) {
        console.log("right");
        label.innerHTML = "right";
    }
    else {
        console.log("left");
        label.innerHTML = "left";
    }

}