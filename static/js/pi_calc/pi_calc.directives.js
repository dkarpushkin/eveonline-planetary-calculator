(function () {
    'use strict';

    angular.module('pi_calc.directives', [])
        .directive('tableTreeNode', TableTreeNode);

    function TableTreeNode($compile) {
        return {
            restrict: 'A',
            scope: {
                inputTypeMap: "=typeMap"
            },
            templateUrl: '/templates/tabletreenode.html',
            controller: 'PlanetaryCalculator',

            link: function (scope, element, attrs, controller, transcludeFn) {
                scope.$watch('inputTypeMap.type.schema.inputTypes.length', setChildNodesFn(scope, element), true);
                scope.$watch('inputTypeMap.isForSell', toggleExpandenceFn(element), true)
            }
        };

        function setChildNodesFn(scope, element) {
            return function (schemaData) {
                if (typeof schemaData == 'undefined') return;

                var newRow = createRow(parseInt(element.attr('level')) + 1);
                newRow.insertAfter(element);
                $compile(newRow)(scope);
            }
        }

        function toggleExpandenceFn(element) {
            return function (isExpanded) {
                if (typeof isExpanded == 'undefined')
                    return;

                var currentLevel = parseInt(element.attr('level'));
                if (!isExpanded) {
                    var allChildren = element.nextUntil('tr[level=' + currentLevel + ']');

                    //  удаляем строки высших уровней
                    for (var i = currentLevel; i > 0; --i)
                        allChildren = allChildren.not('tr[level=' + i + ']');

                    allChildren.addClass('closed');
                    allChildren.removeClass('opened');

                    element.addClass('collapsed');
                } else {
                    var nextLevel = currentLevel + 1;
                    var nlChildren = element.nextAll('tr[level=' + nextLevel + ']');

                    nlChildren.addClass('opened');
                    nlChildren.removeClass('closed');

                    nlChildren.each(function (index, child) {
                        child = $(child);
                        if (!child.hasClass('collapsed'))
                            toggleExpandenceFn(child)(true);
                    });

                    element.removeClass('collapsed');
                }
            }
        }

        function createRow(level) {
            var row =
                '<tr ng-repeat="inputTypeMap in inputTypeMap[\'type\'][\'schema\'][\'inputTypes\']"' +
                'type-map="inputTypeMap"' +
                'level="' + level + '" table-tree-node>' +
                '</tr>';

            return angular.element(row);
        }

    }
})();
