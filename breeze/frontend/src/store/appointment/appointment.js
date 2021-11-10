import _ from 'lodash'

export default {
  state: {
    date: new Date(),
    timezone: 'Asia/Seoul',
    participants: [],
    wishPlaces: [],
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
    partMiddleTime: state => state.partMiddleTime,
    wishPlaces: state => state.wishPlaces,
    middleName: state => state.middleName,
    middleLatitude: state => state.middleLatitude,
    middleLongitude: state => state.middleLongitude,
  },
  mutations: {
    SETDATE (state, data) {
      state.date = data
    },
    //enterinfo에서 참여자 추가할 때마다 사용
    ADDPARTICIPANT (state, data) {
      state.participants.push(data)
    },
    DELETEPARTICIPANT (state, data) {
      state.participants.splice(data, 1)
    },
    //전체 참여자 초기화 or 그룹 참여자 세팅 시 사용
    SETPARTICIPANTS (state, data) {
      state.participants = data
    },
    SET_WISH_PLACE (state, data) {
      state.wishPlaces = data
    },
    ADD_WISH_PLACE (state, data) {
      state.wishPlaces.push(data)
      state.wishPlaces = _.uniqBy(state.wishPlaces, 'placeName')
    },
    DELETE_WISH_PLACE (state, data) {
      state.wishPlaces.splice(data, 1)
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
    addGroupParticipants ({ commit }, data) {
      commit('ADDGROUPPARTICIPANTS', data)
    },
    setWishPlace ( {commit}, data) {
      commit('SET_WISH_PLACE', data)
    },
    addWishPlace ({ commit }, data) {
      commit('ADD_WISH_PLACE', data)
    },
    deleteWishPlace ({ commit }, data) {
      commit('DELETE_WISH_PLACE', data)
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