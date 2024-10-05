import { createRouter, createWebHistory } from 'vue-router'

import HomeView from '../views/HomeView.vue'
import SosView from '../views/SosView.vue'
import LoginView from '../views/LoginView.vue'
import SafetyEscortView from '../views/SafetyEscortView.vue'

const routes = [
  {
    path: '/',             
    name: 'home',          
    component: HomeView    
  },
  {
    path: '/sos',          
    name: 'sos',          
    component: SosView   
  },
  {
    path: '/login',        
    name: 'login',         
    component: LoginView   
  },
  {
    path: '/safety-escort',        
    name: 'safety-escort',         
    component: SafetyEscortView   
  },
]

// router instance
const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),  
  routes  
})

export default router
