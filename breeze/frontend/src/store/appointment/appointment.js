export default {
  state: {
    date: new Date(),
    timezone: 'Asia/Seoul',
    participants: [],
    //약속쪽지에서 필요한 참여자 정보 리스트(타입, 이름, 시간)
    partMiddleTime: [],
    middleName: '',
    middleLatitude: 0,
    middleLongitude: 0
  },
  getters: {
    date: state => state.date,
    participants: state => state.participants,
    partMiddleTime: state => state.partMiddleTime
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
    //전체 참여자 초기화
    SETPARTICIPANTS (state) {
      state.participants = []
    },
    SETPARTMIDTIME (state, data) {
      state.partMiddleTime = data
    },
    SETMIDDLENAME (state, data) {
      state.middleName = data
    },
    SETMIDDLELAT (state, data) {
      state.middleLatitude = data
    },
    SETMIDDLELONG (state, data) {
      state.middleLongitude = data
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
    setParticipants ({ commit }) {
      commit('SETPARTICIPANTS')
    },
    setPartMidTime ({ commit }, data) {
      commit('SETPARTMIDTIME', data)
    },
    setMiddleName ({ commit }, data) {
      commit('SETMIDDLENAME', data)
    },
    setMiddleLat ({ commit }, data) {
      commit('SETMIDDLELAT', data)
    },
    setMiddleLong ({ commit }, data) {
      commit('SETMIDDLELONG', data)
    },
  },
}