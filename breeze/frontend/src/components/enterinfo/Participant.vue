<template>
  <div class="participant">
    <div class="participant-container">
      <div class="col-1 image-box">
        <img
          :src="require('@/assets/barami/' + participant.baramiType + '.png')"
          class="image-box-barami"
          alt="barami-character"
        />
      </div>
      <div class="col-6">
        <div class="content-box">
          <div class="participant-name">{{ participant.partName }}</div>
          <div class="participant-location">{{ participant.partLocation }}</div>
        </div>
      </div>
      <button
        class="col-3 cancel-btn"
        @click="deleteParticipant([idx, participant.baramiType])">
        <i class="fas fa-times"></i>
      </button>
    </div>
    <hr v-if="idx < participants.length-1" class="participant-hr">
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'Participant',
  props: {
    participant: Object,
    idx: Number,
  },
  methods: {
    ...mapActions([
      'deleteParticipant'
    ])
  },
  computed: {
    ...mapGetters([
      'participants'
    ])
  }
}
</script>

<style scoped>
.participant {
  width: 100%;
}
.participant-container {
  display: flex;
  justify-content: center;
  align-items: center;
}
.image-box {
  /* grid-column: 1; */
  /* grid-row: 2; */
  /* align-self: left;
  justify-self: left; */
  /* height: 5%; */
  margin-right: 3%;
  margin-left: 0;
  width: 18%;
  padding: 7px;
  border-radius: 70%;
  background: #E9EDFE;
  }
.image-box-barami {
  width: 100%;
  height: 100%;
}
.content-box {
  margin-left: 5%;
  text-align: left;
}
.participant-name {
  font-weight: bold;
}
.participant-location {
  font-size: 10pt;
  color: #7B6F72;
}
.participant-hr {
  color: #a7a7a7;
  margin-left: 3%;
}
.cancel-btn {
  background: none;
  border: none;
  text-align: right;
  /* padding-right: 4%; */
  /* width: 22%; */
  color: #a7a7a7;
  font-weight: lighter;
}
</style>