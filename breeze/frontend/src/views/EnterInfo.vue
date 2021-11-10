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
  /* padding-top: 2%; */
}
.choose-date {
  height: 12%;
  display: flex;
  flex-direction: column;
  justify-content: center;
}
.add-friends {
  height: 25%;
  display: flex;
  flex-direction: column;
  justify-content: space-evenly;
  margin-bottom: 4%;
}
.participant-list {
  height: 45%;
}
.find-middle-btn {
  height: 14%;
}
</style>