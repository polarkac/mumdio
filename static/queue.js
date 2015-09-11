function get_queue_data() {
    $.ajax({ url: '/queue/' })
        .done(function (data) {
            $("#qt tr").remove();
            var table = document.getElementById("qt");
            var q = data.queue;
            
            for(var i = 0; i < q.length; i++) {
                console.log("VAR I = " + i);
                var t = table.insertRow(0).insertCell(0);
                $(t).html("<a href=\"" + q[i] + "\">" + q[i] + "</a>");
            }            
        })
}

$("body").load(get_queue_data());
setInterval(get_queue_data, 10000);