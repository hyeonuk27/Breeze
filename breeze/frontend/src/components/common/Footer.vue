<template>
  <div class="footer-items">
    <router-link to="/home">
      <img
        src="@/assets/footer/home.png"
        alt="home-button"
        @click="menuUpdate(0)"
        :style="[selectedMenu == 0 ? {opacity:1} : {opacity:0.5}]"
      />
    </router-link>
    <router-link to="/enterinfo">
      <img
        src="@/assets/footer/new.png"
        alt="new-button"
        @click="menuUpdate(1)"
        :style="[selectedMenu == 1 ? {opacity:1} : {opacity:0.5}]"
      />
    </router-link>
    <router-link to="/oneclick">
      <img
        src="@/assets/footer/oneclick.png"
        alt="oneclick-button"
        @click="menuUpdate(2)"
        :style="[selectedMenu == 2 ? {opacity:1} : {opacity:0.5}]"
      />
    </router-link>
  </div>
</template>

<script>
export default {
  name: "Footer",
  data() {
    return {
      selectedMenu: 0,
    }
  },
  methods: {
    menuUpdate: function (idx) {
      this.selectedMenu = idx
    },
  },
  created() {
    this.selectedMenu = 0
  },
};
</script>

<style scoped>
  .footer-items {
    display: flex;
    justify-content: space-around;
  }
  .footer-items img {
    width: 27px;
    height: 27px;
  }
  .deactivate {
    filter: opacity(0.5) drop-shadow(0 0 0 white);
  }
</style>