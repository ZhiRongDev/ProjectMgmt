<template>
    <AppWrapper>
        <!-- https://vuetifyjs.com/en/components/buttons/#discord-event -->
        <div class="pa-5 task-container overflow-x-auto">
            <h2 class="mb-2">{{ this.Project.Project_Name }}</h2>
            <template v-for="list in Project.Task_List" :key="list.Task_List_ID">
                <v-card class="mr-5 task-card" color="#36393f" theme="dark" variant="flat">
                    <v-sheet color="#202225">
                        <v-card-item>
                            <template v-slot:prepend>
                                <v-chip v-if="list.Task_List_Status" class="bg-green" link @click="update_Task_List(
                                    put_data = {
                                        'Task_List_ID': list.Task_List_ID,
                                        'Task_List_Status': !list.Task_List_Status
                                    }
                                )">進行中
                                </v-chip>

                                <v-chip v-else class="bg-grey" link @click="update_Task_List(
                                    put_data = {
                                        'Task_List_ID': list.Task_List_ID,
                                        'Task_List_Status': !list.Task_List_Status
                                    },
                                )">已完成</v-chip>
                            </template>

                            <!-- edit Task_List_Name -->
                            <input
                                v-if="list.Task_List_ID === cache.Task_List_item.Task_List_ID && edit_target === 'Task_List_Name'"
                                type="text" class="pl-1 w-100 bg-grey-lighten-5"
                                v-model="cache.Task_List_item.Task_List_Name" @keyup.esc="edit_Task_List()"
                                @blur="edit_Task_List()"
                                @keyup.enter="update_Task_List($event, put_data = cache.Task_List_item)">
                            <h4 v-else @dblclick="edit_Task_List(list, target = 'Task_List_Name')">{{
                                list.Task_List_Name }}</h4>

                            <template v-slot:append>
                                <v-btn icon="$edit" size="small" variant="text"
                                    @click="edit_Task_List(list, target = 'Task_List_Name')"></v-btn>
                                <v-btn icon="$close" size="small" variant="text"
                                    @click="delete_Task_List(list.Task_List_ID)"></v-btn>
                            </template>
                        </v-card-item>
                    </v-sheet>

                    <template v-for="task in list.Task_Card" :key="task.Task_Card_ID">
                        <v-card class="ma-4" color="#2f3136" rounded="lg" variant="flat">
                            <v-card-item>
                                <v-card-title class="text-body-2 d-flex align-center mb-2">
                                    <div>
                                        <v-chip v-if="task.Task_Card_Status" class="mr-3 bg-green" link @click="update_Task_Card(
                                            put_data = {
                                                'Task_Card_ID': task.Task_Card_ID,
                                                'Task_Card_Status': task.Task_Card_Status,
                                            })">進行中</v-chip>
                                        <v-chip v-else class="mr-3 bg-grey" link>已完成</v-chip>
                                    </div>

                                    <v-spacer></v-spacer>

                                    <div>
                                        <v-chip class="ms-2 text-medium-emphasis" color="grey-darken-4"
                                            prepend-icon="mdi-account-multiple" size="small"
                                            :text="task.Task_WorksOn.length.toString()" variant="flat"></v-chip>
                                    </div>
                                </v-card-title>

                                <!-- edit Task_Card_Name -->
                                <div class="py-2">
                                    <div class="d-flex justify-space-between align-center">
                                        <div class="w-100">
                                            <input
                                                v-if="task.Task_Card_ID === cache.Task_Card_item.Task_Card_ID && edit_target === 'Task_Card_Name'"
                                                type="text" class="pl-1 w-100 bg-grey-lighten-5"
                                                v-model="cache.Task_Card_item.Task_Card_Name" @keyup.esc="edit_Task_Card()"
                                                @blur="edit_Task_Card()"
                                                @keyup.enter="update_Task_Card($event, put_data = cache.Task_Card_item)">
                                            <h4 v-else class="text-h6"
                                                @dblclick="edit_Task_Card(task, target = 'Task_Card_Name')">
                                                {{ task.Task_Card_Name }}
                                            </h4>
                                        </div>
                                        <v-btn icon="$edit" size="small" variant="text"
                                            @click="edit_Task_Card(task, target = 'Task_Card_Name')"></v-btn>
                                    </div>

                                    <div class="d-flex justify-space-between mb-3"
                                        :class="{ 'align-center': task.Task_Card_ID !== cache.Task_Card_item.Task_Card_ID || edit_target !== 'Task_Card_Text' }">
                                        <v-textarea
                                            v-if="task.Task_Card_ID === cache.Task_Card_item.Task_Card_ID && edit_target === 'Task_Card_Text'"
                                            v-model="cache.Task_Card_item.Task_Card_Text"
                                            :model-value="cache.Task_Card_item.Task_Card_Text" @blur="edit_Task_Card()"
                                            @keyup.esc="edit_Task_Card()"
                                            @keyup.shift.enter="update_Task_Card($event, put_data = cache.Task_Card_item)"></v-textarea>
                                        <p v-else class="font-weight-light text-medium-emphasis task_card_text"
                                            @dblclick="edit_Task_Card(task, target = 'Task_Card_Text')">
                                            {{ task.Task_Card_Text }}
                                        </p>
                                        <v-btn icon="$edit" size="small" variant="text"
                                            @click="edit_Task_Card(task, target = 'Task_Card_Text')"></v-btn>
                                    </div>
                                    <div>
                                        <v-tooltip :text="task.Task_Card_StartTime" location="bottom">
                                            <template v-slot:activator="{ props }">
                                                <v-chip v-bind="props" class="mr-3">
                                                    開始時間
                                                </v-chip>
                                            </template>
                                        </v-tooltip>
                                        <v-tooltip :text="task.Task_Card_EndTime" location="bottom">
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
                                            <div class="d-flex align-center w-75">
                                                <div>
                                                    <v-chip v-if="task.Task_Card_Status" class="mr-3 bg-green"
                                                        link>進行中</v-chip>
                                                    <v-chip v-else class="mr-3 bg-grey" link>已完成</v-chip>
                                                </div>
                                                <input
                                                    v-if="task.Task_Card_ID === cache.Task_Card_item.Task_Card_ID && edit_target === 'Task_Card_Name'"
                                                    type="text" class="pl-1 bg-grey-lighten-5 w-100"
                                                    v-model="cache.Task_Card_item.Task_Card_Name" @blur="edit_Task_Card()"
                                                    @keyup.enter="doneEdit()">
                                                <h4 v-else class="text-h5"
                                                    @dblclick="edit_Task_Card(task, target = 'Task_Card_Name')">
                                                    {{ task.Task_Card_Name }}
                                                </h4>
                                                <v-btn icon="$edit" size="small" variant="text"
                                                    @click="edit_Task_Card(task, target = 'Task_Card_Name')"></v-btn>
                                            </div>
                                            <v-btn icon="$close" size="small" variant="text"
                                                @click="checkCard_dialog = false"></v-btn>
                                        </v-card-title>
                                        <v-card-text>
                                            <div>
                                                <h4>任務描述</h4>
                                                <v-divider class="mb-3"></v-divider>
                                                <div class="d-flex justify-space-between mb-3"
                                                    :class="{ 'align-center': task.Task_Card_ID !== cache.Task_Card_item.Task_Card_ID || edit_target !== 'Task_Card_Text' }">
                                                    <v-textarea
                                                        v-if="task.Task_Card_ID === cache.Task_Card_item.Task_Card_ID && edit_target === 'Task_Card_Text'"
                                                        v-model="cache.Task_Card_item.Task_Card_Text"
                                                        :model-value="cache.Task_Card_item.Task_Card_Text"
                                                        @blur="edit_Task_Card()"></v-textarea>
                                                    <p v-else class="font-weight-light text-medium-emphasis task_card_text"
                                                        @dblclick="edit_Task_Card(task, target = 'Task_Card_Text')">
                                                        {{ task.Task_Card_Text }}
                                                    </p>
                                                    <v-btn icon="$edit" size="small" variant="text"
                                                        @click="edit_Task_Card(task, target = 'Task_Card_Text')"></v-btn>
                                                </div>
                                                <br>

                                                <h4>任務成員</h4>
                                                <v-divider class="mb-3"></v-divider>
                                                <v-expansion-panels>
                                                    <v-expansion-panel title="查看名單">
                                                        <v-expansion-panel-text>
                                                            <v-row>
                                                                <v-col v-for="worker in task.Task_WorksOn" cols="12"
                                                                    class="d-flex align-center justify-space-between">
                                                                    <v-list-item :prepend-avatar="worker.User_Avatar"
                                                                        :title="worker.User_Name"
                                                                        :subtitle="worker.User_Mail"></v-list-item>

                                                                    <v-btn icon="$close" size="small"
                                                                        variant="text"></v-btn>
                                                                </v-col>
                                                            </v-row>
                                                            <v-row>
                                                                <v-col cols="12">
                                                                    <v-autocomplete v-model="cache.WorksOn_list"
                                                                        :items="filter_Project_WorksOn(task.Task_WorksOn)"
                                                                        chips closable-chips color="blue-grey-lighten-2"
                                                                        item-title="name" item-value="name" label="Select"
                                                                        multiple>
                                                                        <template v-slot:chip="{ props, item }">
                                                                            <v-chip v-bind="props"
                                                                                :prepend-avatar="item.raw.User_Avatar"
                                                                                :text="item.raw.User_Name"></v-chip>
                                                                        </template>

                                                                        <template v-slot:item="{ props, item }">
                                                                            <v-list-item v-bind="props"
                                                                                :prepend-avatar="item?.raw?.User_Avatar"
                                                                                :title="item?.raw?.User_Name"
                                                                                :subtitle="item?.raw?.User_Mail"></v-list-item>
                                                                        </template>
                                                                    </v-autocomplete>
                                                                </v-col>
                                                            </v-row>
                                                            <v-row>
                                                                <v-col>
                                                                    <v-btn class="text-none text-subtitle-1" color="#5865f2"
                                                                        variant="flat">新增協作者</v-btn>
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
                                                    <v-text-field v-model="cache.Todo_item.Todo_Text" label="請輸入待辦事項"
                                                        variant="solo" @keydown.enter="addTodo">
                                                        <template v-slot:append>
                                                            <v-fade-transition>
                                                                <v-icon v-if="cache.Todo_item.Todo_Text" @click="addTodo">
                                                                    mdi-plus-circle
                                                                </v-icon>
                                                            </v-fade-transition>
                                                        </template>
                                                    </v-text-field>

                                                    <v-row class="my-1" align="center">
                                                        <strong class="mx-4 text-info-darken-2">
                                                            進行中: {{ remainingTasks(task.Todo) }}
                                                        </strong>

                                                        <v-divider vertical></v-divider>

                                                        <strong class="mx-4 text-success-darken-2">
                                                            已完成: {{ completedTasks(task.Todo) }}
                                                        </strong>

                                                        <v-spacer></v-spacer>
                                                    </v-row>

                                                    <v-divider class="mb-4"></v-divider>

                                                    <v-card v-if="task.Todo.length > 0">
                                                        <v-slide-y-transition class="py-0" group tag="v-list">
                                                            <template v-for="(todo, i) in task.Todo"
                                                                :key="`${i}-${todo.Todo_Text}`">
                                                                <v-divider v-if="i !== 0" :key="`${i}-divider`"></v-divider>

                                                                <v-list-item>
                                                                    <v-list-item-action
                                                                        class="d-flex align-center justify-space-between py-2">
                                                                        <div class="d-flex align-center">
                                                                            <v-chip v-if="todo.Todo_Status"
                                                                                @click="doneEdit()" class="mr-3 bg-green"
                                                                                link>進行中</v-chip>
                                                                            <v-chip v-else @click="doneEdit()"
                                                                                class="mr-3 bg-grey" link>已完成</v-chip>
                                                                            <p
                                                                                :class="todo.Todo_Status && 'text-success' || 'text-grey'">
                                                                                {{ todo.Todo_Text }}</p>
                                                                        </div>

                                                                        <v-btn density="compact" icon="mdi-close"
                                                                            class="mr-3"></v-btn>
                                                                    </v-list-item-action>
                                                                </v-list-item>
                                                            </template>
                                                        </v-slide-y-transition>
                                                    </v-card>

                                                </div>

                                                <br>

                                                <h4>留言區</h4>
                                                <v-divider class="mb-3"></v-divider>
                                                <v-text-field v-model="cache.Comment_item.Commenter_Name" label="請輸入留言"
                                                    variant="solo" @keydown.enter="">
                                                    <template v-slot:append>
                                                        <v-fade-transition>
                                                            <v-icon v-if="cache.Comment_item.Commenter_Name" @click="">
                                                                mdi-plus-circle
                                                            </v-icon>
                                                        </v-fade-transition>
                                                    </template>
                                                </v-text-field>

                                                <v-row>
                                                    <v-col v-for="comment in task.Comment" cols="12"
                                                        class="d-flex align-center justify-space-between">
                                                        <div class="d-flex align-center">
                                                            <v-list-item :prepend-avatar="comment.Commenter_Avatar"
                                                                :title="comment.Commenter_Name"
                                                                :subtitle="comment.Commenter_Mail"
                                                                class="mr-3"></v-list-item>
                                                            <p> {{ comment.Comment_Text }}</p>

                                                        </div>
                                                        <v-btn icon="$close" size="small" variant="text"></v-btn>
                                                    </v-col>
                                                </v-row>


                                                <br>

                                                <h4>時間設定</h4>
                                                <v-divider class="mb-3"></v-divider>
                                                <div class="d-flex align-center mb-5">
                                                    <div>
                                                        <v-chip class="mr-3">
                                                            開始時間
                                                        </v-chip>
                                                    </div>
                                                    <input type="date" :value="task.Task_Card_StartTime">
                                                </div>

                                                <div class="d-flex align-center mb-3">
                                                    <div>
                                                        <v-chip class="mr-3">
                                                            截止時間
                                                        </v-chip>
                                                    </div>
                                                    <input type="date" :value="task.Task_Card_EndTime">
                                                </div>

                                            </div>
                                        </v-card-text>
                                        <v-card-actions>
                                            <v-spacer></v-spacer>
                                            <v-btn color="blue-darken-1" variant="text" @click="checkCard_dialog = false">
                                                Close
                                            </v-btn>
                                        </v-card-actions>
                                    </v-card>
                                </v-dialog>

                                <v-btn class="text-none bg-red" variant="flat" @click="delete_Task_Card(task.Task_Card_ID)">
                                    刪除
                                </v-btn>
                            </div>
                        </v-card>
                    </template>
                    <!--  -->
                    <v-dialog v-model="newCard_dialog" persistent width="50%">
                        <template v-slot:activator="{ props }">
                            <v-btn v-bind="props" class="text-none text-subtitle-1 ma-4" color="#5865f2" variant="flat">
                                新增任務卡
                            </v-btn>
                        </template>
                        <v-card>
                            <v-card-title>
                                <span class="text-h5">新增任務卡</span>
                            </v-card-title>
                            <v-card-text>
                                <v-container>
                                    <v-row>
                                        <v-col cols="12">
                                            <v-text-field label="任務標題" required
                                                v-model="cache.Task_Card_item.Task_Card_Name"></v-text-field>
                                            <v-textarea label="任務描述" required
                                                v-model="cache.Task_Card_item.Task_Card_Text"></v-textarea>
                                        </v-col>
                                    </v-row>
                                </v-container>
                            </v-card-text>
                            <v-card-actions>
                                <v-spacer></v-spacer>
                                <v-btn color="blue-darken-1" variant="text" @click="newCard_dialog = false; clearCache()">
                                    Close
                                </v-btn>
                                <v-btn color="blue-darken-1" variant="text"
                                    @click="newCard_dialog = false; create_Task_Card(cache.Task_Card_item)">
                                    Save
                                </v-btn>
                            </v-card-actions>
                        </v-card>
                    </v-dialog>
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
                                    <v-text-field label="輸入列表名稱" required
                                        v-model="cache.Task_List_item.Task_List_Name"></v-text-field>
                                </v-col>
                            </v-row>
                        </v-container>
                    </v-card-text>
                    <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn color="blue-darken-1" variant="text" @click="newList_dialog = false; clearCache()">
                            Close
                        </v-btn>
                        <v-btn color="blue-darken-1" variant="text"
                            @click="newList_dialog = false; create_Task_List(cache.Task_List_item)">
                            Save
                        </v-btn>
                    </v-card-actions>
                </v-card>
            </v-dialog>

            <!--  -->
            <v-dialog v-model="Project_WorksOn_dialog" persistent width="50%">
                <template v-slot:activator="{ props }">
                    <v-btn v-bind="props" size="large" class="mr-5 d-inline-block bg-primary">成員列表</v-btn>
                </template>
                <v-card>
                    <v-card-title>
                        <span class="text-h5">成員列表</span>
                    </v-card-title>
                    <v-card-text>
                        <v-container>
                            <v-row>
                                <v-col cols="12">
                                    <v-text-field label="輸入信箱新增成員" required v-model="cache.WorksOn_Email" @keyup.enter="add_WorksOn()"></v-text-field>
                                    <v-row>
                                        <v-col v-for="worker in Project.Project_WorksOn" cols="12"
                                            class="d-flex align-center justify-space-between">
                                            <v-list-item :prepend-avatar="worker.User_Avatar" :title="worker.User_Name"
                                                :subtitle="worker.User_Mail"></v-list-item>

                                            <v-btn icon="$close" size="small" variant="text" @click="delete_WorksOn(worker.User_ID)"></v-btn>
                                        </v-col>
                                    </v-row>
                                </v-col>
                            </v-row>
                            <v-row>

                            </v-row>
                        </v-container>
                    </v-card-text>
                    <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn color="blue-darken-1" variant="text" @click="Project_WorksOn_dialog = false">
                            Close
                        </v-btn>
                    </v-card-actions>
                </v-card>
            </v-dialog>

            <!-- 提示訊息 -->
            <v-snackbar v-model="snackbar" timeout="2000">
                {{ snackbar_msg }}
                <template v-slot:actions>
                    <v-btn color="blue" variant="text" @click="snackbar = false">
                        Close
                    </v-btn>
                </template>
            </v-snackbar>

        </div>
    </AppWrapper>
</template>

<script>
import axios from "axios";
import { mapState, mapActions } from 'pinia'
import UserStatus from '@/stores/UserStatus'
import AppWrapper from '../components/AppWrapper.vue';
import { queuePostFlushCb } from "vue";

export default {
    data() {
        return {
            tab: null,
            model: null,
            newList_dialog: false,
            newCard_dialog: false,
            checkCard_dialog: false,
            Project_WorksOn_dialog: false,

            Project: {},

            edit_target: "",

            // caches are used for update, they should always be empty objects when not updating.
            cache: {
                Task_List_item: {},
                Task_Card_item: {},
                Todo_item: {},
                Comment_item: {},
                WorksOn_list: [], // Used in Todo List, to show Project WorksOn
                WorksOn_Email: "",
            },

            snackbar_msg: "",
            snackbar: false,
        }
    },
    components: {
        AppWrapper,
    },
    computed: {
        ...mapState(UserStatus, ['User']),

        completedTasks() {
            return function (Todos) {
                return Todos.filter(todo => !todo.Todo_Status).length
            }
        },

        remainingTasks() {
            return function (Todos) {
                return Todos.length - this.completedTasks(Todos)
            }
        },

        // Only show Project_WorksOn which is not in Task_WorksOn 
        filter_Project_WorksOn() {
            return function (Task_WorksOn) {
                return this.Project.Project_WorksOn.filter(item1 => {
                    return !Task_WorksOn.some(item2 => {
                        return Object.keys(item1).every(key => item1[key] === item2[key]);
                    });
                })
            }
        }
    },
    methods: {
        ...mapActions(UserStatus, ['checkAuth']),
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
            let cache = {
                Task_List_item: {},
                Task_Card_item: {},
                Todo_item: {},
                Comment_item: {},
                WorksOn_list: [],
                WorksOn_Email: "",
            }
            this.cache = JSON.parse(JSON.stringify(cache)); // DeepCopy
            this.edit_target = ""
        },

        getProject() {
            let self = this;
            let url = `${import.meta.env.VITE_FLASK_URL}/Project/Content?User_ID=${this.User.User_ID}&Project_ID=${this.$route.query.Project_ID}`;
            axios.get(url)
                .then(function (res) {
                    self.Project = res.data.return_data;
                })
                .catch(function (err) {
                    self.snackbar_msg = err.response.data;
                    self.snackbar = true;
                })
        },

        create_Task_List(post_data = {}) {
            let Task_List_ID = Date.now()
            post_data.Task_List_ID = Task_List_ID

            let self = this;
            let url = `${import.meta.env.VITE_FLASK_URL}/Task_List?User_ID=${this.User.User_ID}`;

            axios.post(url, post_data)
                .then(function (res) {
                    self.getProject();
                    self.snackbar_msg = res.data.response;
                    self.snackbar = true;
                })
                .catch(function (err) {
                    console.log(err);
                })
            this.clearCache();
        },

        create_Task_Card(post_data = {}) {
            let Task_Card_ID = Date.now()
            post_data.Task_Card_ID = Task_Card_ID
            // console.log(post_data);


            let self = this;
            let url = `${import.meta.env.VITE_FLASK_URL}/Task_Card?User_ID=${this.User.User_ID}`;

            axios.post(url, post_data)
                .then(function (res) {
                    self.getProject();
                    self.snackbar_msg = res.data.response;
                    self.snackbar = true;
                })
                .catch(function (err) {
                    console.log(err);
                })
            this.clearCache();
        },

        // https://stackoverflow.com/questions/61776432/how-to-unset-focus-on-an-input-after-keyup-enter-event-in-vuejs
        update_Task_List(event = "", put_data = {}) {
            
            // console.log(event.target)

            let self = this;
            let url = `${import.meta.env.VITE_FLASK_URL}/Task_List?User_ID=${this.User.User_ID}`;

            axios.put(url, put_data)
                .then(function (res) {
                    self.getProject();
                    if (event.target) {
                        event.target.blur();
                    }
                    self.snackbar_msg = res.data.response;
                    self.snackbar = true;
                })
                .catch(function (err) {
                    console.log(err);
                })
            this.clearCache();
        },

        update_Task_Card(event = "", put_data = {}) {
            let self = this;
            let url = `${import.meta.env.VITE_FLASK_URL}/Task_Card?User_ID=${this.User.User_ID}`;

            axios.put(url, put_data)
                .then(function (res) {
                    self.getProject();
                    if (event.target) {
                        event.target.blur();
                    }
                    self.snackbar_msg = res.data.response;
                    self.snackbar = true;
                })
                .catch(function (err) {
                    console.log(err);
                })
            this.clearCache();
        },

        delete_Task_List(Task_List_ID) {
            // console.log(Task_List_ID)
            let self = this;
            let url = `${import.meta.env.VITE_FLASK_URL}/Task_List?User_ID=${this.User.User_ID}&Task_List_ID=${Task_List_ID}`;

            axios.delete(url)
                .then(function (res) {
                    self.getProject();
                    self.snackbar_msg = res.data.response;
                    self.snackbar = true;
                })
                .catch(function (err) {
                    console.log(err);
                })
        },

        delete_Task_Card(Task_Card_ID) {
            console.log(Task_Card_ID)
            let self = this;
            let url = `${import.meta.env.VITE_FLASK_URL}/Task_Card?User_ID=${this.User.User_ID}&Task_Card_ID=${Task_Card_ID}`;

            axios.delete(url)
                .then(function (res) {
                    self.getProject();
                    self.snackbar_msg = res.data.response;
                    self.snackbar = true;
                })
                .catch(function (err) {
                    console.log(err);
                })
        },

        // Only to activate the input field
        edit_Task_List(list = {}, target = "") {
            this.edit_target = target;
            // if ckick the </v-btn icon="$edit"> once again
            if (list.Task_List_ID === this.cache.Task_List_item.Task_List_ID) {
                this.clearCache()
            } else {
                this.cache.Task_List_item.Task_List_ID = list.Task_List_ID;
                this.cache.Task_List_item[`${target}`] = list[`${target}`];
            }
        },

        // Only to activate the input field
        edit_Task_Card(task = {}, target = "") {
            this.edit_target = target;
            if (task.Task_Card_ID === this.cache.Task_Card_item.Task_Card_ID) {
                this.clearCache()
            } else {
                this.cache.Task_Card_item.Task_Card_ID = task.Task_Card_ID;
                this.cache.Task_Card_item[`${target}`] = task[`${target}`];
            }
        },

        add_WorksOn() {
            let self = this;
            let url = `${import.meta.env.VITE_FLASK_URL}/WorksOn?User_ID=${this.User.User_ID}`;

            let post_data = {
                "Project_ID": this.$route.query.Project_ID,
                "User_Mail": this.cache.WorksOn_Email
            }

            axios.post(url, post_data)
                .then(function (res) {
                    self.getProject();
                    self.snackbar_msg = res.data.response;
                    self.snackbar = true;
                })
                .catch(function (err) {
                    console.log(err);
                })
        },

        delete_WorksOn(Worker_ID) {
            console.log(Worker_ID)
            let self = this;
            let url = `${import.meta.env.VITE_FLASK_URL}/WorksOn?User_ID=${this.User.User_ID}&Project_ID=${this.$route.query.Project_ID}&Worker_ID=${Worker_ID}`;

            axios.delete(url)
                .then(function (res) {
                    self.getProject();
                    self.snackbar_msg = res.data.response;
                    self.snackbar = true;
                })
                .catch(function (err) {
                    console.log(err);
                })
        },

        doneEdit() {
            console.log("ok");
            this.getProject();
        },
    },

    mounted() {
        (async () => {
            await this.checkAuth();
            await this.getProject();
        })();

        // console.log(this.$route.query.Project_ID)
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
}</style>