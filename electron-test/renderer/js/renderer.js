import { PER17Reading } from "../questions/PER17Questions.js";

window.addEventListener("DOMContentLoaded", e => {
    
    // Add student section
    // const readingSection = document.querySelector(".student-info");

    // PER17Reading.forEach(input => {
    //     readingSection.innerHTML += 
    //     `<p>${input.label}</p>
    //     <input type="text" name="studentName" id="studentName"/>
    //     <p>${input.total}</p>`
    // });


    // Event listeners
    document.querySelectorAll(".reading").forEach((element, i) => {
        element.addEventListener("focusout", () => {
            const inputs = document.querySelectorAll(".reading");
            let total = 0

            inputs.forEach(input => {
                total += Number(input.value);
            });

            document.querySelector("#reading-total-display").value = total;
        })
    });
})