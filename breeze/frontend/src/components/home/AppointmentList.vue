<template>
  <div class="appointment-list">
    <Appointment 
      v-for="(appointment, idx) in appointmentList"
      :key="idx"
      :appointment="appointment"
      @get-notebooklist="getAppointmentList"
    />
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
      isDday: false,
      appointmentList: 
      [
        {
        appointment_id: 0,
        datetime: '2021-10-28(목) 오후 1시',
        middle_place: '신촌역',
        d_day: 0
        },
        {
        appointment_id: 1,
        datetime: '2021-10-29(금) 오후 7시',
        middle_place: '강남역',
        d_day: 1
        },
        {
        appointment_id: 2,
        datetime: '2021-10-30(토) 오후 2시',
        middle_place: '등촌역',
        d_day: 2
        },
        {
        appointment_id: 3,
        datetime: '2021-11-01(일) 오전 11시',
        middle_place: '서울역',
        d_day: 3
        },
      ]
    }
  },
  methos: {
    async getAppointmentList() {
      let accessToken = sessionStorage.getItem("access-token");
      let refreshToken = sessionStorage.getItem("refresh-token");
      let result = await appointmentApi.getAppointmentList({
        "access-token": accessToken,
        "refresh-token": refreshToken,
      });
      this.appointmentList = result;
    }
  },
  created() {
    this.getAppointmentList()
  }
}
</script>

<style>
.appointment-list {
  margin-top:6%;
  overflow-y: scroll;
}
</style>