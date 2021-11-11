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
        // {
        // secret_code: 0,
        // datetime: '2021-10-28(목) 오후 1시',
        // middle_place: '신촌역',
        // d_day: 0
        // },
      ]
    }
  },
  methods: {
    async getAppointmentList() {
      const response = await appointmentApi.getAppointmentList();
      this.appointmentList = response.my_appointment
      this.appointmentCnt = this.appointmentList.length;
      this.$emit('set-info', this.appointmentCnt)	
    }
  },
  created() {
    this.getAppointmentList()
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
  font-size: 0.85rem;
  width: 100%;
  color: #7b6f72;
}
.nothing-image {
  position: absolute;
  top: 36%;
  left: 50%;  
  transform: translate(-50%, -50%);
  width: 48vw;
}
</style>