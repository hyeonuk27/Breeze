<template>
  <div class="home-items">
    <Myprofile class="my-profile" />
    <MyAppointmentList class="my-appointment-list" />
  </div>
</template>

<script>
import Myprofile from '@/components/home/Myprofile'
import MyAppointmentList from '@/components/home/MyAppointmentList'

export default {
  name: 'Home',
  components: {
    Myprofile,
    MyAppointmentList,
  }
}
</script>

<style>
.home-items {
  padding: 8%;
}
.my-profile {
  height: 30%;
  background: rgb(235, 239, 254);
}
.my-appointment-list {
  height: 70%;
  background: rgb(245, 247, 190);
}
</style>