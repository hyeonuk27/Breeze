<template>
  <div>
    <div
      v-for="(part, idx) in participants"
      :key="idx"
      >
      <div class="image-box">
        <img
          :src="require('@/assets/barami/' + part.baramiType + '.png')"
          class="image-box-barami"
          alt="barami-character"
        />
        <div>{{ part.name }}</div>
        <div>{{ part.location }}</div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'Participant',
  data () {
    return {
    }
  },
  computed: {
    ...mapGetters([
      'participants'
    ])
  }
}
</script>

<style>
.image-box {
    grid-column: 1;
    grid-row: 2;
    align-self: center;
    justify-self: center;
    height: 48px;
    width: 48px;
    padding: 7px;
    border-radius: 70%;
    background: rgba(256, 256, 256, 0.5);
  }
.image-box-barami {
  width: 100%;
  height: 100%;
}
</style>