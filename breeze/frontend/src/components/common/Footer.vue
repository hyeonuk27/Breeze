<template>
  <div class="footer-items">
    <router-link to="/home">
      <img
        src="@/assets/footer/home.png"
        alt="home-button"
        @click="menuUpdate(0)"
        :style="[selectedMenu == 0 ? { opacity: 1 } : { opacity: 0.5 }]"
      />
    </router-link>
    <router-link to="/enterinfo">
      <img
        src="@/assets/footer/new.png"
        alt="new-button"
        @click="menuUpdate(1)"
        :style="[selectedMenu == 1 ? { opacity: 1 } : { opacity: 0.5 }]"
      />
    </router-link>
    <router-link to="/oneclick">
      <img
        src="@/assets/footer/oneclick.png"
        alt="oneclick-button"
        @click="menuUpdate(2)"
        :style="[selectedMenu == 2 ? { opacity: 1 } : { opacity: 0.5 }]"
      />
    </router-link>
  </div>
</template>

<script>
import { mapActions, mapState } from "vuex"

export default {
  name: "Footer",
  methods: {
    ...mapActions([
      "setDate",
      "setFilter",
      "setGroupId",
      "setGroupName",
      "setMenu",
      "setMiddle",
      "setMiddleLists",
      "setMiddleLat",
      "setMiddleLong",
      "setMiddleName",
      "setMode1",
      "setMode2",
      "setParticipants",
      "setPartMidTime",
      "setWishPlace",
    ]),
    menuUpdate: function (idx) {
      this.setMenu(idx)
      if (idx !== 1) {
        this.setDate("")
        this.setFilter(0)
        this.setGroupId(null)
        this.setGroupName("")
        this.setMiddleLists([])
        this.setMiddleLat(0)
        this.setMiddleLong(0)
        this.setMiddleName("")
        this.setMiddle(0)
        this.setMode1(0)
        this.setMode2(0)
        this.setParticipants([])
        this.setPartMidTime([])
        this.setWishPlace([])
      }
    },
  },
  computed: {
    ...mapState({
      selectedMenu: (state) => state.mode.menu,
    }),
  },
}
</script>

<style scoped>
.deactivate {
  filter: opacity(0.5) drop-shadow(0 0 0 white);
}
.footer-items {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
}
.footer-items img {
  height: 100%;
  width: 20%;
  flex: 1;
}
</style>