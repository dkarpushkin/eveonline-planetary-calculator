
(function() {
    'use strict';

    angular.module('evedb.services', ['ngCookies'])
        .factory('EveDbService', EveDbService);

    EveDbService.$inject = ['$cookies', '$http'];

    function EveDbService($cookies, $http) {
        var EveDbService = {
            schemaInfo: function(kwargs, successFn, errorFn) {
                var url = 'evedb/pschematics';

                if (kwargs.hasOwnProperty('schemaId'))
                    url += '/' + kwargs['schemaId'];
                else if (kwargs.hasOwnProperty('ouTypeId'))
                    url += '?outtype=' + kwargs['ouTypeId'];

                return $http.get(url)
                    .then(successFn, errorFn)
            }
        };

        return EveDbService;
    }
})();
