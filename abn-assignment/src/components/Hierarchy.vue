<script setup>
import OrganizationChart from 'primevue/organizationchart';
import Card from 'primevue/card';
import Button from 'primevue/button';


import { ref } from "vue";

const data = ref({
    key: '0',
    label: "A",
    data: { "description": "This is a description of A" },
    children: [
        {
            key: '0_0',
            label: "B",
            data: { "description": "This is a description of B" },
            children: [
                {
                    key: '0_0_1',
                    label: "B-1",
                    data: { "description": "This is a description of B-1" }
                },
                {
                    key: '0_0_2',
                    label: "B-2",
                    data: { "description": "This is a description of B-2" }
                },
                {
                    key: '0_0_3',
                    label: "B-3",
                    data: { "description": "This is a description of B-3" }
                }
            ]
        },
        {
            key: '0_1',
            label: "C",
            data: { "description": "This is a description of C" }
        },
        {
            key: '0_2',
            label: "D",
            data: { "description": "This is a description of D" }
        }
    ]
});
const selection = ref({});
let selectedNode = ref({});

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
            <template #title>{{ selectedNode.label }}</template>
            <template #content>
                <p class="m-0">
                    {{ selectedNode.data.description }}
                </p>
            </template>
        </Card>
    </div>
</template>
