const { jsPDF } = require("jspdf");

const generateButton = document.querySelector('#generate-button');

generateButton.addEventListener('click', async function() {
  // Remove junk

  var inputs = document.querySelectorAll('input');
  inputs.forEach(i => {
    i.style.border = '0 none';
  });

  var disappearMe = document.querySelectorAll('.disappear');
  disappearMe.forEach(d => {
    d.style.display = 'none';
  });

  // Process

  var element = document.getElementById('entire-thing');
  var opt = {
    margin:       0.5,
    filename:     'file.pdf',
    html2canvas:  { scale: 1, scrollY: 0 },
    jsPDF:        { unit: 'in', format: 'letter', orientation: 'portrait' },
    scale: 4,
    letterRendering: true,
    image: { type: 'jpeg', quality: 1 },
    html2canvas: {
      dpi: 192,
      scale: 4,
      scrollY: 0,
      letterRendering: true,
      useCORS: true
    },
  };

  await html2pdf().from(element).set(opt).save();

  // Add junk back in

  inputs.forEach(i => {
    i.style.border = '';
  });

  disappearMe.forEach(d => {
    d.style.display = '';
  });
})

// reset button

const resetButton = document.querySelector('#reset-button');

resetButton.addEventListener('click', async function() {
  document.getElementById("input-form").reset();
});