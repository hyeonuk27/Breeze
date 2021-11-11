<template>
  <div class="participant-list">
    <Participant
      v-for="(participant, idx) in participants"
      :key="idx"
      :idx="idx"
      :participant="participant" />
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import Participant from '@/components/enterinfo/Participant'

export default {
  name: 'ParticipantList',
  components: {
    Participant
  },
  data () {
    return {
    }
  },
  computed: {
    ...mapGetters([
      'participants'
    ])
  }
}
</script>

<style>
.participant-list {
  /* margin: 4%; */
  width: 88%;
  margin: auto;
  overflow-y: scroll;
}
</style>