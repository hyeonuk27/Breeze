<template>
    <div class="background">
        <div class="not-found-body">
            <img src="@/assets/barami/3.png" alt="" class="n3">
            <div class="not-found-text">
                <h4 class="text">잘못된 방향입니다!</h4>
                <p class="desc">
                    바라미들과는 갈 수 없는 곳이에요<br>
                    다른 길을 찾아볼까요?
                </p>
                <button class="btn" @click="goToHome">Home</button>
            </div>
        </div>
        <div class="wave-set">
            <img src="@/assets/wave (3).svg" alt="" class="wave2">
            <img src="@/assets/wave.svg" alt="" class="wave1">
            <img src="@/assets/wave (12).svg" alt="" class="wave3">
        </div>
        
        <div class="barami-set">
            <!-- <img src="@/assets/baramis.png" alt="" class="barami"> -->
            <div class="title">breeze</div>
        </div>
    </div>
</template>


<script>
export default {
  name: 'NotFound',
  methods: {
    goToHome() {
      this.$router.push({ name: 'Home' })
    }
  }
}
</script>

<style scoped>

.wave-background {
  width: 100%;
  height: 45%;
}

.not-found-body {
    padding-top: 20%;
    justify-content: center;
}

.barami-set {
    margin-top: 70%;
}

.not-found-text {
  margin-top: 10%;
}

.title {
  margin-top: 1%;
  font-size: 15px;
  font-weight: bold;
  color: #525252;
}

.text {
    font-weight: bold;
}

.desc {
  padding-top: 1%;
  padding-bottom: 2%;
  color:  #919399;
  font-weight: bold;
}

@keyframes shake {
	0%{
		transform: translate(1px, 1px) rotate(0deg);
	}
	10%{
		transform: translate(-1px, -1px) rotate(1deg);
	}
	20%{
		transform: translate(-2px, 1px) rotate(-1deg);
	}
	30%{
		transform: translate(1px, 2px) rotate(0deg);
	}
	40%{
		transform: translate(-1px, 1px) rotate(1deg);
	}
	50%{
		transform: translate(1px, -1px) rotate(-2deg);
	}
	60%{
		transform: translate(2px, 1px) rotate(1deg);
	}
	70%{
		transform: translate(-1px, 2px) rotate(2deg);
	}
	80%{
		transform: translate(2px, -1px) rotate(1deg);
	}
	90%{
		transform: translate(-1px, 2px) rotate(0deg);
	}
	100%{
		transform: translate(2px, 1px) rotate(-1deg);
	}
}

.n3 {
	animation: shake 0.5s infinite;
    width: 50px;
}

.barami {
    width: 150px;
}

.wave-set {
    margin-top: 35%;
    position: relative;
}

.wave1 {
    position: absolute;
    top: 0;
    left: 0;
}

.wave2 {
    position: absolute;
    top: 20;
    left: 0;
}

.wave3 {
    position: absolute;
    margin-top: 12%;
    left: 0;
}

button {
    position: absolute;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 30%;
    margin-top: 5%;
    padding: 3%;
    background: linear-gradient(to left, #92a3fd, #9dceff);
    box-shadow: 1px 1px 5px 0px gray;
    border: none;
    border-radius: 20px;
    color: white;
}

</style>