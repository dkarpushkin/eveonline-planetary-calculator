function PiSchema(schemaData) {
    this.schematicID = parseInt(schemaData['schematicID']);
    this.cycleTime = parseFloat(schemaData['cycleTime']);
    this.schematicName = schemaData['schematicName'];
    this.prodLinesNumber = 1;

    var inputTypes = schemaData['inputTypes'];
    if (Array.isArray(inputTypes)) {
        this.inputTypes = [];
        for (var i = 0; i < inputTypes.length; ++i) {
            var typeMap = new TypeMap(inputTypes[i])
            this.inputTypes.push(typeMap);
            typeMap.type.isForSell = false;
        }
    }

    if (typeof schemaData['outputType'] == 'object') {
        this.outputType = new TypeMap(schemaData['outputType']);
        this.outputType.type.isForSell = true;
    }
}

PiSchema.prototype.getTotalInputCost = function (tax) {
    var accPrice = 0;
    for (var i = 0; i < this.inputTypes.length; ++i) {
        accPrice += this.inputTypes[i].getTotalPrice(tax);
    }
    return accPrice;
};

PiSchema.prototype.getOneRunProfit = function (poco_tax) {
    poco_tax = typeof poco_tax == 'number' ? poco_tax / 100 : 0;
    return (this.outputType.getTotalPrice(-poco_tax) - this.getTotalInputCost(poco_tax));
};

PiSchema.prototype.getHourlyProfit = function (poco_tax) {
    var prodLinesNumber = parseInt(this.prodLinesNumber);
    if (prodLinesNumber === Number.NaN)
        return 0;

    var hoursForCycle = this.cycleTime / 3600;    //  3600 - количество секунд в часе
    var unitProfit = this.getOneRunProfit(poco_tax);
    return (hoursForCycle * unitProfit * this.prodLinesNumber);
};

/*

 */
PiSchema.prototype.setOrderType = function (isForBuyables, orderType) {
    this.outputType.setOrderType(isForBuyables, orderType);

    for (var i = 0; i < this.inputTypes.length; ++i) {
        this.inputTypes[i].setOrderType(isForBuyables, orderType);
    }
};

