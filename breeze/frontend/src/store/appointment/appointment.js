import _ from 'lodash'

export default {
  state: {
    barami: [],
    date: '',
    groupId: null,
    groupName: '',
    isAppointmentDeleted: false,
    isFirst: false,
    isGroupSaved: false,
    isMapRendered: false,
    middleLists: [],
    middleLatitude: 0,
    middleLongitude: 0,
    middleName: '',
    participants: [],
    partMiddleTime: [],
    timezone: 'Asia/Seoul',
    wishPlaces: [],
  },
  getters: {
    date: state => state.date,
    getGroupId(state) {
      return state.groupId
    },
    getIsGroupSaved(state) {
      return state.isGroupSaved
    },
    getIsFirst(state) {
      return state.isFirst
    },
    groupId: state => state.groupId,
    isAppointmentDeleted: state => state.isAppointmentDeleted,
    isFirst: state => state.isFirst,
    isGroupSaved: state => state.isGroupSaved,
    isMapRendered: state => state.isMapRendered,
    middleName: state => state.middleName,
    middleLatitude: state => state.middleLatitude,
    middleLongitude: state => state.middleLongitude,
    middleLists: state => state.middleLists,
    participants: state => state.participants,
    partMiddleTime: state => state.partMiddleTime,
    wishPlaces: state => state.wishPlaces,
  },
  mutations: {
    ADD_PARTICIPANT(state, data) {
      if (state.barami.length != 0) {
        data['baramiType'] = state.barami.shift()
      }
      state.participants.push(data)
    },
    ADD_WISH_PLACE(state, data) {
      state.wishPlaces.push(data)
      state.wishPlaces = _.uniqBy(state.wishPlaces, 'placeName')
    },
    DELETE_PARTICIPANT(state, data) {
      state.barami.push(data[1])
      state.participants.splice(data[0], 1)
    },
    DELETE_WISH_PLACE(state, data) {
      state.wishPlaces.splice(data, 1)
    },
    SET_DATE(state, data) {
      state.date = data
    },
    SET_GROUP_ID(state, data) {
      state.groupId = data
    },
    SET_GROUP_NAME(state, data) {
      state.groupName = data
    },
    SET_IS_APPOINTMENT_DELETED(state, data) {
      state.isAppointmentDeleted = data
    },
    SET_IS_FIRST(state, data) {
      state.isFirst = data
    },
    SET_IS_GROUPSAVED(state, data) {
      state.isGroupSaved = data
    },
    SET_IS_MAPRENDERED(state, data) {
      state.isMapRendered = data
    },
    SET_MIDDLE_LAT(state, data) {
      state.middleLatitude = data
    },
    SET_MIDDLE_LISTS(state, data) {
      state.middleLists = data
    },
    SET_MIDDLE_LONG(state, data) {
      state.middleLongitude = data
    },
    SET_MIDDLE_NAME(state, data) {
      state.middleName = data
    },
    SET_PART_MID_TIME(state, data) {
      state.partMiddleTime = data
    },
    SET_PARTICIPANTS(state, data) {
      state.participants = data
    },
    SET_WISH_PLACE(state, data) {
      state.wishPlaces = data
    },
  },
  actions: {
    addParticipant({ commit }, data) {
      commit('ADD_PARTICIPANT', data)
    },
    addWishPlace({ commit }, data) {
      commit('ADD_WISH_PLACE', data)
    },
    deleteParticipant({ commit }, data) {
      commit('DELETE_PARTICIPANT', data)
    },
    deleteWishPlace({ commit }, data) {
      commit('DELETE_WISH_PLACE', data)
    },
    setDate({ commit }, data) {
      commit('SET_DATE', data)
    },
    setGroupId({ commit }, data) {
      commit('SET_GROUP_ID', data)
    },
    setGroupName({ commit }, data) {
      commit('SET_GROUP_NAME', data)
    },
    setIsAppointmentDeleted({ commit }, data) {
      commit('SET_IS_APPOINTMENT_DELETED', data)
    },
    setIsFirst({ commit }, data) {
      commit('SET_IS_FIRST', data)
    },
    setIsGroupSaved({ commit }, data) {
      commit('SET_IS_GROUPSAVED', data)
    },
    setIsMapRendered({ commit }, data) {
      commit('SET_IS_MAPRENDERED', data)
    },
    setMiddleLat({ commit }, data) {
      commit('SET_MIDDLE_LAT', data)
    },
    setMiddleLists({ commit }, data) {
      commit('SET_MIDDLE_LISTS', data)
    },
    setMiddleLong({ commit }, data) {
      commit('SET_MIDDLE_LONG', data)
    },
    setMiddleName({ commit }, data) {
      commit('SET_MIDDLE_NAME', data)
    },
    setPartMidTime({ commit }, data) {
      commit('SET_PART_MID_TIME', data)
    },
    setParticipants({ commit }, data) {
      commit('SET_PARTICIPANTS', data)
    },
    setWishPlace({ commit }, data) {
      commit('SET_WISH_PLACE', data)
    },
  },
}