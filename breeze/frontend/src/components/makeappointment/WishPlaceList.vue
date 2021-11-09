<template>
  <div>
    <WishPlace/>
  </div>
</template>

<script>
import WishPlace from '@/components/makeappointment/WishPlace.vue'

export default {
  name: 'WishPlaceList',
  components: {
    WishPlace,
  },
  props: {
    wishPlaces: Array,
  }

}
</script>

<style>

</style>