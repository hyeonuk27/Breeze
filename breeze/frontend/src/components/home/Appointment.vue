<template>
  <div @mouseup="moveToAppointmentNote" class="appointment" :style="[isDday ? {background:'#B8D0FA'} : {background:'#EBECCA'}]">
  <button @mousedown="deleteAppointment(appointment.appointment_id)">x</button>
    <div class="appointment-info">{{appointment.datetime}} {{appointment.middle_place}}</div>
    <div class="appointment-d-day"><div class="test">D-{{appointment.d_day}}</div></div>
  </div>
</template>

<script>
import appointmentApi from "@/api/appointment.js";

export default {
  name: 'Appointment',
  props: {
  appointment: Object,
  },
  data() {
    return {
      isDday: false,
    }
  },
  methods: {
    moveToAppointmentNote: function () {
      this.$router.push({
        name: 'MakeAppointment',
        params: {
          noteId: this.appointment.appointment_id 
        },
      })
    },
    async deleteAppointment(noteId) {
      let accessToken = sessionStorage.getItem("access-token");
      let refreshToken = sessionStorage.getItem("refresh-token");
      let data = {
        noteId,
      };
      await appointmentApi.deleteAppointment(data, {
        "access-token": accessToken,
        "refresh-token": refreshToken,
      });
      this.$emit("get-appointmentlist");
      console.log('삭제')
    }
  },
  created() {
    if (this.appointment.d_day == 0) {
      this.isDday = true
    }
  }
} 
</script>

<style>
.appointment {
  height: 31%;
  padding: 7%;
  margin-right: 2%;
  margin-bottom: 3%;
  display: flex;
  justify-content: space-around;
  align-items: center;
  border-radius: 15px;
}
.appointment-info {
  text-align: start;
  color: #7b6f72;
  font-size: 13px;
}
.appointment-d-day {
  height: 55px;
  width: 55px;
  position: relative;
  background: rgba(256, 256, 256, 0.5);
  border-radius: 70%;
  font-size: 14px;
  font-weight: 700;
  color: rgb(80, 79, 79);
}
.test {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);

}
button {
  z-index: 100;
}


</style>