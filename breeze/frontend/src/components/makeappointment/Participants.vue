<template>
  <div class="participant-container">
    <div class="participant-items">
      <div
        v-for="(part, idx) in noteParticipants"
        :key="idx"
        class="participant-item"
      >
        <div class="participant">
          <div class="image-box">
            <img
              :src="require('@/assets/barami/' + part.barami_type + '.png')"
              class="barami-img"
              alt="barami-character"
            />
          </div>
          <div class="part-name">{{ part.name }}</div>
          <div class="part-time">{{ part.time }}분</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Participants",
  props: {
    noteParticipants: Array,
  },
}
</script>

<style scoped>
.barami-img {
  width: 100%;
  height: 100%;
}
.image-box {
  width: 6.7vh;
  height: 6.7vh;
}
.part-name {
  font-size: 10px;
  padding-top: 4px;
}
.part-time {
  font-size: 9px;
}
.participant {
  display: flex;
  flex-direction: column;
}
.participant-container {
  width: 100%;
  padding-top: 5%;
  padding-bottom: 2%;
}
.participant-container .participant-items {
  height: 100%;
  display: flex;
  justify-content: space-around;
}
.participant-item {
  width: 13%;
  display: inline-block;
}
</style>