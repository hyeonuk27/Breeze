<template>
  <div class="find-middle-btn-items">
    <button
      type="button"
      class="find-middle-btn"
      @click="goToFindMiddle()"
      >중간 장소 찾기
    </button>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import dayjs from 'dayjs'
import  customParseFormat from 'dayjs/plugin/customParseFormat'
import isSameOrBefore from 'dayjs/plugin/isSameOrBefore'
import Swal from 'sweetalert2'
dayjs.extend(customParseFormat)
dayjs.extend(isSameOrBefore)

export default {
  name: 'FindMiddleBtn',
  methods: {
    ...mapActions([
      'setMode1',
      'setMiddle'
    ]),
    goToFindMiddle: function() {
      if (dayjs(this.date, 'YYYY-MM-DD HH:mm').isSameOrBefore(dayjs())) {
        Swal.fire({
          icon: 'error',
          html: '<b>약속 날짜를 올바르게 선택해주세요</b>',
          showConfirmButton: false,
          timer: 1500
        })
      } else if (this.participants.length < 2) {
        Swal.fire({
          icon: 'error',
          html: '<b>2명 이상의 친구를 추가해주세요</b>',
          showConfirmButton: false,
          timer: 1500
        })
      } else {
        this.$router.push({ name: 'FindMiddle' })
        this.setMode1(0)
        this.setMiddle(0)
      }
    }
  },
  computed: {
    ...mapGetters([
      'participants', 
      'date'
    ])
  }
}
</script>

<style scoped>
.find-middle-btn-items {
  position: relative;
}
.find-middle-btn-items .find-middle-btn {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 65%;
  height: 65%;
  padding: 3%;
  background: linear-gradient(to left, #92a3fd, #9dceff);
  box-shadow: 1px 1px 5px 0px gray;
  border: none;
  border-radius: 20px;
  color: white;
  font-weight: 600;
}
</style>