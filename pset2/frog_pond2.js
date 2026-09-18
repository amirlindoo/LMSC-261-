const activities = ["babysit tadpoles", "flies for lunch", "tongue stretch", "swimming lesson"];
let activityIndex = prompt ("2");
let wrappedIndex = activityIndex % activities.length;

print(activities[wrappedIndex]);