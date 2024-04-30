<script setup>
import OrganizationChart from 'primevue/organizationchart'
import Card from 'primevue/card'
import Button from 'primevue/button'
import { ref, onMounted } from 'vue'
import { fetchData } from '../service/dataService'

const data = ref({})
let selectedNode = ref({})
const selection = ref({})

// Shows card
const show = (event) => {
  console.log('Inside of show')
  selectedNode.value = event
  console.log(selectedNode)
}

// Hides card
const hide = () => {
  console.log('Inside of hide')

  selectedNode.value = {}
  // Unselect nodes
  selection.value = {}
  console.log(selectedNode)
}

onMounted(async () => {
  // Fetch data when the component is mounted
  data.value = await fetchData()
})
</script>

<template>
  <div class="card overflow-x-auto">
    <OrganizationChart
      v-model:selectionKeys="selection"
      :value="data"
      selectionMode="single"
      @node-select="show"
      @node-unselect="hide"
    >
      <template #default="slotProps">
        <span>{{ slotProps.node.label }}</span>
      </template>
    </OrganizationChart>

    <Card v-if="Object.keys(selectedNode).length !== 0" class="card-with-shadow">
      <template #header>
        <Button icon="pi pi-times" severity="danger" aria-label="Cancel" @click="hide" />
      </template>
      <template #title>{{ selectedNode.name }}</template>
      <template #content>
        <p class="m-0">
          {{ selectedNode.data.description }}
        </p>
      </template>
    </Card>
  </div>
</template>

<style scoped>

.card-with-shadow {
  box-shadow: 2px 5px 5px 8px rgba(0, 0, 0, 0.1); /* Adjust shadow properties as needed */
  margin: 20px; 
}
</style>