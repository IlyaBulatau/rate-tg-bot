let rForm = document.getElementById("registrationForm");
let countrySelect = document.getElementById("country");
let countryOtherSelect = document.getElementById("otherCounty")
let ageGroupSelect = document.getElementById("ageGroup");
let participantTypeSelect = document.getElementById("participantType");
let competitionSelect = document.getElementById("competitionSelect");
const rootURL = window.location.origin;


countrySelect.addEventListener("change", function() {
  let country = countrySelect.value;
    if (country !== "") {
        if (country === "by") {
          document.getElementById("countryLabel").style.display = "none";
          document.getElementById("country").style.display = "none";
            
          document.getElementById("byCountryLink").style.display = "block";
        }

        else if (country === "oth") {
          document.getElementById("countryLabel").style.display = "none";
          document.getElementById("country").style.display = "none";

          document.getElementById("otherCountyLabel").style.display = "block";
          document.getElementById("otherCounty").style.display = "block";
          showSendButton()
        }

        else {
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
          showNextSelect("country", "ageGroup", "ageGroupLabel")
        }
    }
    
  });

ageGroupSelect.addEventListener("change", function() {
    showNextSelect("ageGroup", "participantType", "participantTypeLabel")
});

participantTypeSelect.addEventListener("change", function() {

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
      }
      showNextSelect("participantType", "competitionSelect", "competitionLabel")
});

competitionSelect.addEventListener("change", function() {
    showSendButton()
});


function showNextSelect(currentSelectId, nextSelectId, nextLabel) {
  document.getElementById(currentSelectId).disabled = true;
  document.getElementById(nextSelectId).style.display = "block";
  document.getElementById(nextLabel).style.display = "block";
}


function showSendButton() {
    document.getElementById("sendData").style.display = "block";
}
