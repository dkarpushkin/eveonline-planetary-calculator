

(function() {
    'use strict';

    angular.module('pi_calc', [
        'evedb.services',
        'eve_central.services',
        'pi_calc.config',
        'pi_calc.controllers',
        'pi_calc.directives'
    ]);

    angular.module('pi_calc').run();
})();
