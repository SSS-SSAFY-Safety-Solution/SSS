<template>
  <div class="RevisionMenuBox">
    <span class="material-symbols-outlined flex" @click="toggle_view">circle_notifications</span>

    <div class="flex">
      <span @click="add_mia" class="material-symbols-outlined metalBtn linearBtn">person_add</span>
      <span @click="del_mia" class="material-symbols-outlined metalBtn linearBtn">delete</span>
    </div>
  </div>
</template>

<script>
import { useMiaStore } from '@/stores/mia';
export default {
  setup() {
    const miaStore = useMiaStore()
    miaStore.mia_list_mode = true
    function add_mia () { 
        miaStore.mia_update_id = -1
        miaStore.is_add_mia = !miaStore.is_add_mia
        miaStore.miaData = {
        name:'',
        child_img: {name: '이미지를 추가해 주세요'},
        age: 0,
      }
    }
    function del_mia (e) { 
      e.target.classList.toggle('clickR')
      miaStore.mia_list_mode = !miaStore.mia_list_mode
    }
    function toggle_view () {
      miaStore.is_alarm_view = !miaStore.is_alarm_view
      miaStore.is_add_mia = false
    }
    return {
      add_mia,
      del_mia,
      toggle_view
    }
  }
}

</script>

<style scoped>

.RevisionMenuBox {
  justify-content: space-between;
  text-align: center;
  display: flex;
  width: 200px;
  height: 28px;
  border-radius: 5px;
}
.metalBtn {
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
  color: #eee;
  background-color: hsla(0,0%,20%,1);
  border: none;
}

/* Linear ------------------------- */

.metalBtn.linearBtn {
  width: 28px;
  font-size: 1.5em;
  height: 28px;

}
.menuIcons {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

/* active ------------------------- */


.clickB:hover {
  color: hsl(210, 100%, 40%);

  box-shadow: 
    inset hsla(210,100%,30%,  1) 0  0px 0px 2px, /* border */
    inset rgba(255, 255, 255, 0.7) 0  2px 1px 14px, /* top HL */
    
    hsla(210 ,100%,55%, .8) 0  0px 1px 1px, /* outer SD */
    hsla(210 ,80%,95%, 1) 0px  0px 0px 0px; /* outer HL */
}
.clickY {
  color: hsl(43, 80%, 70%);

  box-shadow: 
    inset rgb(212, 176, 84) 0  0px 0px 2px, /* border */
    inset rgba(255, 255, 255, 0.525) 0  2px 1px 14px, /* top HL */
    
    hsla(43,100%,75%, .8) 0  0px 1px 1px, /* outer SD */
    hsla(210 ,80%,95%, 1) 0px  0px 0px 0px; /* outer HL */
}
.clickR {
  color: hsla(0,100%,30%,  1);

  box-shadow: 
    inset hsla(0,100%,30%,  1) 0  0px 0px 2px, /* border */
    inset rgba(255, 255, 255, 0.862) 0  2px 1px 14px, /* top HL */
    
    hsla(0,100%,75%, .8) 0  0px 1px 1px, /* outer SD */
    hsla(210 ,80%,95%, 1) 0px  0px 0px 0px; /* outer HL */
}
.flex {
  display: flex;
  align-items: center;
}
</style>