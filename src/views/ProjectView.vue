<template>
    <AppWrapper>
        <!-- https://vuetifyjs.com/en/components/buttons/#discord-event -->
        <div class="pa-5 task-container overflow-x-auto">
            <h2 class="mb-2">專案 1</h2>
            <template v-for="list in Task_List" :key="list.Task_List_ID">
                <v-card class="mr-5 task-card" color="#36393f" theme="dark" variant="flat">
                    <v-sheet color="#202225">
                        <v-card-item>
                            <template v-slot:prepend>
                                <v-chip v-if="list.Task_List_Status" class="bg-green"><strong>進行中</strong></v-chip>
                                <v-chip v-else class="bg-grey"><strong>已完成</strong></v-chip>
                            </template>

                            <!-- edit title -->
                            <input
                                v-if="list.Task_List_ID === cache_Task_List.Task_List_ID && edit_target === 'Task_List_Name'"
                                type="text" class="pl-1 w-100 bg-grey-lighten-5" v-model="cache_Task_List.Task_List_Name"
                                @keyup.esc="edit_TaskList()" @blur="edit_TaskList()" @keyup.enter="doneEdit()">
                            <h4 v-else @dblclick="edit_TaskList(list, target = 'Task_List_Name')">{{
                                list.Task_List_Name }}</h4>

                            <template v-slot:append>
                                <v-btn icon="$edit" size="small" variant="text"
                                    @click="edit_TaskList(list, target = 'Task_List_Name')"></v-btn>
                                <v-btn icon="$close" size="small" variant="text"></v-btn>
                            </template>
                        </v-card-item>
                    </v-sheet>

                    <template v-for="task in list.Task_Card" :key="n">
                        <v-card class="ma-4" color="#2f3136" rounded="lg" variant="flat">
                            <v-card-item>
                                <v-card-title class="text-body-2 d-flex align-center mb-2">
                                    <!-- <v-icon color="#949cf7" icon="mdi-calendar" start></v-icon> -->
                                    <div>
                                        <v-chip v-bind="props" class="mr-3 bg-green">已完成</v-chip>
                                    </div>

                                    <v-spacer></v-spacer>

                                    <v-avatar image="https://cdn.vuetifyjs.com/images/john-smirk.png"
                                        size="x-small"></v-avatar>

                                    <div>
                                        <v-chip class="ms-2 text-medium-emphasis" color="grey-darken-4"
                                            prepend-icon="mdi-account-multiple" size="small" text="81"
                                            variant="flat"></v-chip>
                                    </div>
                                </v-card-title>

                                <div class="py-2">
                                    <div class="d-flex justify-space-between align-center">
                                        <div class="w-100">
                                            <input
                                                v-if="task.Task_Card_ID === cache_Task_Card.Task_Card_ID && edit_target === 'Task_Card_Name'"
                                                type="text" class="pl-1 w-100 bg-grey-lighten-5"
                                                v-model="cache_Task_Card.Task_Card_Name" @keyup.esc="edit_TaskCard()"
                                                @blur="edit_TaskCard()" @keyup.enter="doneEdit()">
                                            <h4 v-else class="text-h6"
                                                @dblclick="edit_TaskCard(task, target = 'Task_Card_Name')">
                                                {{ task.Task_Card_Name }}
                                            </h4>
                                        </div>
                                        <v-btn icon="$edit" size="small" variant="text"
                                            @click="edit_TaskCard(task, target = 'Task_Card_Name')"></v-btn>
                                    </div>

                                    <div class="d-flex justify-space-between align-center">
                                        <v-textarea
                                            v-if="task.Task_Card_ID === cache_Task_Card.Task_Card_ID && edit_target === 'Task_Card_Text'"
                                            v-model="cache_Task_Card.Task_Card_Text"
                                            :model-value="cache_Task_Card.Task_Card_Text"
                                            @blur="edit_TaskCard()"></v-textarea>
                                        <p v-else class="font-weight-light text-medium-emphasis task_card_text mb-3"
                                            @dblclick="edit_TaskCard(task, target = 'Task_Card_Text')">
                                            {{ task.Task_Card_Text }}
                                        </p>
                                    </div>

                                    <div>
                                        <v-tooltip text="1 Fri Dec 16th - 9:00" location="bottom">
                                            <template v-slot:activator="{ props }">
                                                <v-chip v-bind="props" class="mr-3">
                                                    開始時間
                                                </v-chip>
                                            </template>
                                        </v-tooltip>
                                        <v-tooltip text="1 Fri Dec 17th - 17:00" location="bottom">
                                            <template v-slot:activator="{ props }">
                                                <v-chip v-bind="props" class="mr-3">
                                                    截止時間
                                                </v-chip>
                                            </template>
                                        </v-tooltip>
                                    </div>
                                </div>
                            </v-card-item>

                            <v-divider></v-divider>

                            <div class="pa-4 d-flex align-center justify-end">
                                <v-btn class="mr-3 text-none" color="#4f545c" variant="flat">
                                    查看
                                </v-btn>
                                <v-btn class="text-none bg-red" variant="flat">
                                    刪除
                                </v-btn>
                            </div>
                        </v-card>
                    </template>
                    <v-btn class="text-none text-subtitle-1 ma-4" color="#5865f2" variant="flat">
                        新增任務卡
                    </v-btn>
                </v-card>
            </template>
            <v-btn size="large" class="mr-5 d-inline-block bg-black">新增任務列表</v-btn>
        </div>
    </AppWrapper>
</template>

<script>
import axios from "axios";
import AppWrapper from '../components/AppWrapper.vue';

export default {
    data: () => ({
        model: null,
        Task_List: [],
        Project_WorksOn: [],
        // caches are used for update, they should always be empty objects when not updating.
        cache_Task_List: {},
        cache_Task_Card: {},
        cache_Todo: {},
        cache_Comment: {},
        edit_target: ""
    }),
    components: {
        AppWrapper
    },
    methods: {
        isObjEmpty(obj) {
            return Object.keys(obj).length === 0;
        },
        clearCache() {
            this.cache_Task_List = {};
            this.cache_Task_Card = {};
            this.cache_Todo = {};
            this.cache_Comment = {};
            this.edit_target = "";
        },
        getTaskList() {
            let self = this;
            axios.get('http://127.0.0.1:5001/tasklist')
                .then(function (response) {
                    self.Task_List = response.data.Task_List
                    console.log(self.Task_List)
                })
                .catch(function (error) {
                    console.log(error);
                })
                .finally(function () {
                });
        },
        edit_TaskList(list = {}, target = "") {
            this.edit_target = target;
            // if ckick the </v-btn icon="$edit"> once again
            if (list.Task_List_ID === this.cache_Task_List.Task_List_ID) {
                this.clearCache()
            } else {
                this.cache_Task_List.Task_List_ID = list.Task_List_ID;
                this.cache_Task_List[`${target}`] = list[`${target}`];
            }
        },
        edit_TaskCard(task = {}, target = "") {
            this.edit_target = target;
            if (task.Task_Card_ID === this.cache_Task_Card.Task_Card_ID) {
                this.clearCache()
            } else {
                this.cache_Task_Card.Task_Card_ID = task.Task_Card_ID;
                this.cache_Task_Card[`${target}`] = task[`${target}`];
            }
        },
        doneEdit() {
            console.log("ok")
        }
    },
    mounted() {
        this.getTaskList();
    }
}
</script>

<style>
/* Small devices */
@media (min-width: 576px) {}

/* Medium devices */
@media (min-width: 768px) {}

/* Large devices */
@media (min-width: 992px) {}

.task-container {
    height: 100%;
    white-space: nowrap;
}

.task-card {
    width: 370px;
    display: inline-block;
    vertical-align: top;
}

.task_card_text {
    white-space: initial;
}
</style>