<template>
  <div class="appointment-list-items">
    <div v-if="appointmentList.length == 0">
    <div class="nothing"><div>예정된 약속이 없습니다.</div><div> 바라미들과 즐거운 약속을 만들어보세요!</div></div>
    <img class="nothing-image" src="@/assets/barami/baramis.png" alt="">
    </div>
    <Appointment 
      v-for="(appointment, idx) in appointmentList"
      :key="idx"
      :appointment="appointment"
      @get-appointmentlist="getAppointmentList"
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
      appointmentCnt: 0,
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
      this.appointmentCnt = result[0].length;
      this.$emit('set-info', this.appointmentCnt)	
    }
  },
  created() {
    this.getAppointmentList
  }
}
</script>

<style>
.appointment-list-items {
  margin-top:6%;
  overflow-y: scroll;
  position: relative;
}
.nothing {
  position: absolute;
  top: 50%;
  left: 50%;  
  transform: translate(-50%, -50%);
  font-size: 14px;
  width: 100%;
  color: #7b6f72;
}
.nothing-image {
  position: absolute;
  top: 38%;
  left: 50%;  
  transform: translate(-50%, -50%);
  width: 38%;
}
</style>