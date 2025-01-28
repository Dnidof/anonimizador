if (document.readyState !== 'loading') {
    onReady();
} else {
    document.addEventListener('DOMContentLoaded', onReady);
}

function onReady() {
    
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

        fetch('http://server:5009/submit', {
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
                downloadLink.href = URL.createObjectURL(blob);
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

}
