$(function () {
    var addButton = $('#add-button');
    var schemasSelect = $('#schemasSelect');
    var typesTable =

    setCallbacks();

    function setCallbacks() {

        addButton.click(function () {
            EveDbService.pschematicsInfo(schemasSelect.value,
                function (data, status, jqXHR) {
                    if (typeof data === 'object')
                        addSchema(data);
                }, function (jqXHR, status) {
                    alert(status)
                })
        });
    }

    function addSchema(type) {

    }
});

