let tg = window.Telegram.WebApp;
let rForm = document.getElementById("registrationForm");
let countrySelect = document.getElementById("country");
let ageGroupSelect = document.getElementById("ageGroup");
let categoryTypeSelect = document.getElementById("categoryType");
let participantTypeSelect = document.getElementById("participantType");

document.getElementById("confirmCountry").addEventListener("click", function() {
    if (countrySelect.value !== "") {
        showNextField("confirmCountry", "confirmCategory");
    }
});

document.getElementById("confirmCategory").addEventListener("click", function() {
    if (categoryTypeSelect.value !== "") {
        showNextField("confirmCategory", "confirmAgeGroup");
    }
});

document.getElementById("confirmAgeGroup").addEventListener("click", function() {
    if (ageGroupSelect.value !== "") {
        showNextField("confirmAgeGroup", "confirmParticipantType");
    }
});

document.getElementById("confirmParticipantType").addEventListener("click", function() {
    if (participantTypeSelect.value !== "") {
        showSendButton();
    }
});

document.getElementById("sendData").addEventListener("click", function() {
    // Отправка данных в Telegram
    let formData = {
        "country": countrySelect.value,
        "ageGroup": ageGroupSelect.value,
        "categoryType": categoryTypeSelect.value,
        "participantType": participantTypeSelect.value
    };
    tg.sendData(JSON.stringify(formData));
    tg.close();
});

function showNextField(currentButtonId, nextButtonId) {
    document.getElementById(currentButtonId).style.display = "none";
    document.getElementById(nextButtonId).style.display = "block";
}

function showSendButton() {
    document.getElementById("sendData").style.display = "block";
}
