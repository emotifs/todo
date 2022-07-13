<template>
    <h1>{{idx + 1}} : {{title}}</h1>
</template>

<script>
export default {
  name: "TheTask",
  props : ['id', 'title', 'idx']
}
</script>

<style scoped>

</style>