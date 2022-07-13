<template>
  <section>
    <BaseCard>
      <h2>Add New Task: </h2>
      <form @submit.prevent="addTask">
        <h5 v-if="invalidInput" style="color: red">Invalid input. Please try again</h5>
        <div class="form-control">
          <input type="text" v-model.trim="enteredTask" id="enteredTask" name="enteredTask">
        </div>
        <div>
          <BaseButton>Add</BaseButton>
        </div>
      </form>
    </BaseCard>
  </section>
</template>

<script>
import BaseCard from "@/components/UI/BaseCard";
import BaseButton from "@/components/UI/BaseButton";
export default {
  name: "AddTask",
  components: {BaseButton, BaseCard},

  data(){
    return {
      enteredTask : '',
      invalidInput : false,
    }
  },
  methods : {
    addTask(){
      if(this.enteredTask.trim().length === 0) {
        this.invalidInput = true;
        return;
      }

      this.invalidInput = false;
      fetch('http://127.0.0.1:8000/api/task-create/', {
        method : 'POST',
        headers : {
          'Content-Type' : 'application/json'
        },
        body : JSON.stringify({
          title : this.enteredTask,
        })
      })
      this.enteredTask = '';
    }
  }
}
</script>

<style scoped>
  .form-control {
    margin: 2rem 12rem;
  }
  input[type='text'] {
    display: block;
    width: 15rem;
    margin-top: 0.5rem;
    padding:5px;
    border-radius: 5px;
  }
</style>