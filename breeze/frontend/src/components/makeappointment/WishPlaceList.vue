<template>
  <div class="wish-place-container">
    <div class="wish-places">
      <WishPlace v-for="(place, idx) in wishPlaces" :key="idx" :place="place" />
    </div>
  </div>
</template>

<script>
import WishPlace from "@/components/makeappointment/WishPlace.vue"

export default {
  name: "WishPlaceList",
  components: {
    WishPlace,
  },
  props: {
    wishPlaces: Array,
  },
}
</script>

<style scoped>
.wish-place-container {
  padding-top: 3%;
  padding-bottom: 3%;
}
.wish-places {
  height: 100%;
  overflow-y: scroll;
}
</style>