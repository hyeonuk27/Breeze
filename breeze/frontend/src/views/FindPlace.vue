<template>
  <div class="find-place">
    <PlaceMap class="place-map" />
    <WishPlaceList class="wish-place-list" />
    <MakeAppointmentBtn class="make-appointment-btn" />
  </div>
</template>

<script>
import store from "@/store"
import PlaceMap from "@/components/findplace/PlaceMap";
import WishPlaceList from "@/components/findplace/WishPlaceList";
import MakeAppointmentBtn from "@/components/findplace/MakeAppointmentBtn";

export default {
  name: 'FindPlace',
  components: {
    PlaceMap,
    WishPlaceList,
    MakeAppointmentBtn
  },
  beforeRouteEnter(to, from, next) {
    if (from.name == 'FindMiddle') {
      store.dispatch('setMode2', 0)
      store.dispatch('setFilter', 0)
      store.dispatch('setWishPlace', [])
      next()
    } else {
      next()
    }
  }
} 
</script>

<style scoped>

.place-map {
  height: 64%;
    background: rgb(22, 47, 138);
}
.wish-place-list {
  height: 22%;
}
.make-appointment-btn {
  height: 14%;
}
</style>