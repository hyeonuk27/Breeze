<template>
  <div>
    <div class="wish-place-list-head">
      <img
        class="wish-place-list-image"
        src="@/assets/map/add2.png"
        alt="wish-place-list-image"
      />
      <div class="wish-place-list-title">약속 장소 후보</div>
    </div>

    <div v-if="wishPlaces.length == 0" class="wish-place-list-nothing">
      <img src="@/assets/barami/4.png" alt="" />
      <div>지도에서 원하는 약속 장소를 찾아보세요!</div>
    </div>
    <div v-if="wishPlaces" class="wish-place-list-body">
      <WishPlace
        v-for="(wishPlace, idx) in wishPlaces"
        :key="idx"
        :idx="idx"
        :wishPlace="wishPlace"
        class="wish-place"
      />
    </div>
  </div>
</template>

<script>
import WishPlace from "@/components/findplace/WishPlace"
import { mapGetters } from "vuex"

export default {
  name: "WishPlaceList",
  components: {
    WishPlace,
  },
  computed: {
    ...mapGetters(["wishPlaces"]),
  },
}
</script>

<style>
.wish-place {
  display: inline-block;
  height: 13vh;
  width: 13vh;
}
.wish-place-list-body {
  height: 80%;
  padding: 0 3%;
  text-align: start;
  overflow-x: scroll;
  white-space: nowrap;
  -ms-overflow-style: none;
}
.wish-place-list-body::-webkit-scrollbar {
  display: none;
}
.wish-place-list-head {
  position: relative;
  height: 20%;
  padding: 0 3%;
  text-align: start;
}
.wish-place-list-image {
  position: absolute;
  bottom: 4px;
  width: 13px;
}
.wish-place-list-nothing {
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 0 3.5vw;
  width: 93vw;
  height: 13vh;
  border-radius: 10px;
  border: solid 2px #e9edfe;
  /* background: #F8EED7; */
}
.wish-place-list-nothing div {
  font-size: 0.85rem;
  text-align: start;
}
.wish-place-list-nothing img {
  height: 7vh;
  padding: 1%;
}
.wish-place-list-title {
  position: absolute;
  bottom: 2px;
  left: 27px;
  color: #3a3c3c;
  font-size: 11px;
}
</style>
