// import router from '../../router/index.js'

export default {
  state: {
    userId: null,
    userName: null,
  },
  mutations: {
    SET_USER: function (state, data) {
      state.userId = data.userId,
      state.userName = data.userName
    },
    REMOVE_USER: function (state) {
      state.userId = null,
      state.userName = null
    }
  },
  actions: {
    setUser: function ({commit}, data) {
      commit('SET_USER', data)
    },
    removeUser: function ({commit}) {
      commit('REMOVE_USER')
    }
  },
  getters: {
    getUserId(state) {
      return state.userId
    },
    isLoggedIn: state => state.userId,
  }
}