import React from "react";
import "./styles.css";

const App = () => {
    const submit = () => {
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
    }
    const clickRemove = () => {
        const fileInput = document.getElementById('fileInput');
        const removeFileButton = document.getElementById('removeFileButton');
        fileInput.value = '';
        removeFileButton.style.display = 'none';
    }
    const changeFile = () => {
        const fileInput = document.getElementById('fileInput');
        const removeFileButton = document.getElementById('removeFileButton');
        if (fileInput.files.length > 0) {
            removeFileButton.style.display = 'inline-block';
        } else {
            removeFileButton.style.display = 'none';
        }
    }

    return (
        <div className="container">
            <h1>Upload Document or Enter Text</h1>
            <form id="uploadForm">
                <div className="form-group">
                    <label htmlFor="fileInput">Upload Document:</label>
                    <input type="file" id="fileInput" accept=".txt,.pdf,.doc,.docx" onChange={changeFile}/>
                    <button type="button" id="removeFileButton" onClick={clickRemove}>Remove File</button>
                </div>
                <div className="form-group">
                    <label htmlFor="textInput">Or Enter Text:</label>
                    <textarea id="textInput" rows="4" cols="50"></textarea>
                </div>
                <button type="button" id="submitButton" onClick={submit}>Submit</button>
            </form>
            <div id="responseContainer" className="response-container"></div>
        </div>
    );
};

export default App;