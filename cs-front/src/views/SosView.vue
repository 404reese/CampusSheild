<template>
  <!-- SOS Alert Component -->
  <div class="sos-view">
    <h2>SOS Alert</h2> <!-- Display the SOS alert heading -->
    <p>Press the "Confirm SOS" button to send an emergency alert.</p> <!-- Provide instructions to the user -->
    <button class="confirm-sos-button" @click="confirmSOS">Confirm SOS</button> <!-- Create a button to trigger SOS confirmation -->
    <div class="emergency-contact">
      <h3>Emergency Contact Number:</h3> <!-- Display a heading for emergency contact number -->
      <p>{{ emergencyNumber }}</p> <!-- Display the emergency contact number -->
    </div>
  </div>
</template>

  
  <script setup>
    import { ref } from 'vue';
  
    // Define the emergency contact number (replace with actual number)
    const emergencyNumber = ref('123-456-7890');
  
    // Function to confirm the SOS
    // const confirmSOS = () => {
    //   // Implement your logic to send the SOS alert here
    //   if ("geolocation" in navigator) {
    //     navigator.geolocation.getCurrentPosition(
    //       function (position) {
    //         const latitude = position.coords.latitude;
    //         const longitude = position.coords.longitude;
    //         alert(`Latitude: ${latitude}, Longitude: ${longitude}`);
    //       },
    //       function (error) {
    //         console.error("Error getting location:", error.message);
    //       }
    //     );
    //   } else {
    //     alert("Geolocation is not available in your browser.");
    //   }
    // };
    const confirmSOS = () => {
  if ("geolocation" in navigator) {
    navigator.geolocation.getCurrentPosition(
      function (position) {
        const latitude = position.coords.latitude;
        const longitude = position.coords.longitude;
        
        // Create a request body with latitude and longitude
        const requestBody = {
          latitude: latitude,
          longitude: longitude
        };

        // Send a POST request to the /sos backend endpoint
        fetch('http://127.0.0.1:5000/sos', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(requestBody)
        })
        .then(response => {
          if (response.ok) {
            // Handle a successful response from the backend
            alert('SOS alert sent successfully.');
          } else {
            // Handle errors from the backend
            console.error('Error sending SOS alert:', response.statusText);
          }
        })
        .catch(error => {
          // Handle network errors
          console.error('Network error:', error);
        });
      },
      function (error) {
        console.error("Error getting location:", error.message);
      }
    );
  } else {
    alert("Geolocation is not available in your browser.");
  }
};

  </script>
  
  <style scoped>
    /* Add your CSS styling here */
    .sos-view {
      text-align: center;
      margin: 20px;
    }
  
    h2 {
      font-size: 1.5rem;
    }
  
    p {
      font-size: 1.2rem;
      margin-bottom: 20px;
    }
  
    .confirm-sos-button {
      background-color: #dc3545;
      color: #fff;
      padding: 10px 20px;
      font-size: 1.2rem;
      border: none;
      cursor: pointer;
    }
  
    .emergency-contact {
      margin-top: 20px;
    }
  
    h3 {
      font-size: 1.2rem;
    }
  
    p {
      font-size: 1.2rem;
    }
  </style>
  
<!-- <template>
    <div class="sos-view">
      <h1>SOS Alert</h1>
      <p>Emergency services have been notified.</p>
      <button class="cancel-button" @click="cancelSOS">Cancel SOS</button>
    </div>
  </template>
  
  <script>
  export default {
    methods: {
      cancelSOS() {
        // Implement cancel SOS functionality here (e.g., stop the alert or notify that help is on the way).
        // You can use this.$router.push('/') to navigate back to the homepage or another appropriate route.
      },
    },
  };
  </script>
  
  <style scoped>
    /* Add your CSS styling here */
    .sos-view {
      text-align: center;
      margin: 20px;
    }
  
    h1 {
      font-size: 2rem;
      margin-bottom: 10px;
    }
  
    p {
      font-size: 1.2rem;
      margin-bottom: 20px;
    }
  
    .cancel-button {
      background-color: #dc3545;
      color: #fff;
      padding: 10px 20px;
      font-size: 1.2rem;
      border: none;
      cursor: pointer;
    }
  </style>
   -->
