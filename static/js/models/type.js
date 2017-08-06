function Type(data) {
    this.typeID = parseInt(data['typeID']);
    this.typeName = data['typeName'];
    this.volume = parseFloat(data['volume']);
    this.group = parseInt(data['group']);

    this.iconid = parseInt(data['iconid']);
}

Type.prototype.setBuyable = function (isBuyable) {
    if (typeof isBuyable == 'undefined') {
        console.error('isBuyable is not specified in Type.setBuyable');
        return;
    }

    this.isForSell = !isBuyable;
};

/*
 buy - for buy orders
 sell - for sell orders
 current - current choosen price or user defined
 */
Type.prototype.setPricing = function (pricingData, buyingOrder, sellingOrder) {
    var buy = parseFloat(pricingData['buy']['max']),
        sell = parseFloat(pricingData['sell']['min']);

    this.pricing = {
        buy: buy,
        sell: sell
    };

    if (this.isForSell)
        this.pricing.current = sellingOrder ? this.pricing.buy : this.pricing.sell;
    else
        this.pricing.current = buyingOrder ? this.pricing.buy : this.pricing.sell;
};

Type.prototype.setOrderType = function (isForBuyables, orderType) {
    if (isForBuyables == !this.isForSell)
        this.pricing.current =
            orderType ? this.pricing.buy :
                this.type.pricing.sell;
};

Type.prototype.getBasePrice = function () {
    return Type.prototype.groupBasePrices[this.group];
};

//  соответствие груп налогам
Type.prototype.groupBasePrices = {
    1032: 4,
    1033: 4,
    1035: 4,
    1042: 400,
    1034: 7200,
    1040: 60000,
    1041: 1200000
};