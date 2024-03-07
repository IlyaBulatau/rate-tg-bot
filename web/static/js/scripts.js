function addDynamicFields() {
  var dynamicFieldsContainer = document.getElementById('dynamicFields');

  // Создаем поле выбора страны
  var countrySelect = document.createElement('select');
  countrySelect.name = 'country';
  countrySelect.required = true;

  var countries = ['Выберите страну', 'Россия', 'США', 'Германия']; // Ваши варианты стран
  for (var i = 0; i < countries.length; i++) {
    var option = document.createElement('option');
    option.value = countries[i];
    option.text = countries[i];
    countrySelect.appendChild(option);
  }

  // Создаем поле выбора возрастной группы
  var ageGroupSelect = document.createElement('select');
  ageGroupSelect.name = 'ageGroup';
  ageGroupSelect.required = true;

  var ageGroups = ['Выберите возрастную группу', 'До 18 лет', '18-25 лет', '25-35 лет']; // Ваши варианты возрастных групп
  for (var j = 0; j < ageGroups.length; j++) {
    var option = document.createElement('option');
    option.value = ageGroups[j];
    option.text = ageGroups[j];
    ageGroupSelect.appendChild(option);
  }

  // Добавляем созданные поля к контейнеру
  dynamicFieldsContainer.innerHTML = ''; // Очищаем контейнер перед добавлением новых полей
  dynamicFieldsContainer.appendChild(countrySelect);
  dynamicFieldsContainer.appendChild(ageGroupSelect);
}