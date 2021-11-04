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

export default {
  name: 'EnterInfo',
  components: {
    ChooseDate,
    AddFriends,
    ParticipantList,
    FindMiddleBtn,
  }
}
</script>

<style scoped>
.enterinfo {
  padding: 8%;
}
.choose-date {
  height: 16%;
}
.add-friends {
  height: 30%;
  margin-top: 4%;
}
.participant-list {
  height: 45%;
  margin-top: 4%;
}
.find-middle-btn {
  height: 14%;
  margin-top: 4%;
}
</style>