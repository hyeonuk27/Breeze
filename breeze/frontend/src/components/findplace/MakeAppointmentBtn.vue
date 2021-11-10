<template>
  <div class="make-appointment-btn-items">
    <button
      type="button"
      @click="goToMakeAppointment()"
    >
      약속 쪽지 만들러 가기
      <img
        src="@/assets/common/arrow.png"
        alt="arrow-image"
      />
    </button>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import mapApi from '@/api/map.js'
export default {
  name: "MakeAppointmentBtn",
  methods: {
    async saveAppointment() {
      const data = {
        dateTime: this.date,
        middlePlace: this.middleName,
        participants: this.partMiddleTime,
        places: this.wishPlaces,
      }
      console.log(data)
      const response = await mapApi.saveAppointment(data)
      console.log(response, '노트 아이디 받음')
    },
    goToMakeAppointment: function () {
      if ( this.wishPlaces.length == 0 ) {
        alert('한 개 이상의 장소를 선택하세요.')
      } else {
        this.saveAppointment()
        this.$router.push({ name: "MakeAppointment" });
      }
    },
  },
  computed: {
    ...mapGetters([
      'date',
      'middleName',
      'partMiddleTime',
      'wishPlaces',
    ]),
  },
  created() {
    console.log(this.date)
    console.log(this.participants)
  }
};
</script>

<style>
.make-appointment-btn-items {
  position: relative;
}
.make-appointment-btn-items button {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 65%;
  height: 65%;
  padding: 3%;
  background: linear-gradient(to left, #92a3fd, #9dceff);
  box-shadow: 1px 1px 5px 0px gray;
  border: none;
  border-radius: 20px;
  color: white;
  font-weight: 600;
}
.make-appointment-btn-items img {
  height: inherit;
  margin-left: 2%;
}
</style>