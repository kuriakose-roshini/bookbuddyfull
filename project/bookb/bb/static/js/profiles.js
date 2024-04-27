const form = document.getElementById('profile-form');

form.addEventListener('submit', (e) => {
  e.preventDefault(); // prevent the form from submitting normally

  const name = document.getElementById('name').value;
  const email = document.getElementById('email').value;
  const memid = document.getElementById('memid').value;
  const dept = document.getElementById('dept').value;
  // Perform any necessary validation here

  // Update the user's profile
  updateProfile(name, email,memid,dept);
});

function updateProfile(name, email,memid,dept) {
  // Make an API request or perform any necessary logic to update the user's profile

  // Display a success message
  alert('Profile updated successfully!');
}