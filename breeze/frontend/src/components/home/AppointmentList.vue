<template>
  <div class="appointment-list-items">
    <div v-if="appointmentList.length == 0">
      <div class="nothing">
        <div>예정된 약속이 없습니다.</div>
        <div>바라미들과 즐거운 약속을 만들어보세요!</div>
      </div>
      <img class="nothing-image" src="@/assets/barami/baramis.png" alt="" />
    </div>
    <Appointment
      v-for="(appointment, idx) in appointmentList"
      :key="idx"
      :appointment="appointment"
    />
  </div>
</template>

<script>
import Appointment from "@/components/home/Appointment"
import appointmentApi from "@/api/appointment.js"
import { mapActions, mapGetters } from "vuex"

export default {
  name: "AppointmentList",
  components: {
    Appointment,
  },
  data() {
    return {
      isDday: false,
      isDeleted: false,
      appointmentCnt: 0,
      appointmentList: [],
    }
  },
  methods: {
    ...mapActions(["setIsAppointmentDeleted"]),
    async getAppointmentList() {
      const response = await appointmentApi.getAppointmentList()
      this.appointmentList = response.my_appointment

      for (let i = 0; i < this.appointmentList.length; i++) {
        var data = this.appointmentList[i].datetime
        const date =
          data.substr(0, 4) + "년 " + data.substr(5, 2) + "월 " + data.substr(8, 2) + "일 "
        var localDate = new Date(data)
        const local = localDate.toString()
        const cal =
          date + local.substr(16, 2) + "시 " + local.substr(19, 2) + "분"
        this.appointmentList[i].datetime = cal
      }

      this.appointmentCnt = this.appointmentList.length
      this.$emit("set-info", this.appointmentCnt)
      this.setIsAppointmentDeleted(false)
    },
  },
  created() {
    this.getAppointmentList()
  },
  computed: {
    ...mapGetters(["isAppointmentDeleted"]),
  },
  watch: {
    isAppointmentDeleted() {
      this.getAppointmentList()
    },
  },
}
</script>

<style>
.appointment-list-items {
  margin-top: 6%;
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