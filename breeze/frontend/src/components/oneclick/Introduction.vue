<template>
  <div class="d-flex align-items-center justify-content-center">
    <div class="image-box">
      <img
        :src="require('@/assets/barami/' + randomNum + '.png')"
        class="image-box-barami"
        alt="barami-character"
      />
    </div>
    <div class="intro-message">
      <div>{{ introMessage[randomNum][0] }}</div>
      <div>{{ introMessage[randomNum][1] }}</div>
    </div>
  </div>
</template>

<script>
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
  }
}
</script>

<style scoped>
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