<template>
  <div>
    <Participants
      v-if="this.noteInfo"
      class="participants"
      :noteParticipants="noteInfo.participants"
    />
    <AppointmentDate
      v-if="this.noteInfo"
      class="appointment-date"
      :datetime="noteInfo.datetime"
      :middlePlace="noteInfo.middle_place"
    />
    <WishPlaceList 
      v-if="this.noteInfo" 
      class="wish-place-list" 
      :wishPlaces="noteInfo.places" 
    />
    <div v-if="this.noteInfo" class="btn-group">
      <Buttons :isFirst="isFirst" :noteInfo="noteInfo" />
    </div>
    <div
      class="modal fade"
      id="rememberModal"
      tabindex="-1"
      aria-labelledby="rememberModalLabel"
      aria-hidden="true"
    >
      <RememberModal />
    </div>
  </div>
</template>

<script>
import AppointmentDate from "@/components/makeappointment/AppointmentDate.vue"
import Buttons from "@/components/makeappointment/Buttons.vue"
import Participants from "@/components/makeappointment/Participants.vue"
import RememberModal from "@/components/makeappointment/RememberModal.vue"
import WishPlaceList from "@/components/makeappointment/WishPlaceList.vue"
import appointmentApi from "@/api/appointment.js"
import store from "@/store"
import { mapGetters } from "vuex"
import Swal from 'sweetalert2'

export default {
  name: "MakeAppointment",
  components: {
    AppointmentDate,
    Buttons,
    Participants,
    RememberModal,
    WishPlaceList,
  },
  data() {
    return {
      noteInfo: {},
      secretCode: "",
      userId: "",
    }
  },
  beforeRouteEnter(to, from, next) {
    store.dispatch("setMenu", 3)

    var isGroup
    if (store.getters.getGroupId == null) {
      isGroup = false
    } else {
      isGroup = true
    }
    const isFirst = store.getters.getIsFirst

    if (from.name == "FindPlace" && !isGroup) {
      store.dispatch("setIsFirst", true)
      store.dispatch("setIsGroupSaved", false)
      next()
    } else if (from.name == null && isFirst) {
      next()
    } else {
      store.dispatch("setIsFirst", false)
      next()
    }
  },
  methods: {
    async setInfo() {
      this.secretCode = this.$route.params.secretCode
      const response = await appointmentApi.getAppointment(this.secretCode)
      this.noteInfo = response
      if (response == '') {
        await Swal.fire({
          html: '<b>존재하지 않는 약속 쪽지입니다!</b>',
          imageUrl: 'https://ifh.cc/g/bYAc4j.png',
          imageWidth: 170,
          imageHeight: 170,
          imageAlt: 'Logo image',
          showConfirmButton: false,
          showCloseButton: true,
        })
        await this.$router.push('/')
      } else {
        const data = this.noteInfo.datetime
        const date = data.substr(0, 4) + "년 " + data.substr(5, 2) + "월 " + data.substr(8, 2) + "일 "
        var localDate = new Date(data)
        const local = localDate.toString()
        const cal = date + local.substr(16, 2) + "시 " + local.substr(19, 2) + "분"
        this.noteInfo.datetime = cal
        this.noteInfo.middle_place = this.noteInfo.middle_place+ '역'
      }
    },
  },
  created() {
    this.userId = this.$store.getters.getUserId
    this.setInfo()
  },
  computed: {
    ...mapGetters(["isFirst"]),
  },
}
</script>

<style scoped>
.appointment-date {
  padding-left: 8%;
  padding-right: 8%;
  height: 14%;
}
.btn-group {
  width: 100%;
  height: 14%;
}
.wish-place-list {
  padding-left: 8%;
  padding-right: 8%;
  height: 50%;
}
.participants {
  padding-left: 8%;
  padding-right: 8%;
  height: 22%;
}
</style>