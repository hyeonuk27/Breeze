<template>
  <div class="modal-dialog modal-container">
    <div class="modal-content modal-box">
      <div class="modal-head-content">
        <div class="d-flex justify-content-end">
          <button
            type="button"
            class="btn-close cancel-btn"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <h5 class="modal-title" id="rememberModalLabel">이멤버 리멤버</h5>
        <p class="modal-desc">이 멤버 그대로 다음에도 약속을 잡을 수 있어요!</p>
      </div>
      <div class="choose-name-box">
        <i class="fas fa-user-friends"></i>
        <input
          type="text"
          placeholder="모임 이름을 입력해주세요."
          v-model="groupName"
          class="
            choose-name-input
            text-gray-700
            w-full
            py-1
            px-2
            appearance-none
            rounded-r
          "
        />
      </div>
      <div class="d-flex justify-content-end">
        <button
          type="button"
          class="btn ok-btn"
          @click="createGroup()"
          data-bs-dismiss="modal"
        >
          저장하기
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex"
import groupApi from "@/api/group.js"
import Swal from "sweetalert2"

export default {
  name: "RememberModal",
  data() {
    return {
      groupName: "",
    }
  },
  methods: {
    ...mapActions(["setIsGroupSaved"]),
    async createGroup() {
      if (this.groupName == "") {
        Swal.fire({
          icon: "error",
          html: "<b>그룹 이름을 입력해주세요</b>",
          showConfirmButton: false,
          timer: 1500,
        })
      } else {
        Swal.fire({
          icon: "success",
          html: "<b>그룹이 저장되었습니다</b>",
          showConfirmButton: false,
          timer: 1500,
        })
      }
      const data = {
        groupName: this.groupName,
        groupMembers: this.participants,
      }
      await groupApi.createGroup(data)
      this.groupName = ""
      this.setIsGroupSaved(true)
    },
  },
  computed: {
    ...mapGetters(["participants"]),
  },
}
</script>

<style scoped>
.cancel-btn {
  text-align: left;
  font-size: 9pt;
  padding-top: 7%;
  padding-right: 7%;
}
.choose-name-box {
  width: 90%;
  margin: 0 auto;
  border-radius: 15px;
  background-color: #f7f8f8;
  padding: 1%;
  padding-left: 3%;
  text-align: left;
}
.choose-name-input {
  background-color: #f7f8f8;
  border: none;
  text-align: left;
  color: #ada4a5;
}
.choose-name-input:focus {
  outline: none;
}
.modal-box {
  border-radius: 20px;
  border: none;
  width: 95%;
  margin: 0 auto;
  box-shadow: 1px 1px 5px 0px gray;
}
.modal-container {
  margin-top: 40%;
}
.modal-desc {
  font-size: 14px;
  margin: 10px;
}
.ok-btn {
  background: linear-gradient(to left, #92a3fd, #9dceff);
  border: none;
  font-size: 10pt;
  border-radius: 10px;
  padding: 1%;
  margin-top: 3%;
  margin-bottom: 5%;
  margin-right: 5%;
  width: 20%;
  height: 37px;
  color: white;
}
</style>