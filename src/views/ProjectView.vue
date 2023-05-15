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
                            <h4 v-if="list.Task_List_ID !== cache_Task_List.Task_List_ID"
                                @dblclick="edit_TaskList(list.Task_List_ID)">{{
                                    list.Task_List_Name }}</h4>
                            <input v-else type="text" class="pl-1 w-100 bg-grey-lighten-5" v-model="list.Task_List_Name"
                                @keyup.esc="edit_TaskList()" @blur="edit_TaskList()" @keyup.enter="doneEdit()">

                            <template v-slot:append>
                                <v-btn icon="$edit" size="small" variant="text"
                                    @click="edit_TaskList(list.Task_List_ID)"></v-btn>
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
                                    <div v-if="!task_list_title_edit">
                                        <p class="text-h6 d-inline-block">{{ task.Task_Card_Name }}</p>
                                    </div>
                                    <input v-else type="text" class="pl-1 w-100 bg-grey-lighten-5" v-model="task_list_title"
                                        @keyup.esc="cancelEdit()" @blur="cancelEdit()" @keyup.enter="doneEdit()">

                                    <p class="font-weight-light text-medium-emphasis task_card_text mb-3">
                                        {{ task.Task_Card_Text }}
                                    </p>
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
        cache_Task_List: {
            Task_List_ID: '',
            Task_List_Name: '',
            Task_List_Status: null,
        },
        cache_Task_Card: {
            Task_Card_ID: '',
            Task_Card_Name: '',
            Task_Card_Text: '',
            Task_Card_StartTime: '',
            Task_Card_EndTime: '',
            Task_Card_Status: null,
            Task_WorksOn: []
        },
        cache_Todo: {
            Todo_ID: '',
            Todo_Text: '',
            Todo_Status: null,
        },
        cache_Comment: {
            Commenter_ID: '',
            Commenter_Name: '',
            Comment_Text: '',
        },

        task_list_title: '測試標題',
        task_list_title_edit: false,

        test: {}
    }),
    components: {
        AppWrapper
    },
    methods: {
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
        edit_TaskList(id = {}) {
            if (this.cache_Task_List.Task_List_ID === id) {
                this.cache_Task_List.Task_List_ID = {};
            } else {
                this.cache_Task_List.Task_List_ID = id;
            }
        },

        cancelEdit() {
            this.task_list_title_edit = false;
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
@media (min-width: 576px) {
}

/* Medium devices */
@media (min-width: 768px) {
    .task-card {
        width: 80%;
    }
}

/* Large devices */
@media (min-width: 992px) {
    .task-card {
        width: 30%;
    }
}

.task-container {
    height: 100%;
    white-space: nowrap;
}

.task-card {
    display: inline-block;
    vertical-align: top;
}

.task_card_text {
    white-space: initial;
}
</style>