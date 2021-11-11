<template>
  <div class="find-place-btn-items" >
    <button
      type="button"
      class="find-place-btn"
      @click="goToFindPlace()"
      >약속 계획 짜기
      </button>
  </div>
</template>

<script>
import { mapState, mapGetters, mapActions } from 'vuex'
import mapApi from '@/api/map.js'

export default {
  name: 'FindPlaceBtn',
  data() {
    return {
      middleList: [],
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
    findMiddle(modeIdx, middleIdx) {
      this.modeList = []
      for (let i = 0; i < this.middleList.length; i++) {
        if (this.middleList[i].middle_place_type === modeIdx) {
          this.modeList.push(this.middleList[i])
        }
      }
      return this.modeList[middleIdx]
    },
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
    async setInfo() {
      // console.log('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
      const cnt = this.participants.length
      const data = []
      for (let i = 0; i < cnt; i++) {
        const part = {
          baramiType: this.participants[i].baramiType,
          partLatitude: this.participants[i].partLatitude,
          partLongitude: this.participants[i].partLongitude
        }
      data.push(part)
      }
      // console.log(data, '내가 axios에 data로 담아 보내는 정보. 버튼')
      const response = await mapApi.middle(data)
      // console.log(response.middle_data, '중간 장소 관련 data들이 넘어온다. 버튼')
      this.middleList = response.middle_data
      // console.log(this.middleList, '마지막 확인')
      // console.log('**************************')
    },
    async goToFindPlace() {
      // console.log('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
      const middleInfo = await this.findMiddle(this.mode, this.middle)
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
    mode: state => state.mode.mode1,
    middle: state => state.mode.middle,
  }),
  ...mapGetters([
    'participants'
  ])
},
created() {
  this.setInfo()
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

</style>