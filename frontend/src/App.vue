<template>
  <AddTask />
  <TheTasks />
</template>

<script>

import AddTask from "@/components/Elements/AddTask";
import TheTasks from "@/components/Elements/TheTasks";
export default {
  name: 'App',
  components: {
    TheTasks,
    AddTask
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
