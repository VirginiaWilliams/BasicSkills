const { jsPDF } = require("jspdf");


const generateButton = document.querySelector('#generate-button');

const readingInputs = document.querySelector('.reading');

generateButton.addEventListener('click', function() {
    window.alert('hello');
    const doc = new jsPDF();

    doc.text("Hello world!", 10, 10);
    doc.save("a4.pdf");
})

// function getTotal(inputs) {
    
// }

window.addEventListener("DOMContentLoaded", e => {
    document.querySelectorAll(".reading").forEach((element, i) => {
        element.addEventListener("focusout", () => {
            const inputs = document.querySelectorAll(".reading");
            let total = 0

            inputs.forEach(input => {
                total += Number(input.value);
            });

            document.querySelector("#reading-total-display").value = total;
            console.log('---------------');
        })
    });
})