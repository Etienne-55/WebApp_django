import { createRouter, createWebHistory } from 'vue-router';
import HelloWorld from './components/HelloWorld.vue';
import SignIn from './components/SignIn.vue';
import LogedIn from './components/LogedIn.vue';

const routes = [
  { path: '/', component: HelloWorld },
  { path: '/sign-in', component: SignIn },
  {path: '/logedin', component: LogedIn},
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
