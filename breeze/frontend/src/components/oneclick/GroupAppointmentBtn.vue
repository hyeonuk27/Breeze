<template>
  <button
    type="button"
    class="btn group-appointment-btn"
    >이 모임으로 약속 만들기</button>
</template>

<script>
export default {
  name: 'GroupAppointmentBtn'
}
</script>

<style scoped>
.group-appointment-btn {
  background: linear-gradient(to left, #92A3FD, #9DCEFF);
  border: none;
  border-radius: 20px;
  padding: 3%;
  width: 60%;
  box-shadow: 1px 1px 5px 0px gray;
  color: white;
}
</style>