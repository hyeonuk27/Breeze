<template>
  <div>
    <Introduction class="introduction" />
    <GroupList class="group-list" />
    <GroupAppointmentBtn
      data-bs-toggle="modal" data-bs-target="#groupAppointmentModal"
    />
    <div class="modal fade" id="groupAppointmentModal" tabindex="-1" aria-labelledby="groupAppointmentModalLabel" aria-hidden="true">      
      <GroupAppointmentModal/>
    </div>
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
  margin: 1%;
}
.group-list {
  height: 70%;
}
</style>