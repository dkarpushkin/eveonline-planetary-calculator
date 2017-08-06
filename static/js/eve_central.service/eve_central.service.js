(function () {
    'use strict';

    angular.module('eve_central.services', ['ngCookies'])
        .factory('EveCentralService', EveCentralService);

    EveCentralService.$inject = ['$cookies', '$http'];

    function EveCentralService($cookies, $http) {
        var EveCentralService = {
            quickLookEP: 'http://api.eve-central.com/api/quicklook?typeid=',
            marketStatEP: 'http://api.eve-central.com/api/marketstat/json?typeid=',

            quicklook: function (typeId, systemId, successFn, errorFn) {
                if (typeof typeId !== 'number' && typeof typeId !== 'string') {
                    console.log('typeId is required for EveCentralService.quicklook');
                    return false;
                }

                var url = this.quickLookEP + typeId;
                if (typeof systemId == 'number' || typeof systemId == 'string')
                    url += '&usesystem=' + systemId;
                else
                    console.warn('systemId is neither nubmer nor string');

                $http.get(url, {transformResponse: xml2json})
                    .success(successFn)
                    .error(function (response) {
                        console.log('EveCentralService.quicklook failed');
                        console.log(response.status);
                        if (typeof errorFn != 'undefined')
                            errorFn(response);
                    });
            },

            marketStat: function (typeId, systemId, successFn, errorFn) {
                if (typeof typeId !== 'number' && typeof typeId !== 'string') {
                    console.log('typeId is required for EveCentralService.marketStat');
                    return false;
                }

                var url = this.marketStatEP + typeId;
                if (typeof systemId == 'number' || typeof systemId == 'string')
                    url += '&usesystem=' + systemId;
                else
                    console.warn('systemId is not nubmer or string');

                $http.get(url)
                    .success(successFn)
                    .error(function (response) {
                        console.log('EveCentralService.marketStat request failed');
                        console.log(response.status);
                        if (typeof errorFn != 'undefined')
                            errorFn(response)
                    });
            },

            getPricing: function (typeId, systemId, successFn, errorFn) {

            }
        };

        function xml2json(xml) {
            var x2js = new X2JS();
            var json = x2js.xml_str2json(xml);
            return json.evec_api;
        }

        return EveCentralService;
    }
})();
