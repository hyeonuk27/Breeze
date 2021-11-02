<template>
  <div class="find-place">
    <Map class="map" />
    <WishPlaceList class="wish-place-list" />
    <MakeAppointmentBtn class="make-appointment-btn" />
  </div>
</template>

<script>
import Map from "@/components/findplace/Map";
import WishPlaceList from "@/components/findplace/WishPlaceList";
import MakeAppointmentBtn from "@/components/findplace/MakeAppointmentBtn";

export default {
  name: 'FindPlace',
  components: {
    Map,
    WishPlaceList,
    MakeAppointmentBtn
  },
}
</script>

<style scoped>

.map {
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