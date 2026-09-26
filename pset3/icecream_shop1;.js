const priceofIceCream = 5;
let paymentReceived = prompt ("How much money are you paying?");
let isPaymentEnough = paymentReceived >= priceofIceCream;
if (isPaymentEnough) {
    print("Thanks! Enjoy the Ice Cream!");
} else {
    print("Not enough cash!");
}