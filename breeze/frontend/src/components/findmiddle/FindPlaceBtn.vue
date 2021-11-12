<template>
  <div class="find-place-btn-items" >
    <button
      type="button"
      class="find-place-btn"
      @click="goToFindPlace()"
      >약속 계획 짜기
    </button>
  </div>
  <!-- <div v-else>
    <div class="spinner">
      <div class="bounce bounce1"></div>
      <div class="bounce bounce2"></div>
      <div class="bounce bounce3"></div>
    </div>
  </div> -->
</template>

<script>
import { mapState, mapGetters, mapActions } from 'vuex'
// import mapApi from '@/api/map.js'

export default {
  name: 'FindPlaceBtn',
  data() {
    return {
      // middleList: [],
      modeList: [],
      partInfo: [],
    }
  },
  methods: {
     ...mapActions([
      'setPartMidTime',
      'setMiddleName',
      'setMiddleLat',
      'setMiddleLong',
    ]),
    // findMiddle(modeIdx, middleIdx) {
    //   this.modeList = []
    //   for (let i = 0; i < this.middleList.length; i++) {
    //     if (this.middleList[i].middle_place_type === modeIdx) {
    //       this.modeList.push(this.middleList[i])
    //     }
    //   }
    //   return this.modeList[middleIdx]
    // },
    concateArray(selectedMiddle) {
      this.partInfo = []
      for (let i = 0; i < selectedMiddle.participants.length; i++) {
        for (let j = 0; j < this.participants.length; j++) {
          if (selectedMiddle.participants[i].barami_type === this.participants[j].baramiType) {
            this.partInfo.push({
              "baramiType": this.participants[j].baramiType,
              "partName": this.participants[j].partName,
              "time": selectedMiddle.participants[i].time
            })
          }
        }
      }
    },
    // async setInfo() {
    //   // console.log('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    //   const cnt = this.participants.length
    //   const data = []
    //   for (let i = 0; i < cnt; i++) {
    //     const part = {
    //       baramiType: this.participants[i].baramiType,
    //       partLatitude: this.participants[i].partLatitude,
    //       partLongitude: this.participants[i].partLongitude
    //     }
    //   data.push(part)
    //   }
    //   // console.log(data, '내가 axios에 data로 담아 보내는 정보. 버튼')
    //   const response = await mapApi.middle(data)
    //   // console.log(response.middle_data, '중간 장소 관련 data들이 넘어온다. 버튼')
    //   this.middleList = response.middle_data
    //   // console.log(this.middleList, '마지막 확인')
    //   // console.log('**************************')
    // },
    async goToFindPlace() {
      // console.log('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
      // const middleInfo = await this.findMiddle(this.mode, this.middle)
      const middleInfo = this.middleLists[this.middle]
      await this.concateArray(middleInfo)
      this.setMiddleName(middleInfo.name)
      this.setMiddleLat(middleInfo.latitude)
      this.setMiddleLong(middleInfo.longitude)
      this.setPartMidTime(this.partInfo)
      this.$router.push({ name: 'FindPlace' })
    },

  },
  computed: {
    ...mapState({
    // mode: state => state.mode.mode1,
    middle: state => state.mode.middle,
  }),
  ...mapGetters([
    'participants',
    'middleLists',
  ])
},
created() {
  this.modeList = this.middleLists
  // this.setInfo()
}

}
</script>

<style scoped>
.find-place-btn-items {
  position: relative;
}
.find-place-btn-items .find-place-btn {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 65%;
  height: 65%;
  padding: 3%;
  background: linear-gradient(to left, #92a3fd, #9dceff);
  box-shadow: 1px 1px 5px 0px gray;
  border: none;
  border-radius: 20px;
  color: white;
  font-weight: 600;
}

.spinner {
  margin: -300px auto 0;
  width: 100px;
  text-align: center;
}

.spinner > div {
  width: 18px;
  height: 18px;
  background-color: #B8D0FA;
  border-radius: 100%;
  display: inline-block;
  -webkit-animation: sk-bouncedelay 1.4s infinite ease-in-out both;
  animation: sk-bouncedelay 1.4s infinite ease-in-out both;
}

.spinner .bounce1 {
  -webkit-animation-delay: -0.32s;
  animation-delay: -0.32s;
  margin-right: 10%;
}

.spinner .bounce2 {
  -webkit-animation-delay: -0.16s;
  animation-delay: -0.16s;
  margin-right: 10%;
}

@-webkit-keyframes sk-bouncedelay {
  0%, 80%, 100% { -webkit-transform: scale(0) }
  40% { -webkit-transform: scale(1.0) }
}

@keyframes sk-bouncedelay {
  0%, 80%, 100% { 
    -webkit-transform: scale(0);
    transform: scale(0);
  } 40% { 
    -webkit-transform: scale(1.0);
    transform: scale(1.0);
  }
}
</style>