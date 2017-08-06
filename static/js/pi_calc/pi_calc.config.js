(function () {
    'use strict';

    angular.module('pi_calc.config', [])
        .config(config);

    config.$inject = ['$interpolateProvider'];

    function config($interpolateProvider) {
        $interpolateProvider.startSymbol('{[{');
        $interpolateProvider.endSymbol('}]}');
    };
})();
