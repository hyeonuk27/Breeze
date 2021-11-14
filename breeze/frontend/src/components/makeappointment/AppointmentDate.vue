<template>
  <div>
    <div class="date-container">
      <hr class="line-1" />
      <div class="date-box">
        <div class="place-name">{{ middlePlace }}역</div>
        <div class="date">{{ datetime }}</div>
      </div>
      <hr class="line-2" />
    </div>
  </div>
</template>

<script>
export default {
  name: "AppointmentDate",
  props: {
    datetime: String,
    middlePlace: String,
  },
  methods: {
    toLocalDate(data) {
      const date =
        data.substr(0, 4) +
        "년 " +
        data.substr(5, 2) +
        "월 " +
        data.substr(8, 2) +
        "일 "
      var localDate = new Date(data)
      const local = localDate.toString()
      return date + local.substr(16, 2) + "시 " + local.substr(19, 2) + "분"
    },
  },
}
</script>

<style>
.date-box {
  display: flex;
  flex-direction: column;
}
.date-box .date {
  font-size: 14px;
}
.date-box .place-name {
  font-weight: 600;
  font-size: 20px;
}
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
</style>