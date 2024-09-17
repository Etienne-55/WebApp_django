<template>
    <div>
      <h2>Sign Up</h2>
      <form @submit.prevent="signup">
        <input v-model="email" type="email" placeholder="Email" required /><br><br>

        <input v-model="password" type="password" placeholder="Password" required /><br><br>

        <input v-model="confirmPassword" type="password" placeholder="Confirm Password" required /><br><br>

        <button type="submit">Sign Up</button><br><br>
      </form>
      <p v-if="message">{{ message }}</p>

      <button @click="goBack">Go back</button>
    </div>
  </template>
  
  <script>
  import axios from 'axios';

  function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

  export default {
    data() {
      return {
        email: '',
        password: '',
        confirmPassword: '',
        message: ''
      };
    },
  methods: {

    goBack() {
      this.$router.push('/');
    },
    async signup() {
      const csrfToken = getCookie('csrftoken');
      try {
        const response = await axios.post('http://127.0.0.1:8000/signin/', {
          email: this.email,
          password: this.password,
          confirm_password: this.confirmPassword
        }, {
          headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken
          }
        });
        this.message = response.data;
      } catch (error) {
        console.error('Error', error);
        this.message = 'An error has occurred';
      }
    }
  }
};
</script>