<template>
  <div>
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
.my-profile {
  height: 30%;
}
.my-appointment-list {
  height: 70%;
}
</style>