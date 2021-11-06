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

export default {
  name: 'FindMiddleBtn',
  props: {
    middlePlaces: Array
  },
  data() {
    return {
      middleList: this.middlePlaces,
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
    async goToFindPlace() {
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