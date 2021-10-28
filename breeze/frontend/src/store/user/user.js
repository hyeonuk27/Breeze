// import router from '../../router/index.js'

export default {
  state: {
    user: null,
  },
  mutations: {
    SET_USER_INFO: function (state, data) {
      state.user = data
    },
    REMOVE_USER: function (state) {
      state.user = null
    }
  },
  actions: {
    setUserInfo: function ({commit}, data) {
      commit('SET_USER_INFO', data)
      // router.push({name: 'Home'})
    },
    removeUser: function ({commit}) {
      commit('REMOVE_USER')
    }
  },
}