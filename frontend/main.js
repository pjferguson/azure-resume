window.addEventListener("DOMContentLoaded", (event) => {
    getVisitCount();
})

const functionApi = 'http://localhost:7071/api/GetResumeCounter';

const getVisitCount = () => {
    fetch(functionApi)
        .then(response => response.json())
        .then(response => {
            console.log("Website called function API.");
            document.getElementById("counter").innerText = response.counter;
        })
        .catch(function(error){
            console.log(error);
        });
}

