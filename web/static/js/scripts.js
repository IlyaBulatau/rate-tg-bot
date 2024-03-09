let rForm = document.getElementById("registrationForm");
let countrySelect = document.getElementById("country");
let countryOtherSelect = document.getElementById("otherCounty")
let ageGroupSelect = document.getElementById("ageGroup");
let participantTypeSelect = document.getElementById("participantType");
let competitionSelect = document.getElementById("competitionSelect");
const rootURL = window.location.origin;

document.getElementById("confirmCountry").addEventListener("click", function() {
  // кнопка выбор страны
    let country = countrySelect.value;
    if (country !== "") {
        if (country === "by") {
          document.getElementById("confirmCountry").style.display = "none";
          document.getElementById("countryLabel").style.display = "none";
          document.getElementById("country").style.display = "none";

          document.getElementById("byCountryLink").style.display = "block";
        }

        else if (country === "oth") {
          document.getElementById("confirmCountry").style.display = "none";
          document.getElementById("countryLabel").style.display = "none";
          document.getElementById("country").style.display = "none";

          document.getElementById("otherCountyLabel").style.display = "block";
          document.getElementById("otherCounty").style.display = "block";
          document.getElementById("otherCountyButton").style.display = "block";

        }

        else {
          showNextButton("confirmCountry", "confirmAgeGroup");
          showNextLabel("countryLabel", "ageGroupLabel");
          showNextSelect("country", "ageGroup");
  
          let url = new URL(rootURL+"/auth/categories");
          url.searchParams.set("category", country);
  
          fetch(url)
          .then(response => {
            return response.json();
          })
          .then(data => {
            data["categories"].forEach(element => {
              Object.entries(element).forEach(([key, val]) => {
                let option = document.createElement("option");
                option.value = key;
                option.text = val;
                ageGroupSelect.add(option);
              });
            });
          })
        }
       
    }
});

document.getElementById("otherCountyButton").addEventListener("click", function() {
    countrySelect.value = otherCounty.value
    document.getElementById("sendData").style.display = "block";
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
        let country = countrySelect.value;
        let age = ageGroupSelect.value;
        let practic = participantTypeSelect.value;

        let url = new URL(rootURL+"/auth/competitions");
        url.searchParams.set("country", country);
        url.searchParams.set("category", age);
        url.searchParams.set("practic", practic);

        fetch(url)
          .then(response => {
            return response.json();
          })
          .then(data => {
              Object.entries(data).forEach(([key, val]) => {
                let option = document.createElement("option");
                option.value = key;
                option.text = val;
                competitionSelect.add(option);
              });
            });
          

        showNextButton("confirmParticipantType", "configrmCompetitionButton")
        showNextLabel("participantTypeLabel", "competitionLabel")
        showNextSelect("participantType", "competitionSelect")
    }
});


document.getElementById("configrmCompetitionButton").addEventListener("click", function() {
  if (competitionSelect.value !== "") {
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
