<template>
  <div class="mode2-items">
    <button @click="modeUpdate(0)" :style="[selectedMode == 0 ? {color:'#4F5B9A'} : {color:'#FFFFFF'}]">식당</button>
    <button @click="modeUpdate(1)" :style="[selectedMode == 1 ? {color:'#4F5B9A'} : {color:'#FFFFFF'}]">카페</button>
    <button @click="modeUpdate(2)" :style="[selectedMode == 2 ? {color:'#4F5B9A'} : {color:'#FFFFFF'}]">술집</button>
    <select v-model="selectedFilter" class="select" name="filter">
      <option value=0>인기순</option>
      <option value=1>평점순</option>
      <option value=2>랜 덤</option>
      {{selectedFilter}}
    </select>

  </div>
</template>

<script>
import { mapActions, mapState} from 'vuex'

export default {
  name: 'PlaceMode',
  data() {
    return {
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
    },
    filterUpdate(idx) {
      this.setFilter(idx)
      this.selectedFilter = idx
    }
  },
  created() {
    this.selectedFilter = this.filter 
  },
  computed: {
   ...mapState({
      selectedMode: state => state.mode.mode2,
      filter: state => state.mode.filter,
    }),
  },
  watch: {
    selectedFilter(val){
      this.filterUpdate(val)
    }
  },
}
</script>

<style scoped>
  .mode2-items button {
    height: 100%;
    width:23%;
    background-color: rgba(256, 256, 256, 0);
    border: none;
    font-weight: 600;
    font-size: 15px;
  }
  .select {
    height: 100%;
    width: 20%;
    margin-right: 4%;
    margin-left: 2%;
    font-weight: 600;
    font-size: 15px;
    background: transparent;
    border: 0 none;
    outline: 0 none;
    position: relative;
    z-index: 3;
    color: #4F5B9A
  }
</style>