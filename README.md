# exam-schedule-web-app

Features:
Add Exams: Users can add exams to the schedule by providing the exam name and date through a form.
Display Exams: The app displays the upcoming exams in a list format, showing the exam name, date, and the number of days left until each exam.
Countdown: The app calculates the number of days left until each exam based on the current date.
How it Works:
Backend (Python with Flask):
The backend is built using Flask, a Python web framework.
It consists of routes to handle HTTP requests: one for the homepage (/) and one to add exams (/add_exam).
Exam data is stored in a Python list called exam_dates.
When a user adds an exam through the form, the data is submitted to the /add_exam route as a POST request. The backend then processes this request, extracts the exam name and date, calculates the number of days until the exam, and adds this information to the exam_dates list.
The homepage route (/) renders an HTML template (index.html) and passes the exam_dates list to it for display.
Frontend (HTML):
The frontend is built using HTML for structure and content.
It includes a form where users can input the exam name and date.
It displays the upcoming exams in a list format, showing the exam name, date, and the number of days left until each exam.
Styling (CSS):
The app includes CSS styles to make it visually appealing and improve user experience.
Styles are applied to elements such as headings, forms, input fields, buttons, and exam entries to enhance their appearance.
How to Use:
Running the App:
Users can run the app locally by executing the Python script (app.py) in their development environment.
The app will start a Flask development server, and users can access it through their web browser at http://localhost:5000.
Adding Exams:
Users can add exams by entering the exam name and date in the provided form and clicking the "Add Exam" button.
Viewing Exam Schedule:
The app will display the upcoming exams along with their dates and the number of days left until each exam.
Users can view this information on the homepage of the app.
