<template>
  <div class="home">
    <Profile :appointmentCnt="appointmentCnt" class="profile" />
    <AppointmentList @set-info="setInfo" class="appointment-list" />
  </div>
</template>

<script>
import AppointmentList from "@/components/home/AppointmentList"
import Profile from "@/components/home/Profile"

export default {
  name: "Home",
  components: {
    AppointmentList,
    Profile,
  },
  data() {
    return {
      appointmentCnt: 0,
    }
  },
  methods: {
    setInfo(data) {
      this.appointmentCnt = data
    },
  },
}
</script>

<style scoped>
.appointment-list {
  height: 66%;
}
.home {
  padding: 8%;
}
.profile {
  height: 30%;
  background: rgb(235, 239, 254);
}
</style>