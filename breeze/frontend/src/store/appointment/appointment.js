export default {
  state: {
    date: new Date(),
    timezone: 'Asia/Seoul',
    participants: [],
    wishPlaces: []
  },
  getters: {
    date: state => state.date,
    participants: state => state.participants,
    wishPlaces: state => state.wishPlaces,
  },
  mutations: {
    SETDATE (state, data) {
      state.date = data
    },
    ADDPARTICIPANT (state, data) {
      state.participants.push(data)
    },
    DELETEPARTICIPANT (state, data) {
      state.participants.splice(data, 1)
    },
    ADDGROUPPARTICIPANTS (state, data) {
      state.participants = data
    },
    ADD_WISH_PLACE (state, data) {
      state.wishPlaces.push(data)
    },
    DELETE_WISH_PLACE (state, data) {
      state.wishPlaces.splice(data, 1)
    },
  },
  actions: {
    setDate ({ commit }, data) {
      commit('SETDATE', data)
    },
    addParticipant ({ commit }, data) {
      commit('ADDPARTICIPANT', data)
    },
    deleteParticipant ({ commit }, data) {
      commit('DELETEPARTICIPANT', data)
    },
    addGroupParticipants ({ commit }, data) {
      commit('ADDGROUPPARTICIPANTS', data)
    },
    addWishPlace ({ commit }, data) {
      commit('ADD_WISH_PLACE', data)
    },
    deleteWishPlace ({ commit }, data) {
      commit('DELETE_WISH_PLACE', data)
    },
  },
}