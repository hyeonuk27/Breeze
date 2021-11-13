<template>
  <div>
    <Introduction class="introduction" />
    <GroupList class="group-list" />
    <GroupAppointmentBtn
      v-if="this.groupId"
      class="group-appointment-btn"
      data-bs-toggle="modal"
      data-bs-target="#groupAppointmentModal"
    />
    <GroupAppointmentBtn2 v-if="!this.groupId" class="group-appointment-btn" />
    <div
      class="modal fade"
      id="groupAppointmentModal"
      data-bs-backdrop="static"
      tabindex="-1"
      aria-labelledby="groupAppointmentModalLabel"
      aria-hidden="true"
    >
      <GroupAppointmentModal />
    </div>
  </div>
</template>

<script>
import Introduction from "@/components/oneclick/Introduction.vue"
import GroupAppointmentBtn from "@/components/oneclick/GroupAppointmentBtn.vue"
import GroupAppointmentBtn2 from "@/components/oneclick/GroupAppointmentBtn2.vue"
import GroupAppointmentModal from "@/components/oneclick/GroupAppointmentModal.vue"
import GroupList from "@/components/oneclick/GroupList.vue"
import { mapGetters } from "vuex"

export default {
  name: "OneClick",
  components: {
    Introduction,
    GroupAppointmentBtn,
    GroupAppointmentBtn2,
    GroupAppointmentModal,
    GroupList,
  },
  data() {
    return {
      isModalOpen: false,
    }
  },
  methods: {
    closeModal() {
      this.isModalOpen = false
    },
    openModal() {
      this.isModalOpen = true
    },
  },
  computed: {
    ...mapGetters(["groupId"]),
  },
}
</script>

<style scoped>
.group-appointment-btn {
  height: 14%;
}
.group-list {
  height: 67%;
  margin-top: 4%;
  display: flex;
  align-items: center;
  justify-content: center;
}
.introduction {
  height: 15%;
}
</style>