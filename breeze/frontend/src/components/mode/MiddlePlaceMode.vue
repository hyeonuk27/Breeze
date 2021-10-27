<template>
  <div class="mode1-items">
    <button @click="modeUpdate(0)" :style="[selectedMode == 0 ? {color:'#4F5B9A'} : {color:'#FFFFFF'}]">완벽한중간</button>
    <button @click="modeUpdate(1)" :style="[selectedMode == 1 ? {color:'#4F5B9A'} : {color:'#FFFFFF'}]">핫플레이스</button>
    <button @click="modeUpdate(2)" :style="[selectedMode == 2 ? {color:'#4F5B9A'} : {color:'#FFFFFF'}]">코로나멈춰</button>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'MiddlePlaceMode',
  data() {
    return {
      selectedMode: 0
    }
  },
  methods: {
    ...mapActions([
      'setMode1'
    ]),
    modeUpdate: function (idx) {
      this.setMode1(idx)
      this.selectedMode = idx
    }
  },
  created() {
    this.selectedMode = 0
  },
}
</script>

<style scoped>
  .mode1-items {
    display: flex;
    justify-content: space-around;
  }
  .mode1-items button {
    width:100px;
    background-color: rgba(256, 256, 256, 0);
    border: none;
    font-weight: 600;
    font-size: 15px;
  }
</style>