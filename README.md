# StartUp Agile - Mini Resume Ranker

Welcome to the **StartUp Agile - Mini Resume Ranker**! This project allows you to easily rank resumes against job descriptions using advanced AI-driven scoring. It features an API endpoint for ranking resumes and offers a photo validation feature to check image quality. All results are logged into a database for future analysis.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [API Documentation](#api-documentation)
- [Technologies](#technologies)
- [Setup and Installation](#setup-and-installation)
- [Health Check](#health-check)
- [Endpoints](#endpoints)
- [Contributing](#contributing)

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

