<script setup>
import Message from './components/Message.vue'
import Hierarchy from './components/Hierarchy.vue'
</script>

<template>
  <header>
    <div class="wrapper">
      <Message msg="Hierarchy Data Visulization" />
    </div>
  </header>

  <main>
    <Hierarchy />
  </main>
</template>

<style scoped>
header {
  line-height: 1.5;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}

</style>
