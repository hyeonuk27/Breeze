export default {
  state: {
    // 0: 완벽한 중간 1: 핫플레이스 2: 코로나멈춰
    mode1: 0,
    // 0: 식당 1: 카페 2: 술집 3: 문화
    mode2: 0,
  },
  mutations: {
    SET_MODE1: (state, idx) => {
      state.mode1 = idx
    },
    SET_MODE2: (state, idx) => {
      state.mode2 = idx
    },
  },
  actions: {
    setMode1({commit}, idx) {
    commit('SET_MODE1', idx)
    },
    setMode2({commit}, idx) {
    commit('SET_MODE2', idx)
    }
  }
}