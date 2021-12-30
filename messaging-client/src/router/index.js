import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Signup from '../views/Signup.vue'
import Login from '../views/Login.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/signup',
    name: 'Signup',
    component: Signup,
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

router.beforeEach((to, from, next) => {
  if (to.fullPath === '/') {
    if (!localStorage.getItem('token')) {
      next('/login')
    }
  }
  if (to.fullPath === '/login' || to.fullPath === '/signup') {
    if (localStorage.getItem('token')) {
      next('/')
    }
  }
  next()
})

export default router
