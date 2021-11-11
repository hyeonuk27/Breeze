<template>
  <div class="one-click">
    <Introduction class="introduction" />
    <GroupList class="group-list d-flex align-items-center justify-content-center" />
    <GroupAppointmentBtn
      v-if="this.groupId"
      class="group-appointment-btn"
      data-bs-toggle="modal" data-bs-target="#groupAppointmentModal"
    />
    <GroupAppointmentBtn2
      v-if="!this.groupId"
      class="group-appointment-btn"
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
import GroupAppointmentBtn2 from '@/components/oneclick/GroupAppointmentBtn2.vue'
import GroupAppointmentModal from '@/components/oneclick/GroupAppointmentModal.vue'
import { mapGetters } from 'vuex'

export default {
  name: 'OneClick',
  components: {
    Introduction,
    GroupList,
    GroupAppointmentBtn,
    GroupAppointmentBtn2,
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
  },
  computed: {
    ...mapGetters([
      'groupId',
    ])
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
  height: 9%;
}
.group-list {
  /* margin: auto 0%; */
  height: 80%;
  margin-top: 5%;
}
.group-appointment-btn {
  height: 14%;
}
</style>