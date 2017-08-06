(function () {
    'use strict';

    angular.module('pi_calc.controllers', [])
        .controller('PlanetaryCalculator', PlanetaryCalculator);

    PlanetaryCalculator.$inject = ['$scope', 'EveDbService', 'EveCentralService'];

    function PlanetaryCalculator($scope, EveDbService, EveCentralService) {
        $scope.schemas = [];

        $scope.schemaId = 'undefined';
        $scope.tradeHubId = '30000142';     //  Jita default
        $scope.buyingOrderType = 'false';   //  тип ордера для покупки, true - бай ордер
        $scope.sellingOrderType = 'true';   //  тип ордера для продажи, false - селл ордер

        $scope.poco_tax = 5;

        $scope.addSchema = function (callback) {
            if ($scope.schemaId != 'undefined')
                EveDbService.schemaInfo({ 'schemaId': $scope.schemaId },
                    function (response) {
                        if (typeof callback === 'undefined')
                            _addSchema(response.data);
                        else
                            callback(response.data);
                    }, function (response) {
                        console.error('Fetching schematic info failed.');
                        console.error(response);
                    });
        };

        $scope.fetchSubScheme = function (typeMap) {
            if (typeof typeMap.type.schema === 'undefined') {
                EveDbService.schemaInfo({
                        'ouTypeId': typeMap['type']['typeID']
                    }, function (response) {
                        if (Array.isArray(response.data) && response.data.length > 0) {
                            typeMap.type.schema = new PiSchema(response.data[0]);
                        } else if (typeof response != 'undefined' && typeof response.data == 'object') {
                            typeMap.type.schema = new PiSchema(response.data);
                        }

                        if (typeof typeMap.type.schema != 'undefined')
                            _loadPrices(typeMap.type.schema)
                    });
            }
        };

        $scope.removeSchema = function (schema) {
            for (var i = 0; i < $scope.schemas.length; ++i) {
                if (schema == $scope.schemas[i]) {
                    $scope.schemas.splice(i, 1);
                    break;
                }
            }
        };

        $scope.reloadAllPrices = function () {
            for (var i = 0; i < $scope.schemas.length; ++i) {
                _loadPrices($scope.schemas[i]);
            }
        };

        $scope.getQuantity = function(typeMap, schema) {
            var runsNeeded = schema.outputType.quantity
        };

        $scope.getTotalVolume = function (typeMap) {
            return typeMap.type.volume * typeMap.quantity;
        };

        $scope.getTotalInputCost = function (schema) {
            if (typeof schema == 'undefined')
                return '';

            return schema.getTotalInputCost().toFixed(2);
        };

        $scope.getTotalCost = function (typeMap) {
            return typeMap.getTotalPrice().toFixed(2);
        };

        $scope.getOneRunProfit = function (schema) {
            return schema.getOneRunProfit(parseFloat($scope.poco_tax)).toFixed(2);
        };

        $scope.getHourlyProfit = function (schema) {
            return schema.getHourlyProfit(parseFloat($scope.poco_tax)).toFixed(2);
        };

        $scope.getDaylyProfit = function (schema) {
            return (24 * schema.getHourlyProfit(parseFloat($scope.poco_tax))).toFixed(2);
        };

        $scope.getHoursToComplete = function (schema) {
            var hoursForCycle = parseFloat(schema['cycleTime']) / 3600;    //  3600 - количество секунд в часе
            var runs = Math.ceil(parseFloat(schema['numberOfRuns']) / parseFloat(schema['prodLinesNumber']));
            return (runs * hoursForCycle).toFixed(2);
        };

        //  Продавать ли по бай ордерам
        $scope.isSellingByBuy = function () {
            return $scope.sellingOrderType === "true";
        };

        //  Покупать ли по бай ордерам
        $scope.isBuyingByBuy = function () {
            return $scope.buyingOrderType === "true";
        };

        $scope.parseInt = parseInt;
        $scope.parseFloat = parseFloat;

        $scope.$watch('buyingOrderType', _updateOrderTypesFn(true));
        $scope.$watch('sellingOrderType', _updateOrderTypesFn(false));


        function _addSchema(schemaData) {
            var schema = new PiSchema(schemaData);
            $scope.schemas.push(schema);
            _loadPrices(schema);
        }

        /*
         Загружает цены для всех типов в схеме
         */
        function _loadPrices(schema) {
            var systemId = $scope.tradeHubId;
            _requestPricing(schema.outputType, systemId);

            for (var i = 0; i < schema.inputTypes.length; ++i) {
                _requestPricing(schema.inputTypes[i], systemId);
            }
        }

        function _requestPricing(typeMap, systemId) {
            var type = typeMap.type;
            EveCentralService.marketStat(type.typeID, systemId,
                function (result) {
                    if (Array.isArray(result))
                        type.setPricing(result[0], $scope.isBuyingByBuy(), $scope.isSellingByBuy());
                    else
                        type.setPricing(result, $scope.isBuyingByBuy(), $scope.isSellingByBuy());
                });
        }

        function _updateOrderTypesFn(isForBuyables) {
            /*
                orderType - строка c boolean
             */
            return function (orderType) {
                if (typeof orderType == 'undefined')
                    return;
                orderType = orderType === 'true';
                //  Обновляем pricing.current для каждого предмета\
                for (var i = 0; i < $scope.schemas.length; ++i) {
                    $scope.schemas[i].setOrderType(isForBuyables, orderType);
                }
            }
        }

        function _evalPricings(schema, tax) {
            if (typeof schema.outputCost == 'undefined')
                schema.outputCost = {
                    buy: _evalTotalPrice(schema['outputTypes'][0], tax),
                    sell: _evalTotalPrice(schema['outputTypes'][0], tax)
                };

            //if (typeof schema.inputCost == 'undefined')
            schema.inputCost = {
                buy: _evalInputPrice(schema, true),
                sell: _evalInputPrice(schema, false)
            };
        }

        function _evalInputPrice(schema, tax) {
            var accPrice = 0;
            for (var i = 0; i < schema['inputTypes']['length']; ++i) {
                accPrice += _evalTotalPrice(schema['inputTypes'][i], tax);
            }
            return accPrice;
        }

        function _evalTotalPrice(typeMap, tax) {
            if (typeof typeMap.type.pricing == 'undefined')
                return 0;

            if (typeof tax !== 'number')
                tax = 0;
            else
                tax = tax / 100;

            return (typeMap.type.pricing.curr + groupBasePrices[typeMap['type']['group']] * tax) * typeMap.quantity;
        }

        //  соответствие груп налогам
        var groupBasePrices = {
            1032: 4,
            1033: 4,
            1035: 4,
            1042: 400,
            1034: 7200,
            1040: 60000,
            1041: 1200000
        };
    }
})();
