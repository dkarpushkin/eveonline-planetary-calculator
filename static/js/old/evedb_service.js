(function () {
    EveDbService = {
        typesOfGroup: function (groupId, successCallback, errorCallback) {
            groupId = parseInt(groupId);

            $.ajax('/evedb/pschematics?outgroupid=' + groupId, {
                type: 'GET',
                dataType: 'json',
                success: successCallback,
                error: errorCallback
            });
        },
        pschematicsInfo: function (schemaId, success, error) {
            schemaId = parseInt(schemaId);

            $.ajax('/evedb/pschematics/' + schemaId, {
                type: 'GET',
                dataType: 'json',
                success: success,
                error: error
            });
        }
    };
})();
