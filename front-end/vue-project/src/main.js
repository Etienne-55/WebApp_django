import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import axios from 'axios';

createApp(App).use(router).mount('#app');
axios.defaults.baseURL = 'http://localhost:8000/'; 

createApp(App)
  .use(router)
  .provide('$axios', axios) 
  .mount('#app');

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
  
  const csrfToken = getCookie('csrftoken');
  
  axios.defaults.headers.common['X-CSRFToken'] = csrfToken;