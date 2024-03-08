function validateAndProceed(country, ageGroup, participantType) {
  if (country !== "") {
      showNextField();
  } else {
      alert("Пожалуйста, выберите страну.");
  }
}

function validateAndSubmit(country, ageGroup, participantType) {
  if (ageGroup !== "") {
      showParticipantType();
  } else {
      alert("Пожалуйста, выберите возрастную группу.");
  }
}

function showNextField() {
  document.getElementById("country").style.display = "none";
  document.getElementById("countryLabel").style.display = "none";
  document.getElementById("ageGroup").style.display = "block";
  document.getElementById("ageGroupLabel").style.display = "block";
}

function showParticipantType() {
  document.getElementById("participantType").style.display = "block";
  document.getElementById("participantTypeLabel").style.display = "block";
  document.getElementById("confirmButton").onclick = function() {
      validateAndSubmit(countrySelect.value, ageGroupSelect.value, participantTypeSelect.value);
  };
  document.getElementById("sendData").style.display = "block";
  document.getElementById("confirmButton").style.display = "none";
}