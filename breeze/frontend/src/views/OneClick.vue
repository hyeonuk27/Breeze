<template>
  <div>
    <Introduction class="introduction" />
    <GroupList/>
    <GroupAppointmentBtn
      @openModal="openModal()"
    />
    <GroupAppointmentModal
      @closeModal="closeModal()"
    />
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
  },
  data () {
    return {
      isModalOpen: false,
    }
  },
  methods: {
    openModal() {
      this.isModalOpen = true
    },
    closeModal() {
      this.isModalOpen = false
    }
  }
}
</script>

<style scoped>
.introduction {
  padding: 5%;
}

</style>