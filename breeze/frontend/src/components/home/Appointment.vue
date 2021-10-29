<template>
  <div
    @mouseup="moveToAppointmentNote"
    class="appointment"
    :style="[isDday ? { background: '#B8D0FA' } : { background: '#EBECCA' }]"
  >
    <div
      class="deleteBtn"
      @mousedown="deleteAppointment(appointment.appointment_id)"
    >
      x
    </div>
    <div class="appointment-info">
      {{ appointment.datetime }}
      <div></div>
      {{ appointment.middle_place }}
    </div>
    <div class="appointment-d-day">
      <div class="test">D-{{ appointment.d_day }}</div>
    </div>
  </div>
</template>

<script>
import appointmentApi from "@/api/appointment.js";

export default {
  name: "Appointment",
  props: {
    appointment: Object,
  },
  data() {
    return {
      isDday: false,
    };
  },
  methods: {
    moveToAppointmentNote: function () {
      this.$router.push({
        name: "MakeAppointment",
        params: {
          noteId: this.appointment.appointment_id,
        },
      });
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
      console.log("삭제");
    },
  },
  created() {
    if (this.appointment.d_day == 0) {
      this.isDday = true;
    }
  },
};
</script>

<style scoped>
.appointment {
  display: grid;
  grid-template-columns: 4fr 1fr 1fr;
  grid-template-rows: 1fr 4fr;
  height: 31.5%;
  padding: 2% 5%;
  margin: 0 2% 3% 0;
  border-radius: 15px;
}
.appointment-info {
  grid-column-start: 1;
  grid-column-end: span 2;
  grid-row-start: 1;
  grid-row-end: span 2;
  align-self: center;
  text-align: start;
  color: #7b6f72;
  font-size: 13px;
  margin-left: 5%;
  letter-spacing: -0.5px
}
.appointment-d-day {
  margin-right: 15%;
  grid-column-start: 2;
  grid-column-end: span 2;
  grid-row-start: 1;
  grid-row-end: span 2;
  align-self: center;
  justify-self: end;
  height: 50px;
  width: 50px;
  position: relative;
  background: rgba(256, 256, 256, 0.5);
  border-radius: 70%;
  font-size: 13px;
  font-weight: 700;
  color: rgb(80, 79, 79);
}
.test {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
.deleteBtn {
  z-index: 100;
  grid-column: 3;
  grid-row: 1;
  text-align: end;
}
</style>