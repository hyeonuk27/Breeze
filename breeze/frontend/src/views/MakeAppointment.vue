<template>
  <div class="note">
    <Participants 
      class="participants"
      :noteParticipants="noteInfo.participants"/>
    <AppointmentDate 
      class="appointment-date"
      :datetime="noteInfo.datetime"
      :middlePlace="noteInfo.middle_place"/>
    <WishPlaceList 
      class="wish-place-list"
      :wishPlaces="noteInfo.places"/>
    <div v-if="this.userId" class="btn-group">
      <Buttons 
      :isFirst="isFirst"
      :noteInfo="noteInfo"/>
    </div>
    <div 
      class="modal fade" 
      id="rememberModal" 
      tabindex="-1" 
      aria-labelledby="rememberModalLabel" 
      aria-hidden="true">      
      <RememberModal/>
    </div>
  </div>
</template>

<script>
import Participants from '@/components/makeappointment/Participants.vue'
import AppointmentDate from '@/components/makeappointment/AppointmentDate.vue'
import WishPlaceList from '@/components/makeappointment/WishPlaceList.vue'
import Buttons from '@/components/makeappointment/Buttons.vue'
import RememberModal from '@/components/makeappointment/RememberModal.vue'
// import appointmentApi from '@/api/appointment.js'
import store from "@/store"
import { mapGetters } from 'vuex'

export default {
  name: 'MakeAppointment',
  components: {
    Participants,
    AppointmentDate,
    WishPlaceList,
    Buttons,
    RememberModal
  },
  data() {
    return {
      userId: '',
      secretCode : '',
      // noteInfo: {},
      noteInfo: {
        participants: [
          {
            name: '지미짐',
            time: 30,
            barami_type: 0
          },
          {
            name: '수빙수',
            time: 30,
            barami_type: 2
          },
          {
            name: '라라라라라라',
            time: 30,
            barami_type: 4
          },
          {
            name: '현욱킴',
            time: 30,
            barami_type: 5
          },
          {
            name: '채니챈',
            time: 30,
            barami_type: 3
          },
          {
            name: '교저스',
            time: 30,
            barami_type: 1
          },
        ],
      datetime: '2021-11-26T14:12:09.268Z',
      middle_place: '역삼역',
      places: [
        {
          name: '가게1dddddddddd',
          category: 0,
          url: 'https://www.naver.com/'
        },
        {
          name: '가게2',
          category: 0,
          url: ''
        },
        {
          name: '가게3',
          category: 2,
          url: ''
        },
        {
          name: '가게4',
          category: 1,
          url: ''
        },
        {
          name: '가게5',
          category: 2,
          url: ''
        },
        {
          name: '가게6',
          category: 0,
          url: ''
        },
      ]

      }
    }
  },
  beforeRouteEnter(to, from, next) {
    var isGroup
    if (store.getters.getGroupId == null) {
      isGroup = false
    } else {
      isGroup = true
    }
    // console.log(isGroup, '그룹아이디 유무 확인')
    const isFirst = store.getters.getIsFirst

    if (from.name == 'FindPlace' && !isGroup) {
      // console.log('findplace에서 온다')
      store.dispatch('setIsFirst', true)
      store.dispatch('setIsGroupSaved', false)
      next()
    } else if (from.name == null && isFirst) {
      // console.log('findplace에서 왔는데 새로고침한 경우')
      next()
    }
    else {
      // console.log('홈에서 바로 오거나 그룹으로 온 경우')
      store.dispatch('setIsFirst', false)
      next()
    }
  },
  methods: {
    async setInfo () {
      console.log('$$$$$$$$$$$$$$$$$$$$$$$$$')
      this.secretCode = this.$route.params.secretCode
      console.log(this.secretCode, '노트아이디 확인')
      // const response = await appointmentApi.getAppointment(this.secretCode)
      // console.log(response)
      // this.noteInfo = response
      console.log(this.noteInfo)
    }

  },
  created() {
    this.userId = this.$store.getters.getUserId
    this.setInfo() 
  },
  computed: {
  ...mapGetters([
    'isFirst',
  ])
  }

}
</script>

<style scoped>
/* .note {

} */
.participants {
  padding-left: 8%;
  padding-right: 8%;
  height: 22%; 
}
.appointment-date {
  padding-left: 8%;
  padding-right: 8%;
  height: 14%;
}
.wish-place-list {
  padding-left: 8%;
  padding-right: 8%;
  height: 50%;
}
.btn-group {
  width:100%;
  height: 14%
}
</style>