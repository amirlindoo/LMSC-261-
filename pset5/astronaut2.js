
function checkLifeSpan(hoursUsed) {
    const maxLifeSpan = 1000;

    if (typeof hoursUsed !== "number" || !Number.isFinite(hoursUsed) || hoursUsed < 0) {
        return "please enter valid number";
    }

    if (hoursUsed < 800) {
        return "suit in working condition";
    } else if (hoursUsed < maxLifeSpan) {
        return "suit needs replacement soon";
    } else {
        return "suit no longer safe to use";
    }
}

print(checkLifeSpan(500));
print(checkLifeSpan(850));
print(checkLifeSpan(1000));
print(checkLifeSpan("hello"));
