<template>
  <div class="find-place-btn-items">
    <button type="button" class="find-place-btn" @click="goToFindPlace()">
      약속 계획 짜기
    </button>
  </div>
</template>

<script>
import { mapActions, mapGetters, mapState } from "vuex"

export default {
  name: "FindPlaceBtn",
  data() {
    return {
      partInfo: [],
    }
  },
  methods: {
    ...mapActions([
      "setMiddleName",
      "setMiddleLat",
      "setMiddleLong",
      "setPartMidTime",
    ]),
    async goToFindPlace() {
      const middleInfo = this.middleLists[this.middle]
      await this.concateArray(middleInfo)
      this.setMiddleName(middleInfo.name)
      this.setMiddleLat(middleInfo.latitude)
      this.setMiddleLong(middleInfo.longitude)
      this.setPartMidTime(this.partInfo)
      this.$router.push({ name: "FindPlace" })
    },
    concateArray(selectedMiddle) {
      this.partInfo = []
      for (let i = 0; i < selectedMiddle.participants.length; i++) {
        for (let j = 0; j < this.participants.length; j++) {
          if (
            selectedMiddle.participants[i].barami_type ===
            this.participants[j].baramiType
          ) {
            this.partInfo.push({
              baramiType: this.participants[j].baramiType,
              partName: this.participants[j].partName,
              time: selectedMiddle.participants[i].time,
            })
          }
        }
      }
    },
  },
  computed: {
    ...mapState({
      middle: (state) => state.mode.middle,
    }),
    ...mapGetters(["participants", "middleLists"]),
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