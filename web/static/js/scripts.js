function showNextField() {
  // Скрываем поле выбора страны и кнопку
  document.getElementById("country").style.display = "none";
  document.getElementById("countryLabel").style.display = "none";
  document.getElementById("ageGroup").style.display = "block";
  document.getElementById("ageGroupLabel").style.display = "block";
  // Показываем кнопку "Отправить"
  document.getElementById("sendData").style.display = "block";
}
