<template>
  <div class="home">
    <Profile :appointmentCnt="appointmentCnt" class="profile" />
    <AppointmentList @set-info="setInfo" class="appointment-list" />
  </div>
</template>

<script>
import Profile from "@/components/home/Profile";
import AppointmentList from "@/components/home/AppointmentList";

export default {
  name: 'Home',
  components: {
    Profile,
    AppointmentList,
  },
  data() {
    return {
      appointmentCnt: 0,
    };
  },
  methods: {
    setInfo(data) {
      this.appointmentCnt = data;
    },
  },
};
</script>

<style scoped>
  .home {
    padding: 8%;
  }
  .profile {
    height: 30%;
    background: rgb(235, 239, 254);
  }
  .appointment-list {
    height: 66%;
  }
</style>