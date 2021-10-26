<template>
  <div class="footer-items">
    <router-link to="/home">
      <img
        src="@/assets/footer/home.png"
        alt="home-button"
        :class="{ deactivate: $route.name !== 'Home' }"
      />
    </router-link>
    <router-link to="/enterinfo">
      <img
        src="@/assets/footer/new.png"
        alt="new-button"
        :class="[{ deactivate: $route.name == 'Home'}, { deactivate: $route.name == 'OneClick'}]"
      />
    </router-link>
    <router-link to="/oneclick">
      <img
        src="@/assets/footer/oneclick.png"
        alt="oneclick-button"
        :class="{ deactivate: $route.name !== 'OneClick' }"
      />
    </router-link>
  </div>
</template>

<script>
export default {
  name: "Footer",
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