<template>
  <button
    type="button"
    class="btn btn-primary"
    @click="goToFindPlace()"
    >약속 계획 짜기
    </button>
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

<style>

</style>