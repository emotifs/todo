<template>
  <button>
    <slot></slot>
  </button>
</template>

<style scoped>
button {
  font: inherit;
  border: 1px solid rgba(77, 112, 255, 0.7);
  background-color: rgba(77, 112, 255, 0.7);
  color: white;
  padding: 0.5rem 2rem;
  cursor: pointer;
}
button:hover,
button:active {
  background-color: rgba(77, 112, 255, 0.7);
  border-color: rgba(77, 112, 255, 0.7);
}
</style>