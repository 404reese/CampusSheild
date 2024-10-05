<template>
  <!-- Login form container -->
  <div class="login">
    <!-- Form header -->
    <h2>Login</h2>
    
    <!-- Form element with submit event handler -->
    <form @submit.prevent="login">
      <!-- ID input field -->
      <div class="form-group">
        <label for="id">ID:</label>
        <input type="text" id="id" v-model="id" required />
      </div>

      <!-- Password input field -->
      <div class="form-group">
        <label for="password">Password:</label>
        <input type="password" id="password" v-model="password" required />
      </div>

      <!-- Submit button -->
      <button type="submit">Log In</button>
    </form>
  </div>
</template>

  <script setup>
    // Define data properties for ID and password
    let id = '';
    let password = '';
  
    // Function to handle login
    const login = () => {
      // Implement your login logic here, e.g., check credentials and navigate to the homepage
    };
  </script>
  
  <style scoped>
    /*  CSS styling here */
    .login {
      text-align: center;
      margin: 20px;
    }
  
    h2 {
      font-size: 1.5rem;
    }
  
    form {
      display: flex;
      flex-direction: column;
      align-items: center;
    }
  
    .form-group {
      margin-bottom: 20px;
    }
  
    label {
      font-size: 1.2rem;
    }
  
    input {
      width: 100%;
      padding: 10px;
      font-size: 1.2rem;
      border: 1px solid #ccc;
    }
  
    button {
      background-color: #007bff;
      color: #fff;
      padding: 10px 20px;
      font-size: 1.2rem;
      border: none;
      cursor: pointer;
    }
  </style>
  