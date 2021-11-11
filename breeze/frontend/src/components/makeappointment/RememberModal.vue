<template>
  <div class="modal-dialog modal-container">
    <div class="modal-content modal-box">
      <div class="modal-head-content">
        <div class="d-flex justify-content-end">
          <button type="button" class="btn-close cancel-btn" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <h5 class="modal-title" id="rememberModalLabel">이멤버 리멤버</h5>
        <p class="modal-desc">이 멤버 그대로 다음에도 약속을 잡을 수 있어요!</p>
      </div>
      <div
        class="choose-name-box">
        <i class="fas fa-user-friends"></i>
        <input
          type="text"
          placeholder="모임 이름을 입력해주세요."
          v-model="groupName"
          class="choose-name-input text-gray-700 w-full py-1 px-2 appearance-none rounded-r"
        />
      </div>
      <div class="d-flex justify-content-end">
        <button type="button" class="btn ok-btn" @click="createGroup()" data-bs-dismiss="modal">저장하기</button>
      </div>
    </div>
  </div>

</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import groupApi from '@/api/group.js'

export default {
  name: 'RememberModal',
  data () {
    return {
      groupName: '',
    }
  },
  methods: {
    ...mapActions([
      'setIsGroupSaved',
    ]),
    async createGroup() {
      if (this.groupName == '') {
        alert('그룹 이름을 입력해주세요')
      }
      console.log(this.participants, this.groupName)
      const data = {
        groupName: this.groupName,
        groupMembers: this.participants
      }
      const response = await groupApi.createGroup(data)
      console.log(response)
      this.groupName = ''
      this.setIsGroupSaved(true)
    }
  },
  computed: {
    ...mapGetters([
    'participants'
  ])
  },
  watch: {
    groupName() {
      // console.log(val)
    }
  }

}
</script>

<style scoped>
.modal-container {
  margin-top: 40%; 
}
.modal-box {
  border-radius: 20px;
  border: none;
  width: 95%;
  margin: 0 auto;
  box-shadow: 1px 1px 5px 0px gray;
}
.modal-desc {
  font-size: 14px;
  margin: 10px;
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
  margin-top: 3%;
  margin-bottom: 5%;
  margin-right: 5%;
  width: 20%;
  height: 37px;
  /* box-shadow: 1px 1px 5px 0px gray; */
  color: white;
}
.choose-name-box {
  width: 90%;
  /* height: 100%; */
  margin: 0 auto;
  border-radius: 15px;
  background-color: #F7F8F8;
  padding: 1%;
  padding-left: 3%;
  text-align: left;
}
.choose-name-input {
  background-color: #F7F8F8;
  border: none;
  text-align: left;
  color: #ADA4A5;
}
.choose-name-input:focus {
  outline: none;
}
</style>