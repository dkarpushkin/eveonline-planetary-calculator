

(function() {

    var piCalcApp = angular.module('pi_calculator', []);

    piCalcApp.config(function($interpolateProvider) {
      $interpolateProvider.startSymbol('{[{');
      $interpolateProvider.endSymbol('}]}');
    });

    piCalcApp.controller('SchemasList', ['$scope', '$http',
        function SchemasList($scope, $http) {
            $http.get('evedb/group/1332').success(function(data) {
                $scope.groups = data.childGroups;
            });

            $scope.schemas = [];
            $scope.table = [];


            //  Event handlers
            $scope.groupChanged = function() {
                $http.get('evedb/types/' + $scope.groupId).success(function(data) {
                    $scope.schemas = data;
                });
            };

            $scope.schemaChanged = function() {

            };

            //$scope.addTypeFromGroup = function() {
            //    $scope.table = $scope.types.concat($scope.schemas);
            //};

            $scope.addToTable = function () {
                $scope.table.push($scope.schemas[$scope.typeId])
            };


            //  helpers
            $scope.parseInt = parseInt;
            $scope.parseFloat = parseFloat;
    }]);

})();
