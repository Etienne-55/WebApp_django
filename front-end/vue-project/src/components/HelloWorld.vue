<template>
  <div>
    <h1>{{ helloMessage }}</h1>

    <h2>Login</h2>
      <form @submit.prevent="login">
      <input v-model="email" type="email" placeholder="Email" required /><br><br>

      <input v-model="password" type="password" placeholder="Password" required /><br><br>
      <button type="submit">Login</button><br><br>
    </form>
    <p v-if="message">{{ message }}</p>

    <button @click="goToSignIn">Sign up</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      helloMessage: '',    
      email: '',     
      password: '',
      message: ''     
    };
  },
  created() {
    this.fetchHelloMessage();
  },
  methods: {
   
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
    
    goToSignIn() {
      this.$router.push('/sign-in');
    },
    
    async login() {
      try {
        const response = await fetch('http://127.0.0.1:8000/login/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': this.getCookie('csrftoken')
          },
          body: JSON.stringify({
            email: this.email,
            password: this.password
          })
        });
        const data = await response.text();
        this.message = data;

        if (response.ok) {
          this.$router.push('/logedin');
        } else {
          const data = await response.text();
          this.message = data;
        }
      } catch (error) {
        console.error('Error', error);
        this.message = 'An error has occurred';
      }
    },
    getCookie(name) {
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
  }
}
</script>

<style scoped>

</style>
