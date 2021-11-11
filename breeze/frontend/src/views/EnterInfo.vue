<template>
  <div class="enterinfo">
    <ChooseDate class="choose-date"/>
    <AddFriends class="add-friends"/>
    <ParticipantList class="participant-list"/>
    <FindMiddleBtn class="find-middle-btn"/>
  </div>
</template>

<script>
import ChooseDate from '@/components/enterinfo/ChooseDate.vue'
import AddFriends from '@/components/enterinfo/AddFriends.vue'
import ParticipantList from '@/components/enterinfo/ParticipantList.vue'
import FindMiddleBtn from '@/components/enterinfo/FindMiddleBtn.vue'
import store from "@/store"

export default {
  name: 'EnterInfo',
  components: {
    ChooseDate,
    AddFriends,
    ParticipantList,
    FindMiddleBtn,
  },
  beforeRouteEnter(to, from, next) {
    var isGroup
    if (store.getters.getGroupId == null) {
      isGroup = false
    } else {
      isGroup = true
    }
    if (from.name == 'OneClick' || from.name == 'MakeAppointment' || isGroup ) {
      // console.log('oneclick에서 온다')
      store.dispatch('setDate', new Date())
      store.dispatch('setParticipants', [])
      store.dispatch('setPartMidTime', [])
      store.dispatch('setMiddleName', '')
      store.dispatch('setMiddleLat', 0)
      store.dispatch('setMiddleLong', 0)
      store.dispatch('setGroupName', '')
      store.dispatch('setGroupId', null)
      store.dispatch('setIsFirst', false)
      next()
    }  else {
      // console.log('정상적으로 진입한 경우')
      next()
    }
  },
}
</script>

<style scoped>
.enterinfo {
  /* padding-top: 2%; */
}
.choose-date {
  height: 11%;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  margin-bottom: 3%;
}
.add-friends {
  height: 26%;
  display: flex;
  flex-direction: column;
  justify-content: space-evenly;
  margin-bottom: 3%;
}
.participant-list {
  height: 43%;
}
.find-middle-btn {
  height: 14%;
}
</style>