<template>
  <div class="group-appointment-btn">
    <button type="button" @click="goToEnterInfo()">새 약속 만들러가기</button>
  </div>
</template>

<script>
import { mapActions } from "vuex"

export default {
  name: "GroupAppointmentBtn2",
  methods: {
    ...mapActions(["setMenu"]),
    goToEnterInfo() {
      this.$router.push({ name: "EnterInfo" })
      this.setMenu(1)
    },
  },
}
</script>

<style scoped>
.group-appointment-btn {
  position: relative;
}
.group-appointment-btn button {
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