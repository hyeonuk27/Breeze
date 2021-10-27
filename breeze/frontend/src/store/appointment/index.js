export default {
  state: {
    date: new Date(),
    timezone: 'Asia/Seoul',
    participants: [],
  },
  getters: {
    date: state => state.date,
    participants: state => state.participants,
  },
  mutations: {
    SETDATE (state, data) {
      state.date = data
    },
    ADDPARTICIPANT (state, data) {
      state.participants.push(data)
    }
  },
  actions: {
    setDate ({ commit }, data) {
      commit('SETDATE', data)
    },
    addParticipant ({ commit }, data) {
      commit('ADDPARTICIPANT', data)
    }
  },
}