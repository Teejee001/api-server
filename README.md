# API Server.

This project is a simple API server built with FastAPI. The server is designed to provide basic information about the user and expose it through a REST API.
## Project Structure

- `main.py`: The main FastAPI application file that contains the API routes.
- `README.md`: This file, containing project documentation.
- `__pycache__/`: Python bytecode cache directory (automatically generated).

## Getting Started

### Prerequisites

Make sure you have Python 3.7 or later installed. You will also need `pip` to install the dependencies.

### Installing Dependencies

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
   cd YOUR_REPO

2. Create a virtual environment:
python3 -m venv myenv
source myenv/bin/activate  # On Windows, use `myenv\Scripts\activate`

3. Install the required dependencies: 
pip install -r requirements.txt

If requirements.txt doesn't exist, manually install the necessary libraries:
pip install fastapi uvicorn

Running the API Server
To run the API server locally:

Activate your virtual environment (if nnot already activated).

Run the FastAPI server using Uvicorn:

uvicorn main:app --reload

3. The API will be running at http://127.0.0.1:8000.

Example Usage
Once the API server is running, you can access the following endpoints:

GET /: Returns basic information about the user (email, current datetime, GitHub URL).

{
  "email": "Olatunjibalogun025@gmail.com",
  "current_datetime": "2025-01-30T07:28:44.142671Z",
  "github_url": "https://github.com/Teejee001/api-server"
}

Deployment
This API can be deployed to platforms like Railway or Render for free hosting.

Deploy on Railway
Go to Railway.app and sign in with your GitHub account.
Click "New Project" → "Deploy from GitHub Repo".
Select the repository and deploy the project.
Railway will assign a public URL for your API.
Deploy on Render
Go to Render.com and sign in with your GitHub account.
Create a new web service and select the repository.
Render will automatically build and deploy your API server.
A public URL will be provided for access.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
FastAPI for building the API.
Uvicorn for running the ASGI server.

