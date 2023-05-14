<template>
    <AppWrapper>
        <!-- https://vuetifyjs.com/en/components/buttons/#discord-event -->
        <div class="pa-5 task-container overflow-x-auto">
            <template v-for="n in 2" :key="n">
                <v-card class="mr-5 task-card" color="#36393f" theme="dark" variant="flat">
                    <v-sheet color="#202225">
                        <v-card-item>
                            <template v-slot:prepend>
                                <v-card-title class="d-flex">
                                    <!-- <v-icon icon="mdi-calendar" start></v-icon> -->
                                    <v-chip class="bg-green mr-2"><strong>進行中</strong></v-chip>
                                    1 Event
                                </v-card-title>
                            </template>

                            <v-divider vertical class="mx-2"></v-divider>

                            <template v-slot:append>
                                <v-btn icon="$close" size="large" variant="text"></v-btn>
                            </template>
                        </v-card-item>
                    </v-sheet>

                    <v-card class="ma-4" color="#2f3136" rounded="lg" variant="flat">
                        <v-card-item>
                            <v-card-title class="text-body-2 d-flex align-center">
                                <v-icon color="#949cf7" icon="mdi-calendar" start></v-icon>

                                <span class="text-medium-emphasis font-weight-bold">1 Fri Dec 16th - 9:00 PM</span>

                                <v-spacer></v-spacer>

                                <v-avatar image="https://cdn.vuetifyjs.com/images/john-smirk.png" size="x-small"></v-avatar>

                                <v-chip class="ms-2 text-medium-emphasis" color="grey-darken-4"
                                    prepend-icon="mdi-account-multiple" size="small" text="81" variant="flat"></v-chip>
                            </v-card-title>

                            <div class="py-2">
                                <div class="text-h6">Live Q&A</div>

                                <div class="font-weight-light text-medium-emphasis">
                                    Join the Vuetify team for a live Question and Answer session.
                                </div>
                            </div>
                        </v-card-item>

                        <v-divider></v-divider>

                        <div class="pa-4 d-flex align-center">
                            <v-icon color="disabled" icon="mdi-broadcast" start></v-icon>

                            <v-icon color="#949cf7" icon="mdi-video-vintage" size="x-small"></v-icon>

                            <span class="text-caption text-medium-emphasis ms-1 font-weight-light">
                                streaming
                            </span>

                            <v-spacer></v-spacer>

                            <v-icon class="me-3" icon="mdi-dots-horizontal"></v-icon>

                            <v-btn class="me-2 text-none" color="#4f545c" prepend-icon="mdi-export-variant" variant="flat">
                                Share
                            </v-btn>

                            <v-btn border class="text-none" prepend-icon="mdi-check" variant="text">
                                Interested
                            </v-btn>
                        </div>
                    </v-card>
                    <v-btn class="text-none text-subtitle-1 ma-4" color="#5865f2" variant="flat">
                        新增任務卡
                    </v-btn>
                </v-card>
            </template>
            <v-card class="mr-5 task-card">
                <v-btn size="large" class="bg-black">新增任務列表</v-btn>
            </v-card>

        </div>
    </AppWrapper>
</template>

<script>
import AppWrapper from '../components/AppWrapper.vue';

export default {
    data: () => ({
        model: null,
    }),
    components: {
        AppWrapper
    }
}
</script>

<style>
.task-container {
    height: 100%;
    white-space: nowrap;
}

.task-card {
    max-width: 650px;
    display: inline-block;
    vertical-align: top;
}
</style>