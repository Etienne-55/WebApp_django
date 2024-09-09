<template>
  <div>
    <!-- Display the Hello World message -->
    <h1>{{ helloMessage }}</h1>

    <!-- Display the Get_name message and input field -->
    <h2>{{ nameMessage }}</h2>
    <input v-model="userName" placeholder="Enter your name" />
    <button @click="submitName">Submit</button>

    <h2>{{ password }}</h2>
    <input v-model="passwordUser" placeholder="Enter your password" />
    <button @click="submitPassword">Submit</button>

    <!-- Display the user's name after submission -->
    <p v-if="submittedName">Hello, {{ submittedName }}!</p>
    <p v-if="submittedPassword">Hello, {{ submittedPassword }}!</p>
    <!-- Error message -->
    <p v-if="errorMessage">{{ errorMessage }}</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      helloMessage: '',    
      nameMessage: '',     
      userName: '',        
      submittedName: '',   
      password: '',
      passwordUser: '',
      submitPassword: '',
      submittedPassword: '',
      errorMessage: ''     
    };
  },
  created() {
    this.fetchHelloMessage();
    this.fetchNameMessage();
    this.fetchPassword();
  },
  methods: {
    // Fetch the HelloWorld message
    async fetchHelloMessage() {
      try {
        const response = await fetch('http://127.0.0.1:8000/api/hello/');
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        const data = await response.json();
        this.helloMessage = data.message;
      } catch (error) {
        console.error('Error fetching HelloWorld message:', error);
        this.errorMessage = 'Error loading HelloWorld message';
      }
    },
    // Fetch the Get_name message
    async fetchNameMessage() {
      try {
        const response = await fetch('http://127.0.0.1:8000/api/get_name/');
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        const data = await response.json();
        this.nameMessage = data.message;
      } catch (error) {
        console.error('Error fetching Get_name message:', error);
        this.errorMessage = 'Error loading Get_name message';
      }
    },
    async fetchPassword() {
      try {
        const response = await fetch('http://127.0.0.1:8000/api/get_password/');
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        const data = await response.json();
        this.password = data.message;
      } catch (error) {
        console.error('Error fetching password.', error);
        this.errorMessage = 'Error loading password.';
      }
    },
    // Handle name submission
    submitName() {
      if (this.userName.trim()) {
        this.submittedName = this.userName;
      } else {
        this.errorMessage = 'Please enter a valid name.';
      }
    },
    submitPassword() {
      if (this.userName.trim()) {
        this.submittedPassword = this.passwordUser;
      } else {
        this.errorMessage = 'Please enter a valid name.';
      }
    }
  }
};


</script>

<style scoped>
/* Add your styles here */
</style>
