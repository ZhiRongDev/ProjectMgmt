<template>
    <AppWrapper>
        <div class="pa-5 task-container overflow-x-auto">
            <template v-for="n in 10" :key="n">
                <v-card class="mr-5 d-inline-block">
                    <v-card-item>
                        <div>
                            <div class="text-overline mb-1">
                                OVERLINE
                            </div>
                            <div class="text-h6 mb-1">
                                Headline
                            </div>
                            <div class="text-caption">Greyhound divisely hello coldly fonwderfully</div>
                        </div>
                    </v-card-item>
                </v-card>
            </template>
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
</style>