document.addEventListener('DOMContentLoaded', function() {
    
const fileInput = document.getElementById('fileInput');
    const removeFileButton = document.getElementById('removeFileButton');

    fileInput.addEventListener('change', function() {
        if (fileInput.files.length > 0) {
            removeFileButton.style.display = 'inline-block';
        } else {
            removeFileButton.style.display = 'none';
        }
    });

    removeFileButton.addEventListener('click', function() {
        fileInput.value = '';
        removeFileButton.style.display = 'none';
    });

document.getElementById('submitButton').addEventListener('click', function() {
    const fileInput = document.getElementById('fileInput');
    const textInput = document.getElementById('textInput').value;
    const formData = new FormData();

    if (fileInput.files.length > 0) {
        formData.append('file', fileInput.files[0]);
    } else if (textInput.trim() !== '') {
        formData.append('text', textInput);
    } else {
        alert('Please upload a document or enter text.');
        return;
    }

    fetch('http://localhost:4444/submit', {
        method: 'POST',
        body: formData
    })
    .then(response => response.blob())
    .then(blob => {
        const responseContainer = document.getElementById('responseContainer');
        responseContainer.innerHTML = '';

        if (blob.type.startsWith('text/')) {
            const reader = new FileReader();
            reader.onload = function(event) {
                responseContainer.textContent = event.target.result;
            }
            reader.readAsText(blob);
        } else {
            const downloadLink = document.createElement('a');
            const url = URL.createObjectURL(blob);
            downloadLink.href = url;
            downloadLink.download = 'response-document';
            downloadLink.textContent = 'Download response document';
            responseContainer.appendChild(downloadLink);
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('An error occurred. Please try again.');
    });
});

});
