import React from "react";
import "./styles.css";

const App = () => {

    return (
        <div className="container">
            <h1>Upload Document or Enter Text</h1>
            <form id="uploadForm">
                <div className="form-group">
                    <label htmlFor="fileInput">Upload Document:</label>
                    <input type="file" id="fileInput" accept=".txt,.pdf,.doc,.docx"/>
                    <button type="button" id="removeFileButton">Remove File</button>
                </div>
                <div className="form-group">
                    <label htmlFor="textInput">Or Enter Text:</label>
                    <textarea id="textInput" rows="4" cols="50"></textarea>
                </div>
                <button type="button" id="submitButton">Submit</button>
            </form>
            <div id="responseContainer" className="response-container"></div>
        </div>
    );
};

export default App;