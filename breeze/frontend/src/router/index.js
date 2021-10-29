import Vue from 'vue'
import VueRouter from 'vue-router'
import Welcome from '../views/Welcome.vue'
import Home from '../views/Home.vue'
import EnterInfo from '../views/EnterInfo.vue'
import FindMiddle from '../views/FindMiddle.vue'
import FindPlace from '../views/FindPlace.vue'
import MakeAppointment from '../views/MakeAppointment.vue'
import OneClick from '../views/OneClick.vue'
import LoginRedirect from '../views/LoginRedirect.vue'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Welcome',
    component: Welcome
  },
  {
    path: '/home',
    name: 'Home',
    component: Home
  },
  {
    path: '/enterinfo',
    name: 'EnterInfo',
    component: EnterInfo
  },
  {
    path: '/findmiddle',
    name: 'FindMiddle',
    component: FindMiddle
  },
  {
    path: '/findplace',
    name: 'FindPlace',
    component: FindPlace
  },
  {
    path: '/makeappointment',
    name: 'MakeAppointment',
    component: MakeAppointment
  },
  {
    path: '/oneclick',
    name: 'OneClick',
    component: OneClick
  },
  {
    path: '/oauth/kakao/callback',
    name: 'LoginRedirect',
    component: LoginRedirect
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
