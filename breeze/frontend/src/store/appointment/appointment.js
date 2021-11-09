export default {
  state: {
    date: new Date(),
    timezone: 'Asia/Seoul',
    participants: [],
    barami: [],
    //약속쪽지에서 필요한 참여자 정보 리스트(타입, 이름, 시간)
    partMiddleTime: [],
    middleName: '',
    middleLatitude: 0,
    middleLongitude: 0,
    groupName: '',
    groupId: null
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
    //enterinfo에서 참여자 추가할 때마다 사용
    ADDPARTICIPANT (state, data) {
      if (state.barami.length != 0) {
        data['baramiType'] = state.barami.shift()
      }
      state.participants.push(data)
    },
    DELETEPARTICIPANT (state, data) {
      state.barami.push(data[1])
      state.participants.splice(data[0], 1)
    },
    //전체 참여자 초기화 or 그룹 참여자 세팅 시 사용
    SETPARTICIPANTS (state, data) {
      state.participants = data
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
    SETGROUPNAME (state, data) {
      state.groupName = data
    },
    SETGROUPID (state, data) {
      state.groupId = data
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
    setParticipants ({ commit }, data) {
      commit('SETPARTICIPANTS', data)
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
    setGroupName ({ commit }, data) {
      commit('SETGROUPNAME', data)
    },
    setGroupId ({ commit }, data) {
      commit('SETGROUPID', data)
    }
  },
}