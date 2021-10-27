<template>
  <div>
    <div
      v-for="(part, idx) in participants"
      :key="idx"
      >
      {{ part }}
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'Participant',
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

</style>