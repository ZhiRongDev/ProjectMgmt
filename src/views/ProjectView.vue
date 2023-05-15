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

                                    <div class="d-flex justify-space-between mb-3"
                                        :class="{ 'align-center': task.Task_Card_ID !== cache_Task_Card.Task_Card_ID || edit_target !== 'Task_Card_Text' }">
                                        <v-textarea
                                            v-if="task.Task_Card_ID === cache_Task_Card.Task_Card_ID && edit_target === 'Task_Card_Text'"
                                            v-model="cache_Task_Card.Task_Card_Text"
                                            :model-value="cache_Task_Card.Task_Card_Text"
                                            @blur="edit_TaskCard()"></v-textarea>
                                        <p v-else class="font-weight-light text-medium-emphasis task_card_text"
                                            @dblclick="edit_TaskCard(task, target = 'Task_Card_Text')">
                                            {{ task.Task_Card_Text }}
                                        </p>
                                        <v-btn icon="$edit" size="small" variant="text"
                                            @click="edit_TaskCard(task, target = 'Task_Card_Text')"></v-btn>
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
                                <v-dialog v-model="checkCard_dialog" persistent width="100%">
                                    <template v-slot:activator="{ props }">
                                        <v-btn v-bind="props" class="mr-3 text-none" color="#4f545c" variant="flat">
                                            查看
                                        </v-btn>
                                    </template>
                                    <v-card class="pa-3">
                                        <v-card-title class="d-flex align-center justify-space-between">
                                            <div class="d-flex align-center">
                                                <v-chip v-bind="props" class="mr-3 bg-green">已完成</v-chip>
                                                <span class="text-h5"> {{ task.Task_Card_Name }} </span>
                                            </div>
                                            <div>
                                                <v-btn icon="$edit" size="small" variant="text" @click=""></v-btn>
                                                <v-btn icon="$close" size="small" variant="text" @click=""></v-btn>
                                            </div>
                                        </v-card-title>
                                        <v-card-text>
                                            <div>
                                                <h4>任務描述</h4>
                                                <v-divider class="mb-3"></v-divider>
                                                <p>
                                                    完成資料庫系統的專案
                                                </p>
                                                <br>

                                                <h4>任務成員</h4>
                                                <v-divider class="mb-3"></v-divider>
                                                <v-expansion-panels>
                                                    <v-expansion-panel title="查看名單">
                                                        <v-expansion-panel-text>
                                                            <v-row>
                                                                <v-col v-for="i in 4" cols="12">
                                                                    <v-list-item
                                                                        prepend-avatar="https://randomuser.me/api/portraits/women/81.jpg"
                                                                        title="Jane Smith"
                                                                        subtitle="jordan990301@gmail.com"></v-list-item>
                                                                </v-col>
                                                            </v-row>
                                                        </v-expansion-panel-text>
                                                    </v-expansion-panel>
                                                </v-expansion-panels>
                                                <br>

                                                <!-- https://vuetifyjs.com/en/styles/transitions/#todo-list -->
                                                <h4>待辦清單</h4>
                                                <v-divider class="mb-3"></v-divider>
                                                <div>
                                                    <v-text-field v-model="newTask" label="請輸入待辦事項"
                                                        variant="solo" @keydown.enter="addTodo">
                                                        <template v-slot:append>
                                                            <v-fade-transition>
                                                                <v-icon v-if="newTask" @click="addTodo">
                                                                    mdi-plus-circle
                                                                </v-icon>
                                                            </v-fade-transition>
                                                        </template>
                                                    </v-text-field>

                                                    <v-row class="my-1" align="center">
                                                        <strong class="mx-4 text-info-darken-2">
                                                            進行中: {{ remainingTasks }}
                                                        </strong>

                                                        <v-divider vertical></v-divider>

                                                        <strong class="mx-4 text-success-darken-2">
                                                            已完成: {{ completedTasks }}
                                                        </strong>

                                                        <v-spacer></v-spacer>

                                                        <v-progress-circular v-model="progress"
                                                            class="me-2"></v-progress-circular>
                                                    </v-row>

                                                    <v-divider class="mb-4"></v-divider>

                                                    <v-card v-if="tasks.length > 0">
                                                        <v-slide-y-transition class="py-0" group tag="v-list">
                                                            <template v-for="(task, i) in tasks" :key="`${i}-${task.text}`">
                                                                <v-divider v-if="i !== 0" :key="`${i}-divider`"></v-divider>

                                                                <v-list-item>
                                                                    <v-list-item-action>
                                                                        <v-checkbox v-model="task.done"
                                                                            :color="task.done && 'grey' || 'primary'">
                                                                            <template v-slot:label>
                                                                                <div :class="task.done && 'text-grey' || 'text-primary'"
                                                                                    class="ms-4" v-text="task.text"></div>
                                                                            </template>
                                                                        </v-checkbox>
                                                                    </v-list-item-action>

                                                                    <v-spacer></v-spacer>

                                                                    <v-scroll-x-transition>
                                                                        <v-icon v-if="task.done" color="success">
                                                                            mdi-check
                                                                        </v-icon>
                                                                    </v-scroll-x-transition>
                                                                </v-list-item>
                                                            </template>
                                                        </v-slide-y-transition>
                                                    </v-card>

                                                </div>
                                                <br>

                                                <h4>留言區</h4>
                                                <v-divider class="mb-3"></v-divider>

                                                <br>

                                                <h4>時間設定</h4>
                                                <v-divider class="mb-3"></v-divider>

                                            </div>
                                        </v-card-text>
                                        <v-card-actions>
                                            <v-spacer></v-spacer>
                                            <v-btn color="blue-darken-1" variant="text" @click="checkCard_dialog = false">
                                                Close
                                            </v-btn>
                                            <v-btn color="blue-darken-1" variant="text" @click="checkCard_dialog = false">
                                                Save
                                            </v-btn>
                                        </v-card-actions>
                                    </v-card>
                                </v-dialog>

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
            <!--  -->
            <v-dialog v-model="newList_dialog" persistent width="50%">
                <template v-slot:activator="{ props }">
                    <v-btn v-bind="props" size="large" class="mr-5 d-inline-block bg-black">新增任務列表</v-btn>
                </template>
                <v-card>
                    <v-card-title>
                        <span class="text-h5">新增任務列表</span>
                    </v-card-title>
                    <v-card-text>
                        <v-container>
                            <v-row>
                                <v-col cols="12">
                                    <v-text-field label="名稱" required></v-text-field>
                                </v-col>
                            </v-row>
                        </v-container>
                    </v-card-text>
                    <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn color="blue-darken-1" variant="text" @click="newList_dialog = false">
                            Close
                        </v-btn>
                        <v-btn color="blue-darken-1" variant="text" @click="newList_dialog = false">
                            Save
                        </v-btn>
                    </v-card-actions>
                </v-card>
            </v-dialog>
        </div>
    </AppWrapper>
</template>

<script>
import axios from "axios";
import AppWrapper from '../components/AppWrapper.vue';

export default {
    data() {
        return {
            tab: null,
            model: null,
            newList_dialog: false,
            checkCard_dialog: false,
            Task_List: [],
            Project_WorksOn: [],
            // caches are used for update, they should always be empty objects when not updating.
            cache_Task_List: {},
            cache_Task_Card: {},
            cache_Todo: {},
            cache_Comment: {},
            edit_target: "",

            //
            tasks: [
                {
                    done: false,
                    text: 'Foobar',
                },
                {
                    done: false,
                    text: 'Fizzbuzz',
                },
            ],
            newTask: null,
        }
    },
    components: {
        AppWrapper,
    },
    computed: {
        completedTasks() {
            return this.tasks.filter(task => task.done).length
        },
        progress() {
            return this.completedTasks / this.tasks.length * 100
        },
        remainingTasks() {
            return this.tasks.length - this.completedTasks
        },
    },
    methods: {
        addTodo() {
            this.tasks.push({
                done: false,
                text: this.newTask,
            })

            this.newTask = null
        },

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