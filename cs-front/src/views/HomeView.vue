<template>
  <div class="homepage">
    <!-- Main heading -->
    <h1>Welcome to Campus Safe</h1>
    <p>
      Our mission is to ensure the safety and well-being of all members of our campus community.
    </p>
    <!-- Login button -->
    <router-link to="/login">
      <button class="login-button">Login</button>
    </router-link>

    <!-- Contact Security -->
    <div class="contact-security">
      <h2>Contact Security</h2>
      <!-- Display a list of security contacts -->
      <ul>
        <li v-for="contact in securityContacts" :key="contact.id">
          {{ contact.name }}: {{ contact.phoneNumber }}
        </li>
      </ul>
    </div>

    <!-- Safety Check -->
    <div class="safety-check">
      <h2>Safety Check</h2>
      <p>Click the button below to send your location for safety checking.</p>
    
      <!-- Button to initiate location check -->
      <button @click="getLocationAndCheckSafety">Send Your Location</button>
    
      <!-- Display safety status or alert message here -->
      <p v-if="safetyStatus">{{ safetyStatus }}</p>
    </div>

    <!-- SOS and Safety Escort buttons -->
    <!-- This is a container for two buttons, SOS and Safety Escort -->
      <div class="button-container">

          <!-- The SOS button, when clicked, navigates the user to the /sos route -->
          <router-link to="/sos">
            <button class="sos-button">SOS</button>
          </router-link>

          <!-- The Safety Escort button, when clicked, navigates the user to the /safety-escort route -->
          <router-link to="/safety-escort">
            <button class="safety-escort-button">Safety Escort</button>
          </router-link>

      </div>

  </div>
</template>

<script setup>
  import { ref } from 'vue';

  // Dummy data for security contacts (replace with actual data)
  const securityContacts = ref([
    { id: 1, name: 'Security Officer 1', phoneNumber: '123-456-7890' },
    { id: 2, name: 'Security Officer 2', phoneNumber: '987-654-3210' },
  ]);

  // Function to get location and check safety
  const getLocationAndCheckSafety = () => {
    // Function to send location data to the server
    function sendLocationToServer() {
      navigator.geolocation.getCurrentPosition(function (position) {
        const latitude = position.coords.latitude;
        const longitude = position.coords.longitude;

        // Send the user's location to the Flask backend via a POST request
        fetch('/check-unsafe-zone', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ latitude, longitude }),
        })
          .then((response) => response.json())
          .then((data) => {
            // Handle the response from the server (e.g., show an alert if in an unsafe zone)
          })
          .catch((error) => {
            console.error('Error sending location:', error);
          });
      });
    }

    // Call sendLocationToServer at regular intervals (e.g., every 5 minutes)
    setInterval(sendLocationToServer, 5 * 60 * 1000); // 5 minutes in milliseconds
  };
</script>

<style scoped>
/* CSS styling here */

/* Styles for the homepage container */
.homepage {
  text-align: center; /* Center-align text */
  margin: 20px; /* Add margin around the container */
}

/* Styles for the main heading */
h1 {
  font-size: 2rem; /* Set font size to 2rem (equivalent to 32px) */
  margin-bottom: 10px; /* Add margin below the heading */
}

/* Styles for paragraphs */
p {
  font-size: 1.2rem; /* Set font size to 1.2rem (equivalent to 19.2px) */
  margin-bottom: 20px; /* Add margin below paragraphs */
}

/* Styles for the login button */
.login-button {
  background-color: #007bff; /* Set background color to blue */
  color: #fff; /* Set text color to white */
  padding: 10px 20px; /* Add padding around the button */
  font-size: 1.2rem; /* Set font size to 1.2rem (equivalent to 19.2px) */
  border: none; /* Remove button border */
  cursor: pointer; /* Change cursor to a pointer on hover */
}

/* Styles for the button container */
.button-container {
  /* display: flex; */ /* Commented out for reference */
  justify-content: space-between; /* Space buttons evenly in the container */
  /* Adjust alignment as needed */
  margin-top: 20px; /* Add margin above the button container */
}

/* Styles for the SOS button */
.sos-button {
  background-color: #dc3545; /* Set background color to red */
  color: #fff; /* Set text color to white */
  padding: 10px 20px; /* Add padding around the button */
  font-size: 1.2rem; /* Set font size to 1.2rem (equivalent to 19.2px) */
  border: none; /* Remove button border */
  cursor: pointer; /* Change cursor to a pointer on hover */
  margin-top: 20px; /* Add margin above the SOS button */
}

/* Styles for the contact security section */
.contact-security {
  margin-top: 20px; /* Add margin above the contact security section */
}

/* Styles for the subheading */
h2 {
  font-size: 1.5rem; /* Set font size to 1.5rem (equivalent to 24px) */
}

/* Styles for the unordered list */
ul {
  list-style-type: none; /* Remove list bullets */
  padding: 0; /* Remove default padding */
}

/* Styles for list items */
li {
  font-size: 1.2rem; /* Set font size to 1.2rem (equivalent to 19.2px) */
  margin-bottom: 5px; /* Add margin below list items */
}

/* Styles for the safety escort button */
.safety-escort-button {
  background-color: #28a745; /* Set background color to green */
  color: #fff; /* Set text color to white */
  padding: 10px 20px; /* Add padding around the button */
  font-size: 1.2rem; /* Set font size to 1.2rem (equivalent to 19.2px) */
  border: none; /* Remove button border */
  cursor: pointer; /* Change cursor to a pointer on hover */
  margin-top: 20px; /* Add margin above the safety escort button */
}

</style>
