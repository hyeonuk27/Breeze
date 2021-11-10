<template>
  <div class="wish-place-items" :style="{background: this.placeTypeColor[mode2]}">
    <img class="wish-place-delete-btn" @click="deleteWishPlace(idx)" src="@/assets/map/minus.png" alt="">
    <div class="wish-place-image-box">
      <img class="wish-place-image" :src="require('@/assets/map/' + mode2 + '.png')" alt="" />
    </div>
    <div class="wish-place-name">{{ placeName }}</div>
  </div>
</template>

<script>
import { mapActions } from "vuex";

export default {
  name: "WishPlace",
  props: {
    wishPlace: Object,
    idx: Number,
  },
  data() {
    return {
      mode2: 0,
      placeName:'',
      placeTypeColor: ["#ADA6AD", "#EBECCA", "#BFD5F8"],
    };
  },
  methods: {
    ...mapActions([
      'deleteWishPlace'
    ]),
    sliceName(name) {
      if (name.length > 7) {
      return name.substr(0, 7) + "..";
    } else {
      return name
    }}
  },
  created() {
    this.mode2 = this.wishPlace.mode2
    this.placeName = this.sliceName(this.wishPlace.name)
  },
  watch: {
    wishPlace() {
      this.mode2 = this.wishPlace.mode2
      this.placeName = this.sliceName(this.wishPlace.name)
    },
  },
};
</script>

<style>
.wish-place-items {
  position: relative;
  margin-right: 10px;
  border-radius: 5px;
}
.wish-place-delete-btn {
  position: absolute;
  top: 5%;
  right: 5%;
  height: 2vh;
  width: 2vh;
}
.wish-place-image-box {
  position: absolute;
  top: 50%;
  left: 50%;  
  transform: translate(-50%, -62%);
  height: 7vh;
  width: 7vh;
  padding: 7px;
  border-radius: 70%;
  background: rgba(256, 256, 256, 0.85);
}
.wish-place-image {
  width: 100%;
  height: 100%;
}
.wish-place-name {
  position: absolute;
  bottom: 8%;
  left:50%;
  transform: translate(-50%, 0%);
  color: #3a3c3c;
  font-size: 10px;
  font-weight: bold;
}
</style>