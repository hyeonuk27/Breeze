<template>
  <div
    @click="moveToAppointmentNote"
    class="appointment-items"
    :style="[isDday ? { background: '#B8D0FA' } : { background: '#EBECCA' }]"
  >
    <img
      onclick="event.cancelBubble = true;"
      @click="deleteAppointment(appointment.appointment_id)"
      class="deleteBtn"
      src="@/assets/common/close.png"
      alt="close button"
    />
    <div class="appointment-info">{{ appointment.datetime }}<div>
    </div>{{ appointment.middle_place }}</div>
    <div class="appointment-d-day">
      <div v-if="isDday" class="appointment-d-day-text">오늘</div>
      <div v-else class="appointment-d-day-text">D-{{ appointment.d_day }}</div>
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
.appointment-items {
  display: grid;
  grid-template-columns: 4fr 1fr 1fr;
  grid-template-rows: 1fr 4fr;
  height: 31.5%;
  padding: 5%;
  margin: 0 2% 3% 0;
  border-radius: 15px;
}
.appointment-info {
  grid-column-start: 1;
  grid-column-end: span 2;
  grid-row-start: 1;
  grid-row-end: span 2;
  align-self: center;
  margin-left: 5%;
  color: #7b6f72;
  font-size: 13px;
  text-align: start;
  letter-spacing: -0.5px;
}
.appointment-d-day {
  position: relative;
  grid-column-start: 2;
  grid-column-end: span 2;
  grid-row-start: 1;
  grid-row-end: span 2;
  align-self: center;
  justify-self: end;
  height: 50px;
  width: 50px;
  margin: 5% 15% 0 0;
  border-radius: 70%;
  background: rgba(256, 256, 256, 0.5);
  color: rgb(80, 79, 79);
  font-size: 13px;
  font-weight: 700;
}
.appointment-d-day-text {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
.deleteBtn {
  grid-column: 3;
  grid-row: 1;
  justify-self: end;
  height: 10px;
  width: 10px;
}
</style>