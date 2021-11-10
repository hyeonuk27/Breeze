<template>
  <div >
    <div class="date-container">
      <hr class="line-1">
      <div class="date-box">
        <div class="place-name">{{ middlePlace }}</div>
        <div class="date">{{ calDate }}</div> 
      </div>
      <hr class="line-2">
    </div>
  </div>
</template>

<script>
export default {
  name: 'AppointmentDate',
  props: {
    datetime: String,
    middlePlace: String,
  },
  data() {
    return {
      calDate: '',
    }
  },
  methods: {
    toLocalDate(data) {
      const date = data.substr(0, 4) + '년 ' + data.substr(5, 2) + '월 ' + data.substr(8, 2) + '일 '
      var localDate = new Date(data)
      // console.log(localDate, typeof(localDate))
      const local = localDate.toString()
      // console.log(typeof(local))
      const cal = date + local.substr(16, 2) + '시 ' + local.substr(19, 2) + '분' 
      this.calDate = cal
    }
  },
  created() {
    this.toLocalDate(this.datetime)
  }

}
</script>

<style>
.date-container {
  height: 100%;
}
.line-1 {
  margin-top: 0px;
  margin-bottom: 4%;
}
.line-2 {
  margin-top: 2%;
  margin-bottom: 0px;
}
.date-box {
  display: flex;
  flex-direction: column;
}
.date-box .place-name {
  font-weight: 600;
  font-size: 20px;
}
.date-box .date {
  font-size: 14px;
}
</style>