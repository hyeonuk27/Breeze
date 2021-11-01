<template>
  <div class="modal-dialog modal-dialog-centered">
    <div class="modal-content modal-box">
      <div>
        <div class="d-flex justify-content-end">
          <button type="button" class="btn-close cancel-btn" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <h5 class="modal-title" id="groupAppointmentModalLabel">약속 날짜 설정</h5>
      </div>
      <div>
        <v-date-picker mode="dateTime" v-model="date" class="choose-date">
          <template v-slot="{ inputValue, togglePopover }">
            <div
              class="choose-date-box"
              @click="togglePopover()">
              <button class="choose-date-btn">
                <i class="far fa-calendar-alt"></i>
              </button>
              <input
                placeholder="약속 날짜를 선택해주세요."
                :value="inputValue"
                class="choose-date-input text-gray-700 w-full py-1 px-2 appearance-none rounded-r focus:outline-none focus:border-blue-500"
                readonly
              />
            </div>
          </template>
        </v-date-picker>
      </div>
      <div class="d-flex justify-content-end">
        <!-- <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button> -->
        <button type="button" class="btn ok-btn">확인</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'GroupAppointmentModal',
  data () {
    return {
      date: ''
    }
  }
}
</script>

<style scoped>
.modal-box {
  border-radius: 20px;
  border: none;
  width: 95%;
  margin: 0 auto;
  box-shadow: 1px 1px 5px 0px gray;
}
.cancel-btn {
  text-align: left;
  font-size: 9pt;
  padding-top: 7%;
  padding-right: 7%;
}
.ok-btn {
  background: linear-gradient(to left, #92A3FD, #9DCEFF);
  border: none;
  font-size: 10pt;
  border-radius: 10px;
  padding: 1%;
  margin-bottom: 5%;
  margin-right: 5%;
  width: 20%;
  /* box-shadow: 1px 1px 5px 0px gray; */
  color: white;
}
.choose-date {
  margin: 4%;
  height: 30%;
}
.choose-date-box {
  width: 90%;
  /* height: 100%; */
  margin: 0 auto;
  border-radius: 15px;
  background-color: #F7F8F8;
  padding: 1%;
  padding-left: 3%;
  text-align: left;
}
.choose-date-btn {
  border: none;
  background-color: #F7F8F8;
  color: #ADA4A5;
}
.choose-date-input {
  background-color: #F7F8F8;
  border: none;
  text-align: left;
  color: #ADA4A5;
}
</style>