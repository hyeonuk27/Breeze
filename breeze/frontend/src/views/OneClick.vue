<template>
  <div>
    <Introduction/>
    <GroupList/>
    <GroupAppointmentBtn/>
    <GroupAppointmentModal/>
  </div>
</template>

<script>
import Introduction from '@/components/oneclick/Introduction.vue'
import GroupList from '@/components/oneclick/GroupList.vue'
import GroupAppointmentBtn from '@/components/oneclick/GroupAppointmentBtn.vue'
import GroupAppointmentModal from '@/components/oneclick/GroupAppointmentModal.vue'

export default {
  name: 'OneClick',
  components: {
    Introduction,
    GroupList,
    GroupAppointmentBtn,
    GroupAppointmentModal
  }
}
</script>

<style>

</style>