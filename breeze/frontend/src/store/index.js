import Vue from 'vue'
import Vuex from 'vuex'
import user from './user/user.js'
import mode from './appointment/mode.js'
import appointment from './appointment/appointment.js'

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
    mode,
    appointment,
  }
})
