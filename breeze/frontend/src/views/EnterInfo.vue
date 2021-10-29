<template>
  <div>
    <ChooseDate/>
    <AddFriends/>
    <ParticipantList class="participant-list"/>
    <FindMiddleBtn/>
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
.participant-list {
  height: 38%;
}
</style>