

function calculateCalories() {
    // Get selected values from the dropdown menus
    var breakfastCalories = parseInt(document.getElementById('breakfast').value);
    var lunchCalories = parseInt(document.getElementById('lunch').value);
    var dinnerCalories = parseInt(document.getElementById('dinner').value);

    // Calculate the total calories
    var totalCalories = breakfastCalories + lunchCalories + dinnerCalories;

    // Display the total calories
    document.getElementById('totalCalories').innerText = totalCalories + ' kcal';
}
