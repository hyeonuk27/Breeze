<template>
  <div
    @click="moveToAppointmentNote"
    class="appointment-items"
    :style="[isDday ? { background: '#B8D0FA' } : { background: '#EBECCA' }]"
  >
    <img
      onclick="event.cancelBubble = true;"
      @click="deleteAppointment(appointment.secret_code)"
      class="deleteBtn"
      src="@/assets/common/close.png"
      alt="close button"
    />
    <div class="appointment-info">
      {{ appointment.datetime.substr(2) }}<br>
      {{ appointment.middle_place }}
    </div>
    <div class="appointment-d-day">
      <div v-if="isDday" class="appointment-d-day-text">오늘</div>
      <div v-else class="appointment-d-day-text">D{{ appointment.d_day }}</div>
    </div>
  </div>
</template>

<script>
import appointmentApi from "@/api/appointment.js"
import { mapActions } from "vuex"
import Swal from "sweetalert2"

export default {
  name: "Appointment",
  props: {
    appointment: Object,
  },
  data() {
    return {
      isDday: false,
    }
  },
  methods: {
    ...mapActions(["setIsAppointmentDeleted", "setMenu"]),
    deleteAppointment(secret_code) {
      Swal.fire({
        html: "<b>정말 삭제하시겠습니까?</b>",
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#94B9F3",
        cancelButtonColor: "#FF91A4",
        confirmButtonText: "삭제",
        cancelButtonText: "취소",
      }).then(async (result) => {
        if (result.isConfirmed) {
          const data = {
            secretCode: secret_code,
          }
          const response = await appointmentApi.deleteAppointment(data)
          if (response == "success") {
            this.setIsAppointmentDeleted(true)
            Swal.fire({
              html: "<b>삭제되었습니다</b>",
              icon: "success",
              showConfirmButton: false,
              timer: 1500,
            })
          }
        }
      })
    },
    moveToAppointmentNote: function () {
      this.$router.push({
        name: "MakeAppointment",
        params: {
          secretCode: this.appointment.secret_code,
        },
      })
      this.setMenu(3)
    },
  },
  created() {
    if (this.appointment.d_day == 0) {
      this.isDday = true
    }
  },
}
</script>

<style scoped>
.appointment-d-day {
  position: relative;
  grid-column-start: 2;
  grid-column-end: span 2;
  grid-row-start: 1;
  grid-row-end: span 2;
  align-self: center;
  justify-self: end;
  height: 9.5vh;
  width: 9.5vh;
  margin: 5% 15% 0 0;
  border-radius: 70%;
  background: rgba(256, 256, 256, 0.5);
  color: rgb(80, 79, 79);
  font-weight: 700;
}
.appointment-d-day-text {
  width: 100%;
  font-size: 0.85rem;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
.appointment-info {
  grid-column-start: 1;
  grid-column-end: span 2;
  grid-row-start: 1;
  grid-row-end: span 2;
  align-self: center;
  margin-left: 5%;
  color: #7b6f72;
  font-size: 0.85rem;
  text-align: start;
  letter-spacing: -0.5px;
}
.appointment-items {
  display: grid;
  grid-template-columns: 4fr 1fr 1fr;
  grid-template-rows: 1fr 4fr;
  height: 31.5%;
  padding: 5%;
  margin: 0 2% 3% 0;
  border-radius: 15px;
}
.deleteBtn {
  grid-column: 3;
  grid-row: 1;
  justify-self: end;
  height: 1.5vh;
  width: 1.5vh;
}
</style>