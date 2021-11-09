<template>
  <div>
    <!-- <div v-for="(part, idx) in noteParticipants" :key="idx">
      {{ part.name }}
    </div> -->
    <!-- {{noteParticipants}} -->
  </div>
</template>

<script>
export default {
  name: 'Participants',
  props: {
    noteParticipants: Array,
  }

}
</script>

<style>

</style>