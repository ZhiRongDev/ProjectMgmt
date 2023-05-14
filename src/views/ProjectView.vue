<template>
    <AppWrapper>
        <!-- https://vuetifyjs.com/en/components/buttons/#discord-event -->
        <div class="pa-5 task-container overflow-x-auto">
            <template v-for="n in 2" :key="n">
                <v-card class="mr-5 task-card" color="#36393f" theme="dark" variant="flat">
                    <v-sheet color="#202225">
                        <v-card-item>
                            <template v-slot:prepend>
                                <!-- <v-card-title class="d-flex align-center"></v-card-title> -->
                                <v-chip class="bg-green"><strong>進行中</strong></v-chip>
                            </template>

                            <!-- edit title -->
                            <h4 v-if="!task_list_title_edit" @dblclick="task_list_title_edit = !task_list_title_edit">{{
                                task_list_title }}</h4>
                            <input v-else type="text" class="pl-1 w-100 bg-grey-lighten-5" v-model="task_list_title"
                                @keyup.esc="cancelEdit()" @blur="cancelEdit()" @keyup.enter="doneEdit()">

                            <template v-slot:append>
                                <v-btn icon="$edit" size="small" variant="text"
                                    @click="task_list_title_edit = !task_list_title_edit"></v-btn>
                                <v-btn icon="$close" size="small" variant="text"></v-btn>
                            </template>
                        </v-card-item>
                    </v-sheet>

                    <template v-for="n in 1" :key="n">
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
                                        <p class="text-h6 d-inline-block">任務卡 1</p>
                                    </div>
                                    <input v-else type="text" class="pl-1 w-100 bg-grey-lighten-5" v-model="task_list_title"
                                        @keyup.esc="cancelEdit()" @blur="cancelEdit()" @keyup.enter="doneEdit()">

                                    <p class="font-weight-light text-medium-emphasis task_card_text mb-3">
                                        Join the Vuetify team for a live Question and Answer session.
                                        Join the Vuetify team for a live Question and Answer session.assssssssssssss
                                        Join the Vuetify team for a live Question and Answer session.
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
                                    Share
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
import AppWrapper from '../components/AppWrapper.vue';

export default {
    data: () => ({
        model: null,
        Task_List: [
            {
                Task_List_ID: '12345',
                Task_List_Name: 'List1',
                Task_List_Status: true,
                Task_Card: [
                    {
                        Task_Card_ID: '54321',
                        Task_Card_Name: 'Card1',
                        Task_Card_Text: 'Card1 text',
                        Task_Card_StartTime: '1998',
                        Task_Card_EndTime: '2021',
                        Task_Card_Status: true,
                        Todo: [
                            {
                                Todo_ID: 'abc',
                                Todo_Text: 'todo text',
                                Todo_Status: true
                            }
                        ],
                        Comment: [
                            {
                                Commenter_ID: 'cba',
                                Commenter_Name: 'commenter_Name',
                                Comment_Text: 'Comment_Text'
                            }
                        ],
                        collaborators: [
                            {
                                User_ID: '',
                                User_Name: '',
                                User_Mail: '',
                                User_Avatar: '',
                                User_Password: ''
                            }
                        ],
                    }
                ]
            },
        ],
        cache_data: {

        },

        task_list_title: '測試標題',
        task_list_title_edit: false,
    }),
    components: {
        AppWrapper
    },
    methods: {
        cancelEdit() {
            this.task_list_title_edit = false;
        },
        doneEdit() {
            console.log("ok")
        }
    }
}
</script>

<style>
.task-container {
    height: 100%;
    white-space: nowrap;
}

.task-card {
    max-width: 500px;
    display: inline-block;
    vertical-align: top;
}

.task_card_text {
    white-space: initial;
}
</style>