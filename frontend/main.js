window.addEventListener("DOMContentLoaded", (event) => {
    getVisitCount();
})
const functionApiURL = "https://getresume-func.azurewebsites.net/api/GetResumeCounter?";
const localfunctionApi = 'http://localhost:7071/api/GetResumeCounter';

const getVisitCount = () => {
    fetch(functionApiURL)
        .then(response => response.json())
        .then(response => {
            console.log("Website called function API.");
            document.getElementById("counter").innerText = response.counter;
        })
        .catch(function(error){
            console.log(error);
        });
}

