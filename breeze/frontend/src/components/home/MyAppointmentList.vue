<template>
  <div>
    <MyAppointment />
  </div>
</template>

<script>
import MyAppointment from '@/components/home/MyAppointment'
import appointmentApi from "@/api/appointment.js";

export default {
  name: 'MyAppointmentList',
  components: {
    MyAppointment,
  },
  data() {
    return {
      myAppointmentList: []
    }
  },
  methos: {
    async getMyAppointmentList() {
      let accessToken = sessionStorage.getItem("access-token");
      let refreshToken = sessionStorage.getItem("refresh-token");
      let result = await appointmentApi.getMyAppointmentList({
        "access-token": accessToken,
        "refresh-token": refreshToken,
      });
      this.myAppointmentList = result;
    }
  }
}
</script>

<style>

</style>