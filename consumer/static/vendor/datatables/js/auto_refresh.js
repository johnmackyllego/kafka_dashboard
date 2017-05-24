//$(function(){
    //$("#logfile").dataTable({
        //"lengthChange": false,
        //"order": [[ 3, "desc" ]],
        //"bStateSave": true
    //});
//})
var table = $('#logfile').DataTable(
    {
        "lengthChange": false,
        "order": [[ 3, "desc" ]],
        "bStateSave": true
    }
            
);
table.ajax.reload();
