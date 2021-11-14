<template>
  <div class="find-place">
    <PlaceMap class="place-map" />
    <WishPlaceList class="wish-place-list" />
    <MakeAppointmentBtn class="make-appointment-btn" />
  </div>
</template>

<script>
import MakeAppointmentBtn from "@/components/findplace/MakeAppointmentBtn"
import PlaceMap from "@/components/findplace/PlaceMap"
import WishPlaceList from "@/components/findplace/WishPlaceList"
import store from "@/store"

export default {
  name: "FindPlace",
  components: {
    MakeAppointmentBtn,
    PlaceMap,
    WishPlaceList,
  },
  beforeRouteEnter(to, from, next) {
    if (from.name == "FindMiddle") {
      store.dispatch("setFilter", 0)
      store.dispatch("setMode2", 0)
      store.dispatch("setWishPlace", [])
      next()
    } else {
      next()
    }
  },
}
</script>

<style scoped>
.make-appointment-btn {
  height: 14%;
  background: rgba(233, 237, 252, 0.1);
}
.place-map {
  height: 64%;
}
.wish-place-list {
  height: 22%;
  background: rgba(233, 237, 252, 0.1);
}
</style>