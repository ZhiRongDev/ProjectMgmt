<template>
    <v-app id="inspire">
        <v-app-bar>
            <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
            <v-toolbar-title>ProjectMgnt</v-toolbar-title>
            <v-btn class="bg-black">登出</v-btn>
        </v-app-bar>

        <v-navigation-drawer v-model="drawer">
            <!--  -->
        </v-navigation-drawer>
        <v-main class="bg-grey-lighten-2">
            <slot></slot>
        </v-main>
    </v-app>
</template>

<script>
export default {
    data: () => ({
        drawer: false,
    }),
    mounted() {
    }
}
</script>