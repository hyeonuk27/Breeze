<template>
  <div class="middle-list-container">
    <div class="middle-list-items">
      <div v-for="(place, idx) in middleLists" :key="idx">
        <label class="middle-select-label">
          <input
            type="radio"
            class="circle-input"
            name="circle"
            :value="idx"
            v-model="selectedMiddle"
          />
          <div class="circle-design"></div>
          <div class="desc-text">
            <div class="select-text name">{{ place.name }}</div>
            <div class="select-text time">
              평균 이동 시간 {{ place.avgTime }} 분
            </div>
          </div>
        </label>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters, mapState } from "vuex"

export default {
  name: "MiddleList",
  data() {
    return {
      selectedMiddle: 0,
    }
  },
  methods: {
    ...mapActions(["setMiddle"]),
    middleUpdate(idx) {
      this.setMiddle(idx)
      this.selectedMiddle = idx
    }
  },
  created() {
    this.selectedMiddle = this.middle
  },
  computed: {
    ...mapState({
      middle: (state) => state.mode.middle,
      mode: (state) => state.mode.mode1,
    }),
    ...mapGetters(["middleLists", "participants"]),
  },
  watch: {
    selectedMiddle: function (newVal) {
      this.middleUpdate(newVal)
    },
  }
}
</script>

<style scoped>
.circle-design {
  width: 18px;
  height: 18px;
  border-radius: 100px;
  background: linear-gradient(to right bottom, #92a3fd, #9dceff);
  position: relative;
}
.circle-design::before {
  content: "";
  display: inline-block;
  width: inherit;
  height: inherit;
  border-radius: inherit;
  background: hsl(0, 0%, 90%);
  transition: 0.3s;
}
.circle-input {
  position: absolute;
  left: 0;
  top: 0;
  width: 1px;
  height: 1px;
  opacity: 0;
  z-index: -1;
}
.circle-input:checked + .circle-design::before {
  transform: scale(0);
}
.circle-input:checked ~ .select-text {
  color: hsl(0, 0%, 40%);
}
.desc-text {
  width: 100%;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
}
.desc-text .name {
  font-size: 12px;
}
.desc-text .select-text {
  color: hsl(0, 0%, 60%);
  margin-left: 14px;
  letter-spacing: 2px;
  font-weight: 900;
  transition: 0.3s;
}
.desc-text .time {
  font-size: 10px;
}
.middle-list-container {
  display: flex;
  justify-content: center;
  align-items: center;
}
.middle-list-container .middle-list-items {
  width: 70%;
  height: 90%;
  padding-top: 5%;
}
.middle-select-label {
  display: flex;
  align-items: center;
  border-radius: 25px;
  padding: 10px;
  transition: 0.3s;
}
.middle-select-label:hover,
.middle-select-label:focus-within {
  background: hsla(0, 0%, 80%, 0.14);
}
</style>