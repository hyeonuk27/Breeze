<template>
  <div class="profile-items">
    <LogoutBtn />
    <div class="image-box">
      <img
        :src="require('@/assets/barami/' + randomNum + '.png')"
        class="image-box-barami"
        alt="barami-character"
      />
    </div>
    <div class="comment-box">
      <div class="comment-box-greet">안녕하세요 {{ userName }}님</div>
      <div>저 {{ baramiName[randomNum] }}{{ baramiComment[randomNum] }}</div>
    </div>
    <div v-if="appointmentCnt" class="remains">
      예정 약속 {{ appointmentCnt }}개가 있습니다.
    </div>
    <div v-else class="remains">예정 약속이 없습니다.</div>
  </div>
</template>

<script>
import LogoutBtn from "@/components/home/LogoutBtn"
import { mapGetters } from "vuex"

export default {
  name: "Myprofile",
  props: {
    appointmentCnt: Number,
  },
  components: {
    LogoutBtn,
  },
  data() {
    return {
      baramiComment: [
        "은 약속이 정말 기대돼요!",
        "은 날씨가 좋으면 설레요!",
        "과 추억을 만들러 갈까요?",
        "은 약속이 정말 좋아요!",
        "과 신나게 놀아요!",
        "과 함께 피크닉은 어때요!",
      ],
      baramiName: [
        "꽃바람",
        "신바람",
        "산들바람",
        "솔바람",
        "소소리바람",
        "실바람",
      ],
      randomNum: 0,
    }
  },
  methods: {
    pickRandomNum: function () {
      this.randomNum = Math.floor(Math.random() * 6)
    },
  },
  created() {
    this.pickRandomNum()
  },
  computed: {
    ...mapGetters(["userName"]),
  },
}
</script>

<style scoped>
* {
  color: #7b6f72;
  font-size: 12px;
}
.comment-box {
  grid-column-start: 2;
  grid-column-end: span 3;
  grid-row: 2;
  align-self: center;
  text-align: start;
  margin-bottom: 8px;
}
.comment-box-greet {
  font-size: 14px;
}
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
.profile-items {
  display: grid;
  grid-template-columns: 1fr 2fr;
  grid-template-rows: 1fr 2fr 2fr;
  padding: 5%;
  border-radius: 15px;
}
.remains {
  grid-column-start: 2;
  grid-column-end: span 3;
  grid-row: 3;
  align-self: center;
  text-align: start;
}
</style>