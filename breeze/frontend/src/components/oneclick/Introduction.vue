<template>
  <div class="introduction-container">
    <div class="image-box">
      <img
        :src="require('@/assets/barami/' + randomNum + '.png')"
        class="image-box-barami"
        alt="barami-character"
      />
    </div>
    <div v-if="this.groupId" class="intro-message">
      <div>{{ introMessage[randomNum][0] }}</div>
      <div>{{ introMessage[randomNum][1] }}</div>
    </div>
    <div v-if="!this.groupId" class="intro-message">
      <div>{{ introMessage2[0][0] }}</div>
      <div>{{ introMessage2[0][1] }}</div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'Introduction',
  data() {
    return {
      randomNum: 0,
      introMessage: [
        ['이전에 만났던 친구들 모임이에요', '편하게 약속을 만들어봐요!'],
        ['저장한 친구들 모임이에요', '다음 약속을 잡아볼까요?'],
        ['이전에 만났던 친구들 모임이에요', '다시 만날 때가 된 것 같네요!'],
        ['기억하고 싶은 친구들 모임이에요', '원클릭으로 약속을 만들어봐요!'],
        ['이전에 만났던 친구들 모임이에요', '다음 약속을 잡아볼까요?'],
        ['저장한 친구들 모임이에요', '약속 쿨타임이 다 찬 것 같아요!']
      ],
      introMessage2: [
        ['여기선 저장된 그룹을 확인하고', '이 모임 그대로 약속 잡을 수 있어요!']
      ]
    }
  },
  methods: {
    pickRandomNum: function () {
      this.randomNum = Math.floor(Math.random() * 6);
    },
  },
  created () {
    this.pickRandomNum()
  },
    computed: {
    ...mapGetters([
      'groupId',
    ])
  }
}
</script>

<style scoped>
.introduction-container {
  width: 88%;
  margin: 0 auto;
  display: flex;
  align-items: flex-end;
  justify-content: center;
}
.image-box {
  margin-right: 3%;
  width: 15%;
  /* padding: 3px; */
  border-radius: 70%;
  }
.image-box-barami {
  width: 100%;
  height: 100%;
}
.intro-message {
  color: #7B6F72;
  text-align: left;
}
</style>