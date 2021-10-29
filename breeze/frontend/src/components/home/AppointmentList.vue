<template>
  <div>
    <Appointment />
  </div>
</template>

<script>
import Appointment from '@/components/home/Appointment'
import appointmentApi from "@/api/appointment.js";

export default {
  name: 'AppointmentList',
  components: {
    Appointment,
  },
  data() {
    return {
      appointmentList: []
    }
  },
  methos: {
    async getMyAppointmentList() {
      let accessToken = sessionStorage.getItem("access-token");
      let refreshToken = sessionStorage.getItem("refresh-token");
      let result = await appointmentApi.getAppointmentList({
        "access-token": accessToken,
        "refresh-token": refreshToken,
      });
      this.appointmentList = result;
    }
  }
}
</script>

<style>

</style>