<template>
  <div class="enter-info">
    <ChooseDate/>
    <AddFriends/>
    <Participant/>
    <FindMiddleBtn/>
  </div>
</template>

<script>
import ChooseDate from '@/components/enterinfo/ChooseDate.vue'
import AddFriends from '@/components/enterinfo/AddFriends.vue'
import Participant from '@/components/enterinfo/Participant.vue'
import FindMiddleBtn from '@/components/enterinfo/FindMiddleBtn.vue'

export default {
  name: 'EnterInfo',
  components: {
    ChooseDate,
    AddFriends,
    Participant,
    FindMiddleBtn,
  }
}
</script>

<style scoped>
.enter-info {
  display: grid;
}
</style>