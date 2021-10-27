<template>
  <div class="mode2-items">
    <button @click="modeUpdate(0)" :style="[selectedMode == 0 ? {color:'#4F5B9A'} : {color:'#FFFFFF'}]">식당</button>
    <button @click="modeUpdate(1)" :style="[selectedMode == 1 ? {color:'#4F5B9A'} : {color:'#FFFFFF'}]">카페</button>
    <button @click="modeUpdate(2)" :style="[selectedMode == 2 ? {color:'#4F5B9A'} : {color:'#FFFFFF'}]">술집</button>
    <button @click="modeUpdate(3)" :style="[selectedMode == 3 ? {color:'#4F5B9A'} : {color:'#FFFFFF'}]">문화</button>
    <select v-model="selectedFilter" class="select" name="filter">
      <option value=0 selected >인기순</option>
      <option value=1>평점순</option>
      <option value=2>랜 덤</option>
    </select>

  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'PlaceMode',
  data() {
    return {
      selectedMode: 0,
      selectedFilter: 0,
    }
  },
  methods: {
    ...mapActions([
      'setMode2',
      'setFilter'
    ]),
    modeUpdate: function (idx) {
      this.setMode2(idx)
      this.selectedMode = idx
    },
  },
  created() {
    this.selectedMode = 0
  },
  watch: {
    selectedFilter: function (idx) {
      this.setFilter(idx)
    }
  }
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
  .select {
    font-weight: 600;
    font-size: 15px;
    background: transparent;
    border: 0 none;
    outline: 0 none;
    padding: 0 5px;
    position: relative;
    z-index: 3;
    color: #4F5B9A
  }
</style>