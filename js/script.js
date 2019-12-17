$.makeTable = function(data) {
    // DECLARE ARRAY
    let isRendered = false;
    var renderHtml = "";



    $.each(data, function(i, tabledata) {
        // WRITE HTML TO RENDER

        // !TODO ADD CLASS NAME FOR OPEN AND CLOSED Applications
        console.log(data[i].organization);
        var parsedDate;
        try {
            parsedDate = moment(data[i].date).toLongDateString();
        } catch(err) {

        }
        if(parsedDate == null) { parsedDate = (data[i].date); }

        if(data[i].date.indexOf("closed") == -1) {
            renderHtml += "<tr class=\"newrow\"><td>" + data[i].org + "</td><td>" + data[i].program + "</td><td> <a href=\"" + data[i].link + "\" target=\"_blank\"> More Info </a></td><td class=\"table-success\">" + parsedDate + "</td><td></tr>";
        } else {
            renderHtml += "<tr class=\"newrow\"><td>" + data[i].org + "</td><td>" + data[i].program + "</td><td> <a href=\"" + data[i].link + "\" target=\"_blank\"> More Info </a></td><td class=\"table-danger\">" + parsedDate + "</td><td></tr>";
        }

        // POPULATE TABLE WITH JSON DATA

    });
    $("tbody").after(renderHtml);

    isRendered = true;
};

$(document).ready(function() {
    // GET JSON DATA
    $.ajax({
        type: 'GET',
        url: 'data.json',
        dataType: 'json',
        success: function(data) {

            // CALL FUNCTION
            $.makeTable(data);
        }
    });




});