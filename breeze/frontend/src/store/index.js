import Vue from 'vue'
import Vuex from 'vuex'
import user from './user/index.js'
import appointment from './appointment/index.js'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
  },
  mutations: {
  },
  actions: {
  },
  modules: {
    user,
    appointment,
  }
})
