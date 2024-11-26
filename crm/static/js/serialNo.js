window.onload = function() {
    var table = document.getElementById("myTable");
    var rows = table.getElementsByTagName("tr");

    for (var i = 1; i < rows.length; i++) {
        var cells = rows[i].cells;
        cells[0].textContent = i ;
    }

    var table = document.getElementById("myTable1");
    var rows = table.getElementsByTagName("tr");

    for (var i = 1; i < rows.length; i++) {
        var cells = rows[i].cells;
        cells[0].textContent = i ;
    }
};
