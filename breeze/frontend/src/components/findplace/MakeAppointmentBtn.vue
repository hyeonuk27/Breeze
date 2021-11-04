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
export default {
  name: "MakeAppointmentBtn",
  methods: {
    goToMakeAppointment: function () {
      this.$router.push({ name: "MakeAppointment" });
    },
  },
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