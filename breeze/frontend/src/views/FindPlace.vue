<template>
  <div class="find-place">
    <PlaceMap class="place-map" />
    <WishPlaceList class="wish-place-list" />
    <MakeAppointmentBtn class="make-appointment-btn" />
  </div>
</template>

<script>
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
}
</script>

<style scoped>

.place-map {
  height: 65%;
    background: rgb(22, 47, 138);
}
.wish-place-list {
  height: 21%;
  background: rgb(235, 239, 254);
}
.make-appointment-btn {
  height: 14%;
}
</style>