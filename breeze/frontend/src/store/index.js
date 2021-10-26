import Vue from 'vue'
import Vuex from 'vuex'
import user from './user/index.js'
import appointment from './appointment/index.js'
import createPersistedState from "vuex-persistedstate";

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
  },
  plugins: [ createPersistedState({ storage: window.sessionStorage }) ],
})
