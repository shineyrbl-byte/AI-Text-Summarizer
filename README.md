# AI Text Summarizer

## Overview

AI Text Summarizer is a web application that generates concise summaries from large text passages and PDF documents using Natural Language Processing (NLP).

The application allows users to:

* Paste text and generate summaries
* Upload PDF documents and summarize their contents
* Choose between Short, Medium, and Long summaries
* View generated summaries instantly through a simple user interface

The project follows a client-server architecture using React for the frontend and FastAPI for the backend.

---

# Features

### Text Summarization

Users can enter large blocks of text and generate concise summaries.

### PDF Summarization

Users can upload PDF files. The application extracts text from the PDF and generates a summary.

### Multiple Summary Lengths

Users can select:

* Short Summary
* Medium Summary
* Long Summary

### Loading Indicator

A loading message is displayed while the summary is being generated.

### REST API Integration

The frontend communicates with the backend using FastAPI APIs.

---

# Technology Stack

## Frontend

* React.js
* Axios
* JavaScript
* HTML

### Why React?

React was chosen because:

* Component-based architecture
* Fast rendering
* Easy API integration
* Suitable for modern web applications

### Why Axios?

Axios is used for:

* Sending HTTP requests
* Communicating with FastAPI endpoints
* Handling API responses efficiently

---

## Backend

* FastAPI
* Python

### Why FastAPI?

FastAPI was chosen because:

* High performance
* Easy REST API development
* Automatic API documentation
* Simple integration with machine learning models

---

## NLP Model

### Hugging Face Transformers

Model Used:

```text
sshleifer/distilbart-cnn-12-6
```

### Why This Model?

* Designed specifically for summarization tasks
* Generates abstractive summaries
* Produces human-like summaries instead of simply extracting sentences
* Lightweight compared to larger transformer models

---

## PDF Processing

Library Used:

```python
pypdf
```

### Why pypdf?

* Extracts text from uploaded PDF files
* Lightweight and easy to integrate
* Supports multi-page PDFs

---

# Project Structure

```text
AI-Summarizer
│
├── backend
│   ├── main.py
│   ├── summarizer.py
│   ├── pdf_reader.py
│   ├── requirements.txt
│
├── frontend
│   ├── src
│   │   ├── App.jsx
│   │   ├── main.jsx
│   │
│   ├── package.json
│
└── README.md
```

---

# File Explanation

## main.py

Main FastAPI application.

Responsibilities:

* Creates API endpoints
* Receives user requests
* Calls summarization functions
* Returns generated summaries

Endpoints:

```text
POST /summarize
POST /summarize-pdf
```

---

## summarizer.py

Contains the summarization logic.

Responsibilities:

* Loads the Hugging Face model
* Receives text input
* Generates summaries
* Supports different summary lengths

---

## pdf_reader.py

Responsible for PDF text extraction.

Responsibilities:

* Reads uploaded PDF files
* Extracts text page-by-page
* Returns extracted text to backend

---

## App.jsx

Main React component.

Responsibilities:

* User interface
* Text input
* PDF upload
* Summary length selection
* API communication
* Displaying generated summaries

---

# Workflow

## Text Summarization Workflow

1. User enters text.
2. User selects summary length.
3. User clicks "Summarize".
4. React sends request to FastAPI.
5. FastAPI calls summarizer.py.
6. Hugging Face model generates summary.
7. Summary is returned to frontend.
8. Summary is displayed to the user.

---

## PDF Summarization Workflow

1. User uploads PDF.
2. PDF is sent to FastAPI.
3. pdf_reader.py extracts text.
4. Extracted text is passed to summarizer.py.
5. Summary is generated.
6. Summary is returned to frontend.
7. Summary is displayed.

---

# API Endpoints

## Text Summarization

```http
POST /summarize
```

Request:

```json
{
  "text": "Input text",
  "length": "medium"
}
```

Response:

```json
{
  "summary": "Generated summary"
}
```

---

## PDF Summarization

```http
POST /summarize-pdf
```

Form Data:

```text
file
length
```

Response:

```json
{
  "summary": "Generated summary"
}
```

---

# Running the Project

## Backend Setup

Navigate to backend folder:

```bash
cd backend
```

Create virtual environment:

```bash
python -m venv venv
```

Activate virtual environment:

### Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run FastAPI server:

```bash
python -m uvicorn main:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

---

## Frontend Setup

Navigate to frontend folder:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Run React application:

```bash
npm run dev
```

Frontend URL:

```text
http://localhost:5173
```

---

# Deployment

## Frontend Deployment

Frontend is deployed using Vercel.

The deployed frontend provides the user interface for the application.

## Backend Requirement

The application requires the FastAPI backend to be running because:

* Summarization is performed on the server side.
* PDF text extraction occurs on the backend.
* The frontend communicates with backend APIs to generate summaries.

---

# Future Improvements

* Authentication and user accounts
* Summary history storage
* Download summaries as PDF
* Multiple language support
* AI-powered keyword extraction
* AI-powered topic detection
* Cloud deployment of backend services
* Enhanced PDF processing

---

# Author

Avisha Srivastava

AI Text Summarizer Internship Project

Built using React, FastAPI, Hugging Face Transformers, and PyPDF.
