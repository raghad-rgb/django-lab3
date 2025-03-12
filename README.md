![image](https://github.com/user-attachments/assets/69af7406-2023-46fd-86e7-b071927d0c45)

![image](https://github.com/user-attachments/assets/b8fce01f-707f-457d-b1c9-c2478e28bd62)

![image](https://github.com/user-attachments/assets/f2ec0782-af4a-4944-98dc-9aad3c9a541b)

![image](https://github.com/user-attachments/assets/990e02c7-19ab-4107-9a34-9593bbc598ad)

![image](https://github.com/user-attachments/assets/95cd44d7-d655-4295-8197-4374a7387c0f)

# ITlan - Trainee & Course Management
![image](https://github.com/user-attachments/assets/c495d573-c5d4-472b-b4fa-92a15820162e)

![image](https://github.com/user-attachments/assets/1e81f6b0-f771-4113-889a-6d244288e194)

![image](https://github.com/user-attachments/assets/3ff80856-5a1c-4980-be99-6069851d9c48)

![image](https://github.com/user-attachments/assets/1c020e4a-dd70-441c-b46a-d46b386c7921)

![image](https://github.com/user-attachments/assets/afa12147-4d4f-4b9a-b209-d684aef509d2)

![image](https://github.com/user-attachments/assets/25a1b1f8-07e7-4ed9-9939-41ea28c98b92)

![image](https://github.com/user-attachments/assets/1a854175-43c8-4635-882d-552c500fb684)

![image](https://github.com/user-attachments/assets/2bbb4d79-c9bc-4b35-9206-e39e99bcc181)

![image](https://github.com/user-attachments/assets/96b5eec5-fa8a-4072-a26e-02ebcb39d2de)

![image](https://github.com/user-attachments/assets/3a40c413-d02e-43c1-a80d-78a54ef3e891)

![image](https://github.com/user-attachments/assets/f9ea0090-a5a9-428a-86cc-de7b49587059)

![image](https://github.com/user-attachments/assets/769bb7d0-f6c0-416f-aab8-b19857f4e4ee)

![image](https://github.com/user-attachments/assets/15792ff5-9739-4436-96ba-bb4a6e08a54b)

![image](https://github.com/user-attachments/assets/9181e6dd-01a6-41b6-9e1f-6ddf0125ebc3)

![image](https://github.com/user-attachments/assets/ca34c9b7-9dc1-4a09-916a-6465b2b3489b)

![image](https://github.com/user-attachments/assets/d557220f-7778-45dd-842c-3a4132665745)

![image](https://github.com/user-attachments/assets/db19fbb4-bf6e-4223-8a4f-2ee8baf9730c)

![image](https://github.com/user-attachments/assets/d0c39df3-6223-492e-934b-0fd067f4dad3)

![image](https://github.com/user-attachments/assets/13dbf092-0cc7-4684-a70e-ff7c7aad32b6)

![image](https://github.com/user-attachments/assets/f2bc6c25-b9c2-462e-bbc6-8179903c9e19)

![image](https://github.com/user-attachments/assets/3a37ec9d-2090-449a-8547-494e5c3e61f9)



## 📌 Project Overview
This project is part of the **ITlan** system and consists of two Django applications:
- **Trainee Management (`trainee_app`)**: Handles trainee information, including adding, updating, and deleting records.
- **Course Management (`course_app`)**: Manages courses, including their details and assignments.

Both apps are integrated with Django's authentication system and use Bootstrap for a modern UI. The project follows best practices in Django development, including the use of **class-based views**, **Django forms**, and **template inheritance**.

---

## 🏗️ Project Structure
```
ITlan/
│── ITlan/               # Main Django project
│   │── settings.py      # Project settings
│   │── urls.py          # Root URL configuration
│   │── wsgi.py          # WSGI entry point
│   │── asgi.py          # ASGI entry point
│
│── trainee_app/         # Trainee management app
│   │── models.py        # Trainee database models
│   │── views.py         # Trainee-related view functions
│   │── urls.py          # URL routing for trainees
│   │── forms.py         # Django forms for trainee input
│   │── templates/
│   │   ├── trainee_list.html      # Displays all trainees
│   │   ├── add_trainee.html       # Form to add a trainee
│   │   ├── update_trainee.html    # Form to update a trainee
│
│── course_app/          # Course management app
│   │── models.py        # Course database models
│   │── views.py         # Course-related view functions
│   │── urls.py          # URL routing for courses
│   │── forms.py         # Django forms for course input
│   │── templates/
│   │   ├── course_list.html       # Displays all courses
│   │   ├── add_course.html        # Form to add a course
│   │   ├── update_course.html     # Form to update a course
│
│── templates/           # Shared templates
│   │── base.html        # Base template with navbar and footer
│   │── home.html        # Welcome page
│
│── static/              # Static assets (CSS, JS, images)
│── manage.py            # Django management script
│── README.md            # Project documentation
```

---

## 🔥 Features
### 🧑‍🎓 Trainee Management (`trainee_app`)
- ✅ **View Trainees**: Displays a table of trainees with details.
- ✅ **Add Trainee**: Form to add a new trainee.
- ✅ **Update Trainee**: Modify trainee details using Django forms.
- ✅ **Delete Trainee**: Remove a trainee from the system.

### 📚 Course Management (`course_app`)
- ✅ **View Courses**: Displays a table of courses with descriptions.
- ✅ **Add Course**: Form to add a new course.
- ✅ **Update Course**: Modify course details.
- ✅ **Delete Course**: Remove a course from the system.

### 🔐 Authentication
- 🔹 **User Login**: Secure login system.
- 🔹 **User Logout**: Ends user sessions securely.
- 🔹 **User Registration**: Allows new users to sign up.

### 🌐 Navigation
- 🏫 **Trainee List**
- ➕ **Add Trainee**
- 📚 **Course List**
- ➕ **Add Course**
- 🔐 **Login/Logout**

---

## 🛠️ Setup Instructions
### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/raghad-rgb/django-lab1.git
cd django-lab1
```

### **2️⃣ Create a Virtual Environment**
```sh
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```

### **3️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **4️⃣ Apply Migrations**
```sh
python manage.py migrate
```

### **5️⃣ Create a Superuser**
```sh
python manage.py createsuperuser
```

### **6️⃣ Run the Development Server**
```sh
python manage.py runserver
```

### **7️⃣ Open the Browser and Visit**
```sh
http://127.0.0.1:8000/
```

---

## 📄 API Endpoints & URLs
| Route                         | Description              | HTTP Method |
|--------------------------------|--------------------------|------------|
| `/trainee/`                    | Trainee List            | `GET`      |
| `/trainee/add/`                | Add Trainee Form        | `GET, POST`|
| `/trainee/update/<id>/`        | Update Trainee          | `GET, POST`|
| `/trainee/delete/<id>/`        | Delete Trainee          | `POST`     |
| `/course/`                     | Course List             | `GET`      |
| `/course/add/`                 | Add Course Form         | `GET, POST`|
| `/course/update/<id>/`         | Update Course          | `GET, POST`|
| `/course/delete/<id>/`         | Delete Course          | `POST`     |

---

## 🏆 Credits
Developed by **Raghad Gamal** ❤️ Using **Django & Bootstrap** for a modern experience.

---

## 📝 License
This project is **open-source** and available under the **MIT License**.

---
### 🎉 **Happy Coding! 🚀**







