<template>
  <div>
    <h1>{{ isEditMode ? 'Edit Coffee' : 'Add Coffee' }}</h1>
    <form @submit.prevent="submitForm">
      <div>
        <label>Name</label>
        <input v-model="coffee.name" required />
      </div>
      <div>
        <label>Origin</label>
        <input v-model="coffee.origin" required />
      </div>
      <div>
        <label>Roast Type</label>
        <input v-model="coffee.roast" required />
      </div>
      <button type="submit">{{ isEditMode ? 'Save Changes' : 'Add Coffee' }}</button>
    </form>
    <button @click="goBackToMenu">Return to menu</button>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      coffee:{
        name: '',
        origin: '',
        roast: '', 
      }
    };
  },
  methods: {
    fetchCoffee(id) {
      axios.get(`/api/coffee/${id}/`)
        .then(response => { this.coffee = response.data; })
        .catch(error => { console.error(error); });
    },
    submitForm() {
      if (this.isEditMode) {
        axios.put(`/api/coffee/${this.$route.params.id}/`, this.coffee)
          .then(() => { this.$router.push('/logedin'); })
          .catch(error => { console.error(error); });
      } else {
        axios.post('/api/coffee/', this.coffee)
          .then(() => { this.$router.push('/logedin'); })
          .catch(error => { console.error(error); });
      }
    },
    goBackToMenu() {
        this.$router.push('/logedin');
      },
  },
  mounted() {
    if (this.$route.params.id) {
      this.isEditMode = true;
      this.fetchCoffee(this.$route.params.id);
    }
  }
}
</script>
