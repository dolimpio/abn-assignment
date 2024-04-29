<script setup>
import OrganizationChart from 'primevue/organizationchart';
import Card from 'primevue/card';
import Button from 'primevue/button';
import { ref, onMounted } from "vue";
import { fetchData } from '../service/dataService';

const data = ref({});
let selectedNode = ref({});
const selection = ref({});

const show = (event) => {
    console.log("Inside of show");
    selectedNode.value = event;
    console.log(selectedNode);
}

const hide = () => {
    console.log("Inside of hide");

    selectedNode.value = {};
    // Unselect nodeS
    selection.value = {};
    console.log(selectedNode);
}

onMounted(async () => {
    // Fetch data when the component is mounted
    data.value = await fetchData();
});

</script>

<template>
    <div class="card overflow-x-auto">
        <OrganizationChart v-model:selectionKeys="selection" :value=data selectionMode="single" @node-select="show"
            @node-unselect="hide">
            <template #default="slotProps">
                <span>{{ slotProps.node.label }}</span>
            </template>
        </OrganizationChart>
        <Card v-if="Object.keys(selectedNode).length !== 0">
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
