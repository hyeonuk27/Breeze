<template>
  <div class="home">
    <Profile :appointmentCnt="appointmentCnt" class="my-profile" />
    <AppointmentList @set-info="setInfo" class="my-appointment-list" />
  </div>
</template>

<script>
import Profile from "@/components/home/Profile";
import AppointmentList from "@/components/home/AppointmentList";

export default {
  name: "Home",
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

<style>
.home {
  padding: 8%;
}
.my-profile {
  height: 30%;
  background: rgb(235, 239, 254);
}
.my-appointment-list {
  height: 66%;
}
</style>