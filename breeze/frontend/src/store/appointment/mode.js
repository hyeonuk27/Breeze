export default {
  state: {
    filter: 0,
    menu: 0,
    middle: 0,
    mode1: 0,
    mode2: 0,
  },
  getters: {
    filter: state => state.filter,
    menu: state => state.menu,
    middle: state => state.middle,
    mode1: state => state.mode1,
    mode2: state => state.mode2,
  },
  mutations: {
    SET_FILTER: (state, idx) => {
      state.filter = idx
    },
    SET_MENU: (state, idx) => {
      state.menu = idx
    },
    SET_MIDDLE: (state, idx) => {
      state.middle = idx
    },
    SET_MODE1: (state, idx) => {
      state.mode1 = idx
    },
    SET_MODE2: (state, idx) => {
      state.mode2 = idx
    },
  },
  actions: {
    setFilter({ commit }, idx) {
      commit('SET_FILTER', idx)
    },
    setMenu({ commit }, idx) {
      commit('SET_MENU', idx)
    },
    setMiddle({ commit }, idx) {
      commit('SET_MIDDLE', idx)
    },
    setMode1({ commit }, idx) {
      commit('SET_MODE1', idx)
    },
    setMode2({ commit }, idx) {
      commit('SET_MODE2', idx)
    },
  }
}