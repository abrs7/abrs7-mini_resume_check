# StartUp Agile - Mini Resume Ranker

Welcome to the **StartUp Agile - Mini Resume Ranker**! This project allows you to easily rank resumes against job descriptions using advanced AI-driven scoring. It features an API endpoint for ranking resumes and offers a photo validation feature to check image quality. All results are logged into a database for future analysis.

---


## Project Overview

The **Mini Resume Ranker** is built using **FastAPI** and aims to automate the process of evaluating resumes for specific job descriptions. The service utilizes AI to provide a match score and feedback. Additionally, it has a feature that allows users to upload a photo with their resume for validation, ensuring it meets the required quality standards.

---

## Features

- **Resume Ranking**: Evaluate how well a resume matches a job description.
- **Photo Validation**: Check whether the uploaded photo meets basic quality standards.
- **Database Logging**: All resume matches are stored in a relational database for future reference.
- **Easy-to-use API**: The service provides simple, RESTful endpoints for interaction.

---

## API Documentation

The API is built using **FastAPI** and includes a variety of endpoints for interacting with the resume ranking functionality.

### Base URL

http://localhost:8000

### Health Check Endpoint

- **GET /health**

  A simple endpoint to check if the service is running.

  **Response:**

  ```json
  {
    "status": "ok"
  }
  ```

---

### Resume Ranking Endpoint

- **POST `/rank`**

  Accepts a POST request with a resume and job description. Returns a score and feedback based on AI analysis.

  **Request Body:**
  ```json
  {
    "resume": "string",
    "job_description": "string",
    "photo": "base64_encoded_image_string"  // Optional
  }
  ```
  **Response:**
  ```json
  {
  "score": 95,
  "feedback": "The resume is an excellent match for the job description. The candidate's 6+ years of Python backend experience, specific experience with FastAPI,  proven LLM integration (OpenAI GPT),  CI/CD implementation with Docker and GitHub Actions, and focus on API performance optimization align perfectly with the requirements.  The mention of mentoring and open-source contributions adds value. The only minor gap is a lack of explicit mention of integrating models beyond OpenAI, but the experience with GPT and focus on LLM applications strongly suggests transferrable skills. The candidate's experience surpasses the minimum requirements.",
  "photo_check": "Looks professional"
}
  ```
## Testing

This project uses **pytest** for unit and integration testing. Follow these steps to run the tests:

1. Run all tests::
   ```bash
    pytest tests/
   ```

  ## Setup and Installation

### Prerequisites

- Python 3.9+ installed
- PostgreSQL installed and running

### Clone Repository

```bash
git clone https://github.com/abrs7/abrs7-mini_resume_check.git
cd abrs7-mini_resume_check
```



### Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```
### Docker Setup

1. **Build the Docker image**:
   ```bash
   docker build -t resume-ranker .
   ```
2. **Run the container (ensure your .env file exists in the project root)**
    ```bash
    docker run -p 8000:8000 --env-file .env resume-ranker
    ```
## License

This project is licensed under the [MIT License](LICENSE).  
Created by Abraham Asrat, email: abrahamasrat791@gmail.com