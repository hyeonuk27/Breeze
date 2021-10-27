<template>
  <div>
    <Myprofile />
    <MyAppointmentList />
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

</style>