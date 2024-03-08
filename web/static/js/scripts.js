let rForm = document.getElementById("registrationForm");
let countrySelect = document.getElementById("country");
let ageGroupSelect = document.getElementById("ageGroup");
let participantTypeSelect = document.getElementById("participantType");
const rootURL = window.location.origin;

document.getElementById("confirmCountry").addEventListener("click", function() {
  // кнопка выбор страны
    if (countrySelect.value !== "") {
        showNextButton("confirmCountry", "confirmAgeGroup");
        showNextLabel("countryLabel", "ageGroupLabel");
        showNextSelect("country", "ageGroup");
        let country = countrySelect.value;
        let url = new URL(rootURL+"/auth/categories");
        url.searchParams.set("category", country);
        const resp = new XMLHttpRequest();
        resp.open("GET", "/auth/categories");
        resp.send();
        console.log(resp.responseText)
    }
});

document.getElementById("confirmAgeGroup").addEventListener("click", function() {
    if (ageGroupSelect.value !== "") {
        showNextButton("confirmAgeGroup", "confirmParticipantType");
        showNextLabel("ageGroupLabel", "participantTypeLabel");
        showNextSelect("ageGroup", "participantType");
    }
});

document.getElementById("confirmParticipantType").addEventListener("click", function() {
    if (participantTypeSelect.value !== "") {
        showSendButton();
    }
});


function showNextButton(currentButtonId, nextButtonId) {
    document.getElementById(currentButtonId).style.display = "none";
    document.getElementById(nextButtonId).style.display = "block";
}

function showNextLabel(currentLabelId, nextLabelId) {
  document.getElementById(currentLabelId).style.display = "none";
  document.getElementById(nextLabelId).style.display = "block";
}

function showNextSelect(currentSelectId, nextSelectId) {
  document.getElementById(currentSelectId).style.display = "none";
  document.getElementById(nextSelectId).style.display = "block";
}


function showSendButton() {
    document.getElementById("sendData").style.display = "block";
}
