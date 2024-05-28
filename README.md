# CLAIM-IT-QM

## Purpose of this Project
This project, CLAIM-IT-QM, was created as part of the ECS639U Web Programming module at Queen Mary University of London. The primary purpose of this project is to help Demonstrators within the EECS school of Queen Mary to log and keep track of their hours with a proper system in place. 
### Mark received: 100%

## Technologies Used
- **Backend**: Django
- **Frontend**: Vue.js with Vite
- **Dependencies**:
  - Django
  - django-cors-headers
  - Vue.js
  - Bootstrap

## How to Run the App

### Create Conda Environment
After cloning this repository, create a conda environment for this project and activate the environment:
```bash
$ conda create --name cwindividual python=3.10
$ conda activate cwindividual
```

### Django Backend

1. **Navigate to the backend folder**:
    ```bash
    $ cd backend
    ```
2. **Install backend dependencies**:
    ```bash
    (cwindividual)$ pip install -r requirements.txt
    ```
3. **Start the backend server**:
    ```bash
    (cwindividual)$ python manage.py runserver
    ```
    The server will start on `http://localhost:8000`

### Vue Frontend

1. **Navigate to the frontend folder**:
    ```bash
    $ cd frontend
    ```
2. **Install frontend dependencies**:
    ```bash
    (cwindividual)$ npm install
    ```
3. **Start the frontend server**:
    ```bash
    (cwindividual)$ npm run dev
    ```
    The server will start on `http://localhost:5173`

## Screenshots
Here are some screenshots of the final application:

### Homepage
![CLAIM-IT-QM Homepage](https://github.com/rohailramesh/ECS639U-Web-Programming-2023-24-CW2/blob/main/Claim_Homepage.png)

### Add Claim
![CLAIM-IT-QM Add Claim](https://github.com/rohailramesh/ECS639U-Web-Programming-2023-24-CW2/blob/main/Add_Claim.png)

### Delete Claim
![CLAIM-IT-QM Delete Claim](https://github.com/rohailramesh/ECS639U-Web-Programming-2023-24-CW2/blob/main/Delete_Claim.png)

### Update Claim
![CLAIM-IT-QM Update Claim](https://github.com/rohailramesh/ECS639U-Web-Programming-2023-24-CW2/blob/main/Update_Claim.png)

### Find Claim
![CLAIM-IT-QM Find Claim](https://github.com/rohailramesh/ECS639U-Web-Programming-2023-24-CW2/blob/main/Find_Claim.png)
