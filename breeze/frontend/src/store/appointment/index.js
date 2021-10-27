export default {
  state: {
    date: new Date(),
    timezone: 'Asia/Seoul',
    participants: [],
  },
  getters: {
    date: state => state.date,
  },
  mutations: {
    SETDATE: function (state, data) {
      state.date = data
    },
  },
  actions: {
    setDate: function ({ commit }, data) {
      commit('SETDATE', data)
    },
  },
}