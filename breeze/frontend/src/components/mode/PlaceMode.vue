<template>
  <div class="mode2-items">
    <button @click="modeUpdate(0)" :style="[selectedMode == 0 ? {color:'#4F5B9A'} : {color:'#FFFFFF'}]">식당</button>
    <button @click="modeUpdate(1)" :style="[selectedMode == 1 ? {color:'#4F5B9A'} : {color:'#FFFFFF'}]">카페</button>
    <button @click="modeUpdate(2)" :style="[selectedMode == 2 ? {color:'#4F5B9A'} : {color:'#FFFFFF'}]">술집</button>
    <button @click="modeUpdate(3)" :style="[selectedMode == 3 ? {color:'#4F5B9A'} : {color:'#FFFFFF'}]">문화</button>
    <button class="dropdown">인기순</button>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'PlaceMode',
  data() {
    return {
      selectedMode: 0,
    }
  },
  methods: {
    ...mapActions([
      'setMode2'
    ]),
    modeUpdate: function (idx) {
      this.setMode2(idx)
      this.selectedMode = idx
    },
  },
  created() {
    this.selectedMode = 0
  },
}
</script>

<style scoped>
  .mode2-items {
    display: flex;
    justify-content: space-around;
  }
  .mode2-items button {
    width:100px;
    background-color: rgba(256, 256, 256, 0);
    border: none;
    font-weight: 600;
    font-size: 15px;
  }
  .dropdown {
    color: #FFFFFF
  }
</style>