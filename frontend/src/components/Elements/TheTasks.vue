<template>
  <section>
    <BaseCard>
      <p v-if="results.length === 0">Tasks not found. To add the task, please enter task to input</p>
      <ul
          v-for="(task, idx) in results"
          :key="task.id"
      >
        <TheTask :id="task.id" :title="task.title" :idx="idx"/>
      </ul>
    </BaseCard>
  </section>
</template>

<script>
import BaseCard from "@/components/UI/BaseCard";
import TheTask from "@/components/Elements/TheTask";
export default {
  name: "TheTasks",
  components: {TheTask, BaseCard},
  data(){
    return{
      results : []
    }
  },


  mounted(){
    fetch('http://127.0.0.1:8000/api/task-list/').then((res) => {
      if(res.ok){
        return res.json();
      }
    }).then((data) => {
      // console.log(data);
      for(const idx in data){
        this.results.push({
          id : data[idx].id,
          title : data[idx].title
        })
      }
    })
    console.log(this.results)
  }
}
</script>

<style scoped>

</style>