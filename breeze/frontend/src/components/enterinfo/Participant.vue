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
        @click="deleteParticipant([idx, participant.baramiType])"
      >
        <i class="fas fa-times"></i>
      </button>
    </div>
    <hr v-if="idx < participants.length - 1" class="participant-hr" />
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex"

export default {
  name: "Participant",
  props: {
    idx: Number,
    participant: Object,
  },
  methods: {
    ...mapActions(["deleteParticipant"]),
  },
  computed: {
    ...mapGetters(["participants"]),
  },
}
</script>

<style scoped>
.cancel-btn {
  background: none;
  border: none;
  text-align: right;
  color: #a7a7a7;
  font-weight: lighter;
}
.content-box {
  margin-left: 5%;
  text-align: left;
}
.image-box {
  margin-right: 3%;
  margin-left: 0;
  width: 18%;
  padding: 7px;
  border-radius: 70%;
  background: #e9edfe;
}
.image-box-barami {
  width: 100%;
  height: 100%;
}
.participant {
  width: 100%;
}
.participant-container {
  display: flex;
  justify-content: center;
  align-items: center;
}
.participant-hr {
  color: #a7a7a7;
  margin-left: 3%;
}
.participant-location {
  font-size: 10pt;
  color: #7b6f72;
}
.participant-name {
  font-weight: bold;
}
</style>