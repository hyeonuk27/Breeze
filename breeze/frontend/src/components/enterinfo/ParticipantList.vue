<template>
  <div class="participant-list">
    <Participant
      v-for="(participant, idx) in participants"
      :key="idx"
      :idx="idx"
      :participant="participant"
    />
  </div>
</template>

<script>
import Participant from "@/components/enterinfo/Participant"
import { mapGetters } from "vuex"

export default {
  name: "ParticipantList",
  components: {
    Participant,
  },
  data() {
    return {}
  },
  computed: {
    ...mapGetters(["participants"]),
  },
}
</script>

<style>
.participant-list {
  width: 88%;
  margin: auto;
  overflow-y: scroll;
}
</style>