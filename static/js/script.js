function previewImage(event) {
    const img = document.getElementById('preview');
    img.src = URL.createObjectURL(event.target.files[0]);
    img.style.display = 'block';
}

function showLoader() {
    document.getElementById("loader").style.display = "block";
}

// Animate confidence bar
window.onload = function() {
    const resultText = document.querySelector('.result');
    if (resultText) {
        const text = resultText.innerText;
        const match = text.match(/\((.*?)%\)/);
        if (match) {
            let value = parseFloat(match[1]);
            document.getElementById("confidenceFill").style.width = value + "%";
        }
    }
}