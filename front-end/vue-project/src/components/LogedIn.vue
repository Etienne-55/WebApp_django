<template>
    <div>
      <h1>{{ hello }}</h1><br><br>
      
      <button @click="goToMenu">Return to menu</button>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        hello: '',     
      };
    },
    created() {
      this.fetchHello();
    },
    methods: {
     
      async fetchHello() {
        try {
          const response = await fetch('http://127.0.0.1:8000/hello/');
          if (!response.ok) {
            throw new Error('Network response was not ok');
          }
          const data = await response.json();
          this.hello = data.message;
        } catch (error) {
          console.error('Error fetching HelloWorld message:', error);
          this.errorMessage = 'Error loading HelloWorld message';
        }
      },
      
      goToMenu() {
        this.$router.push('/');
      },
    }
  };
  </script>
  
  <style scoped>
  
  </style>
  