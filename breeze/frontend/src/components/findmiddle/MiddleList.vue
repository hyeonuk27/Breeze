<template>
  <div>
    <div 
      v-for="(place, idx) in modeList" 
      :key="idx"
    >
      <label class="rad-label">
        <input 
          type="radio" 
          class="rad-input" 
          name="rad" 
          :value="idx" 
          v-model="selectedMiddle">
        <div class="rad-design"></div>
        <div class="rad-text">{{ place.name }}</div>
        <div>평균 이동 시간 {{ modeAvgTime[idx]}} 분</div>
      </label>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
export default {
  name: 'MiddleList',
  props: {
    middlePlaces: Array
  },
  data() {
    return {
      selectedMiddle: 0,
      //props로 받은 전체 중간 장소 리스트
      middleList: this.middlePlaces,
      //헤더 모드에 따라 분류된 장소 리스트
      modeList: [],
      //헤더 모드에 따라 소요되는 장소별 평균 시간
      modeAvgTime: [],
    }
  },
  methods: {
    ...mapActions([
      'setMiddle'
    ]),
    filterList(idx) {
      this.modeList = []
      for (let i = 0; i < this.middleList.length; i++) {
        if (this.middleList[i].middle_place_type === idx) {
          this.modeList.push(this.middleList[i])
        }
      } 
    },
    middleUpdate(idx) {
      this.setMiddle(idx)
      this.selectedMiddle = idx
    },
    partAverageTime(data) {
      let temp = []
      this.modeAvgTime = []
      const placeCnt = data.length
      for (let i = 0; i < placeCnt; i++) {
        const partCnt = data[i].participants.length
        for (let j = 0; j < partCnt; j++) {
          temp.push(data[i].participants[j].time)
        }
        // console.log(temp, '장소별 각 참가자의 소요 시간')
        const result = temp.reduce(function add(sum, currVal) {
          return sum + currVal
        }, 0)
        const avg = Math.round(result / temp.length)
        this.modeAvgTime.push(avg)
        // console.log(this.modeAvgTime, '장소별 평균 시간')
        temp = []
      }
    }
  },
  created() {
    this.filterList(this.mode)
    this.partAverageTime(this.modeList)
    this.selectedMiddle = this.middle
  },
  computed: {
    ...mapState({
      mode: state => state.mode.mode1,
      middle: state => state.mode.middle
    }),  
  },
  watch: {
    selectedMiddle : function (newVal, ) {
      this.middleUpdate(newVal)
    },
    mode : function (newVal, ) {
      // console.log('바뀐 값--->' + newVal, '이전 값--->' + oldVal)
      this.filterList(newVal)
      this.partAverageTime(this.modeList)
      this.middleUpdate(0)
    }
  }
}
</script>

<style scoped>
.rad-label {
  display: flex;
  align-items: center;

  border-radius: 25px;
  padding: 14px 16px;
  margin: 10px 0;

  cursor: pointer;
  transition: .3s;
}

.rad-label:hover,
.rad-label:focus-within {
  background: hsla(0, 0%, 80%, .14);
}

.rad-input {
  position: absolute;
  left: 0;
  top: 0;
  width: 1px;
  height: 1px;
  opacity: 0;
  z-index: -1;
}

.rad-design {
  width: 22px;
  height: 22px;
  border-radius: 100px;

  background: linear-gradient(to right bottom, hsl(154, 97%, 62%), hsl(225, 97%, 62%));
  position: relative;
}

.rad-design::before {
  content: '';

  display: inline-block;
  width: inherit;
  height: inherit;
  border-radius: inherit;

  background: hsl(0, 0%, 90%);
  transform: scale(1.1);
  transition: .3s;
}

.rad-input:checked+.rad-design::before {
  transform: scale(0);
}

.rad-text {
  color: hsl(0, 0%, 60%);
  margin-left: 14px;
  letter-spacing: 3px;
  font-size: 12px;
  font-weight: 900;
  transition: .3s;
}

.rad-input:checked~.rad-text {
  color: hsl(0, 0%, 40%);
}

</style>