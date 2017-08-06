function TypeMap(data) {
    this.quantity = parseInt(data['quantity']);
    this.type = new Type(data['type']);
}

TypeMap.prototype.setSellable = function() {
    this.type.setBuyable(false);
};

TypeMap.prototype.setBuyable = function () {
    this.type.setBuyable(true);
};

TypeMap.prototype.getTotalPrice = function (tax) {
    var isBuy = (typeof this.type.isBuyable == 'undefined') ? true : isBuy;
    tax = (typeof tax == 'number') ? tax / 100 : 0;

    if (typeof this.type.pricing == 'undefined')
        return 0;

    //var oneItemPrice = isBuy ? this.type.pricing.buy : this.type.pricing.sell;

    return this.quantity * (this.type.pricing.current
        + this.type.getBasePrice() * tax);
};

TypeMap.prototype.setOrderType = function (isForBuyables, orderType) {
    if (isForBuyables == !this.type.isForSell)
        this.type.pricing.current =
            orderType ? this.type.pricing.buy :
                this.type.pricing.sell;
};
