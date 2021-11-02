<template>
  <div class="one-click">
    <Introduction class="introduction" />
    <GroupList class="group-list d-flex align-items-center" />
    <GroupAppointmentBtn
      class="group-appointment-btn"
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
.one-click {
  padding: 8%;
}
.introduction {
  /* padding: 5%; */
  /* margin: 1%; */
  height: 11%;
}
.group-list {
  /* margin: auto 0%; */
  height: 80%;
}
.group-appointment-btn {
  height: 14%;
}
</style>