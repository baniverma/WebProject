document.getElementById('macronutrientForm').addEventListener('submit', function(event) {
  event.preventDefault(); // Prevent form submission

  // Get user input values
  const age = parseInt(document.getElementById('age').value);
  const weight = parseFloat(document.getElementById('weight').value);
  const height = parseFloat(document.getElementById('height').value);
  const gender = document.getElementById('gender').value;
  const activity = parseFloat(document.getElementById('activity').value);

  // Calculate BMR using Mifflin-St Jeor Equation
  let bmr;
  if (gender === 'male') {
      bmr = 10 * weight + 6.25 * height - 5 * age + 5; // BMR for men
  } else {
      bmr = 10 * weight + 6.25 * height - 5 * age - 161; // BMR for women
  }

  // Calculate TDEE (Total Daily Energy Expenditure)
  const tdee = bmr * activity;

  // Calculate macronutrient breakdown (using AMDR percentages)
  const carbsCalories = tdee * 0.50; // 50% carbs
  const proteinCalories = tdee * 0.20; // 20% protein
  const fatCalories = tdee * 0.30; // 30% fats

  // Convert calories to grams (1g of carbs = 4 calories, 1g of protein = 4 calories, 1g of fat = 9 calories)
  const carbsGrams = carbsCalories / 4;
  const proteinGrams = proteinCalories / 4;
  const fatGrams = fatCalories / 9;

  // Display the results
  document.getElementById('caloriesResult').innerText = `Total Daily Calories: ${Math.round(tdee)} kcal`;
  document.getElementById('carbResult').innerText = `Carbohydrates: ${Math.round(carbsGrams)} grams`;
  document.getElementById('proteinResult').innerText = `Proteins: ${Math.round(proteinGrams)} grams`;
  document.getElementById('fatResult').innerText = `Fats: ${Math.round(fatGrams)} grams`;

  // Show the results
  document.getElementById('results').style.display = 'block';
});
