<template>
    <v-app id="inspire">
        <v-app-bar>
            <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
            <v-toolbar-title>ProjectMgnt</v-toolbar-title>
            <v-btn class="bg-black">登出</v-btn>
        </v-app-bar>

        <!-- https://vuetifyjs.com/en/components/navigation-drawers/#location -->
        <v-navigation-drawer v-model="drawer">
            <template v-slot:prepend>
                <v-list-item lines="two" prepend-avatar="https://randomuser.me/api/portraits/women/81.jpg"
                    title="Jane Smith" subtitle="Logged in"></v-list-item>
            </template>

            <v-divider></v-divider>

            <v-list density="compact" nav>
                <v-list-item prepend-icon="mdi-home-city" title="Home" value="home"></v-list-item>
                <v-list-item prepend-icon="mdi-account" title="My Account" value="account"></v-list-item>
                <v-list-item prepend-icon="mdi-account-group-outline" title="Users" value="users"></v-list-item>
            </v-list>
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