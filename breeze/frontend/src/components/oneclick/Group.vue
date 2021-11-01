<template>
  <div>
    <!-- {{ group }} -->
    <div>{{ group.group_name }}</div>
    <div
    v-for="(member, idx) in group.group_members"
    :key="idx">
      {{ idx }} {{ member }}
    </div>
  </div>
</template>

<script>
export default {
  name: 'Group',
  props: {
    group: Object,
    idx: Number,
  },

}
</script>

<style>

</style>