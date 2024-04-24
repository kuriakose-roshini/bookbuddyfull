/*const studentForm = document.getElementById("studentForm");
        const facultyForm = document.getElementById("facultyForm");
        const adminForm = document.getElementById("adminForm");

        const studentUsername = document.getElementById("studentUsername");
        const studentPassword = document.getElementById("studentPassword");

        studentForm.addEventListener("submit", (e) => {
          e.preventDefault();
          if (studentUsername.value === "student" && studentPassword.value === "password") {
            alert("Login successful!");
            // Redirect to the desired page
            window.location.href = "list.html";
          } else {
            alert("Invalid username or password.");
          }
        });

        const facultyUsername = document.getElementById("facultyUsername");
        const facultyPassword = document.getElementById("facultyPassword");

        facultyForm.addEventListener("submit", (e) => {
          e.preventDefault();
          if (facultyUsername.value === "faculty" && facultyPassword.value === "password") {
            alert("Login successful!");
            // Redirect to the desired page
            window.location.href = "list.html";
          } else {
            alert("Invalid username or password.");
          }
        });

        const adminUsername = document.getElementById("adminUsername");
        const adminPassword = document.getElementById("adminPassword");

        adminForm.addEventListener("submit", (e) => {
          e.preventDefault();
          if (adminUsername.value === "admin" && adminPassword.value === "password") {
            alert("Login successful!");
            // Redirect to the desired page
            window.location.href = "mngbook.html";
          } else {
            alert("Invalid username or password.");
          }
        });
/*
        var attempt = 3; // Variable to count number of attempts.
// Below function Executes on click of login button.
function validate(){
var username = document.getElementById("username").value;
var password = document.getElementById("password").value;
if ( username == "Formget" && password == "formget#123"){
alert ("Login successfully");
window.location = "success.html"; // Redirecting to other page.
return false;
}
else{
attempt --;// Decrementing by one.
alert("You have left "+attempt+" attempt;");
// Disabling fields after 3 attempts.
if( attempt == 0){
document.getElementById("username").disabled = true;
document.getElementById("password").disabled = true;
document.getElementById("submit").disabled = true;
return false;
}
}
}
*/
const express = require('express');
const session = require('express-session');
const bcrypt = require('bcrypt');
const mongoose = require('mongoose');

const app = express();
const port = 3000;

// Connect to MongoDB
mongoose.connect('mongodb://localhost:27017/login_demo', { useNewUrlParser: true, useUnifiedTopology: true });
const db = mongoose.connection;
db.on('error', console.error.bind(console, 'connection error:'));
db.once('open', function () {
    console.log('Connected to MongoDB');
});

// Define User schema
const userSchema = new mongoose.Schema({
    username: String,
    password: String
});
const User = mongoose.model('User', userSchema);

// Middleware for session management
app.use(session({
    secret: 'your_secret_key',
    resave: false,
    saveUninitialized: true
}));

// Middleware for parsing JSON and URL encoded bodies
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Route for login page
app.post('/login', async (req, res) => {
    const { username, password } = req.body;
    try {
        const user = await User.findOne({ username });
        if (user && bcrypt.compareSync(password, user.password)) {
            req.session.username = username;
            res.redirect('/dashboard');
        } else {
            res.status(401).send('Invalid username or password');
        }
    } catch (error) {
        console.error(error);
        res.status(500).send('Internal server error');
    }
});

// Route for dashboard page
app.get('/dashboard', (req, res) => {
    if (req.session.username) {
        res.send(`Welcome, ${req.session.username}!`);
    } else {
        res.redirect('/');
    }
});

// Route for logout
app.get('/logout', (req, res) => {
    req.session.destroy();
    res.redirect('/');
});

// Start the server
app.listen(port, () => {
    console.log(`Server is listening on port ${port}`);
});
