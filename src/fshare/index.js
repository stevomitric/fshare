function populate_data(data) {
    for (let i = 0; i < data['data'].length; ++i) {
        let item = data['data'][i];
        let table = document.getElementById('main_table');

        let row = table.insertRow();
        let cell1 = row.insertCell();
        cell1.innerHTML = "<a class='link-dark' href='./file/"+item[0]+"'>"+item[0]+"</a>";
        let cell2 = row.insertCell();
        cell2.innerHTML = item[1];
        let cell3 = row.insertCell();
        cell3.innerHTML = item[2];
        let cell4 = row.insertCell();
        cell4.innerHTML = item[3];
        let cell5 = row.insertCell();
        cell5.innerHTML = "<a href='./delete/"+item[0]+"' class='link-dark link-underline-light'>x</a>";
    }
}