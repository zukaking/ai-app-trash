import { createRouter, createWebHistory } from 'vue-router'
import Login from '../components/organisms/LoginView.vue'
import CameraSet from '../components/CameraSet.vue'
import { authorizeToken } from './guards'

const routes = [
  {
    path: '/',
    name: 'CameraSet',
    component: CameraSet,
    meta: {
      requiresAuth: true 
    }
    
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})
router.beforeEach(authorizeToken)

export default router
